import streamlit as st
from fuzzywuzzy import fuzz
from fpdf import FPDF
import pandas as pd

# --- وظيفة إنشاء تقرير PDF ---
def create_pdf(alert_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Marka-Sentry Algeria: Alert Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Reference: MS-DZ-2026-432", ln=True, align='L')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="1. Detected Risk Detail:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"- Original Brand: {alert_data['original']}\n- Detected in BOPI: {alert_data['detected']}\n- Similarity Score: {alert_data['score']}%")
    
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="2. Legal Basis (Algerian Law):", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Based on Ordinance 03-06, this similarity may cause public confusion. Action is recommended within 30 days of publication.")
    
    return pdf.output(dest='S').encode('latin-1')

# --- واجهة الموقع ---
st.set_page_config(page_title="Marka-Sentry Algeria", layout="wide")
st.title("🛡️ Marka-Sentry: نظام الإنذار المبكر")

# بيانات المجلة رقم 432 المستخرجة
bopi_data = [
    {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"},
    {"ID": "139331", "Brand": "Go Play Market", "Owner": "Ooredoo IP LLC (Qatar)", "Class": "9"},
    {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"},
]

st.sidebar.header("لوحة التحكم")
target = st.sidebar.text_input("أدخل اسم علامتك الأصلية:", "MASILECT")

st.header(f"نتائج البحث عن العلامة: {target}")

# منطق المراقبة
found = False
for item in bopi_data:
    score = fuzz.ratio(target.upper(), item['Brand'].upper())
    if score > 60: # عتبة الخطورة
        found = True
        st.error(f"⚠️ خطر مرتفع! تم رصد تشابه مع العلامة رقم {item['ID']} ({item['Brand']})")
        st.write(f"**المالك المنشور:** {item['Owner']} | **الفئات:** {item['Class']}")
        
        # بيانات التقرير
        alert_info = {
            "original": target,
            "detected": item['Brand'],
            "score": score
        }
        
        # زر تحميل التقرير
        pdf_bytes = create_pdf(alert_info)
        st.download_button(
            label="📄 تحميل تقرير الإنذار (PDF)",
            data=pdf_bytes,
            file_name=f"Alert_{target}.pdf",
            mime="application/pdf"
        )

if not found:
    st.success("✅ لم يتم رصد أي مخاطر في المجلة رقم 432")

st.divider()
st.info("ملاحظة: المواعيد القانونية للمعارضة تبدأ من تاريخ نشر المجلة في ديسمبر 2025.")

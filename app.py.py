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
import streamlit as st
from PIL import Image
import cv2
import numpy as np

# --- قسم التحقق البصري ---
st.sidebar.divider()
st.sidebar.header("📸 التحقق بالصورة (Visual Match)")
uploaded_file = st.sidebar.file_uploader("ارفع شعار الموكل الأجنبي:", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # عرض الصورة الأصلية للموكل
    image = Image.open(uploaded_file)
    st.image(image, caption='شعار الموكل المراد حمايته', width=150)
    
    with st.spinner('جاري المسح البصري لصفحات المجلة 432...'):
        # محاكاة منطق البحث البصري عن العلامات الملونة في المجلة
        st.warning("⚠️ تنبيه بصري: تم رصد تشابه لوني مع العلامة رقم 139326 (تيتا Titta).")
        st.info("التحليل التقني: تشابه في استخدام اللون البرتقالي والخط المزخرف في الفئة 30 (بسكويت).")
        
        # ربط النتيجة بالتقرير القانوني
        if st.button("توليد تقرير تحليل بصري (PDF)"):
             st.write("جاري إعداد التقرير بناءً على معايير 'التضليل البصري' في القانون الجزائري...")
            import streamlit as st
from fuzzywuzzy import fuzz
from fpdf import FPDF
import pandas as pd

# إعدادات الواجهة المتجاوبة للهاتف
st.set_page_config(page_title="Marka-Sentry DZ", layout="centered")

# CSS مخصص لجعل الأزرار كبيرة وسهلة الضغط على الهاتف
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Marka-Sentry Algeria")

# بيانات النشرة رقم 432 (ديسمبر 2025)
bopi_data = [
    {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"}, #
    {"ID": "139331", "Brand": "Go Play Market", "Owner": "Ooredoo IP LLC (Qatar)", "Class": "9"}, #
    {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"}, #
    {"ID": "139326", "Brand": "Titta", "Owner": "SARL GROUPE LYDIA SERVICE", "Class": "30"} #
]

# خيارات التطبيق
tab1, tab2 = st.tabs(["🔍 بحث نصي", "📸 مسح ميداني"])

with tab1:
    target = st.text_input("أدخل اسم العلامة الأصلية لحمايتها:", placeholder="مثال: MICRO LABS")
    if target:
        found = False
        for item in bopi_data:
            score = fuzz.partial_ratio(target.upper(), item['Brand'].upper())
            if score > 65:
                found = True
                st.error(f"🚨 تنبيه: تم رصد تشابه بنسبة {score}%")
                st.write(f"**العلامة:** {item['Brand']} | **المالك:** {item['Owner']}")
                st.caption(f"منشورة في العدد 432 - ديسمبر 2025")
        if not found:
            st.success("✅ لم يتم رصد تهديدات لهذه العلامة حالياً.")

with tab2:
    st.info("استخدم كاميرا الهاتف لتصوير علامة تجارية في السوق ومقارنتها بسجلات ديسمبر 2025.")
    # هذا الزر سيفتح الكاميرا مباشرة على الأندرويد
    cam_file = st.camera_input("التقط صورة للعلامة المشبوهة")
    if cam_file:
        st.warning("جاري تحليل البصمة البصرية للعلامة... (قيد التطوير)")

st.divider()
st.caption("بناءً على الأمر 03-06 المتعلق بالعلامات في الجزائر")

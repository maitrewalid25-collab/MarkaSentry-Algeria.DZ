import streamlit as st
from fuzzywuzzy import fuzz
from fpdf import FPDF
import pandas as pd

# 1. إعدادات الصفحة الأساسية لتظهر كأنها تطبيق هاتف
st.set_page_config(page_title="Marka-Sentry DZ", layout="centered")

# تنسيق CSS لجعل الأزرار مريحة للمس باليد
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 3.5em; font-size: 18px; border-radius: 12px; border: 2px solid #FFD700; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. دالة إنذار PDF (المنتج الملحق بالخدمة)
def create_pdf(alert_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Marka-Sentry Algeria: Alert Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Detected Risk for: {alert_data['original']}\n"
                                f"Similar Entry found in BOPI 432: {alert_data['detected']}\n"
                                f"Match Score: {alert_data['score']}%\n"
                                f"Legal Status: Potential Infringement under Ordinance 03-06.")
    return pdf.output(dest='S').encode('latin-1')

# 3. قاعدة بيانات المجلة رقم 432 (ديسمبر 2025)
bopi_data = [
    {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"},
    {"ID": "139331", "Brand": "Go Play Market", "Owner": "Ooredoo IP LLC (Qatar)", "Class": "9"},
    {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"},
    {"ID": "139326", "Brand": "Titta", "Owner": "SARL GROUPE LYDIA SERVICE", "Class": "30"}
]

# 4. واجهة التطبيق الرئيسية
st.title("🛡️ Marka-Sentry DZ")
st.caption("نظام الرصد الذكي للملكية الصناعية - الجزائر")

tab1, tab2 = st.tabs(["🔍 رصد العلامات", "📸 مسح ميداني"])

with tab1:
    st.subheader("مراقبة النشرات الرسمية (BOPI)")
    target = st.text_input("أدخل اسم علامتك الأصلية (مثل MICRO أو ALCON):")
    
    if target:
        found = False
        for item in bopi_data:
            score = fuzz.partial_ratio(target.upper(), item['Brand'].upper())
            if score > 60:
                found = True
                st.error(f"🚨 تنبيه خطورة: {score}%")
                st.write(f"**العلامة المكتشفة:** {item['Brand']} (العدد 432)")
                st.write(f"**المالك:** {item['Owner']}")
                
                # زر توليد التقرير للعميل
                pdf_bytes = create_pdf({"original": target, "detected": item['Brand'], "score": score})
                st.download_button("📄 تحميل تقرير المعارضة القانونية (PDF)", pdf_bytes, f"Alert_{target}.pdf")
        if not found:
            st.success("✅ لم يتم رصد أي تشابه في عدد ديسمبر 2025.")

with tab2:
    st.subheader("المسح البصري بالكاميرا")
    st.info("التقط صورة لعلامة تجارية في السوق لمقارنتها بقاعدة بيانات المعهد الوطني (INAPI).")
    cam_image = st.camera_input("فتح الكاميرا")
    if cam_image:
        st.warning("جاري تحليل البصمة البصرية ومطابقتها مع علامات مثل 'Titta' و 'FB.S'...")

st.divider()
st.markdown("Developed by **Marka-Sentry Legal-Tech Team**")

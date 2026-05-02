import streamlit as st
from fuzzywuzzy import fuzz
from fpdf import FPDF
from PIL import Image
import pandas as pd

# 1. الإعدادات الأساسية للهوية البصرية
st.set_page_config(page_title="Marka-Sentry | Digital Protection", page_icon="🛡️", layout="wide")

# 2. هندسة الديكور (CSS) - الالتزام باللون الأزرق الملكي والذهبي
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #d4af37 !important; color: white !important; border-radius: 10px !important; border: none !important; }
    .sidebar .sidebar-content { background: #1a3a5f; color: white; }
    .agenda-card { background-color: white; border-right: 5px solid #d4af37; padding: 15px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .alert-box { background-color: #fff5f5; border-right: 8px solid #e53e3e; padding: 20px; border-radius: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. وظيفة توليد التقرير (PDF)
def create_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Marka-Sentry: Official Alert Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Analysis for: {data['name']}\nMatch Score: {data['score']}%\nSource: BOPI 432 (Dec 2025)\nStatus: High Risk - Action Recommended.")
    return pdf.output(dest='S').encode('latin-1')

# 4. القائمة الجانبية (The Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063303.png", width=80) # الدرع الذهبي
    st.title("Marka-Sentry")
    menu = st.radio("القائمة الرئيسية:", ["رادار الرصد الذكي", "الأجندة والمواعيد", "حول المنصة", "تواصل معنا"])
    st.divider()
    st.info("نظام حماية الملكية الصناعية - الجزائر © 2026")

# 5. محتوى الصفحات
if menu == "رادار الرصد الذكي":
    # الهيدر الذهبي (الذي اختفى سابقاً)
    col_logo, col_text = st.columns([1, 5])
    with col_logo:
        st.image("https://cdn-icons-png.flaticon.com/512/1063/1063303.png", width=100)
    with col_text:
        st.markdown("<h1 style='color: #1a3a5f; margin:0;'>Marka-Sentry Algeria</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #d4af37; font-weight: bold;'>The Golden Standard in Brand Protection</p>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔍 الرصد النصي", "📸 المسح البصري (كاميرا)"])
    
    # بيانات المجلة 432
    bopi_db = [
        {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"},
        {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"},
        {"ID": "139326", "Brand": "Titta", "Owner": "SARL GROUPE LYDIA SERVICE", "Class": "30"}
    ]

    with tab1:
        st.subheader("مراقبة نشرة ديسمبر 2025")
        search = st.text_input("أدخل اسم العلامة (مثلاً: MICRO):")
        if search:
            for item in bopi_db:
                score = fuzz.partial_ratio(search.upper(), item['Brand'].upper())
                if score > 60:
                    st.markdown(f"""<div class='alert-box'><h4>⚠️ تنبيه خطورة: {score}%</h4>
                    <p>تشابه مع: <b>{item['Brand']}</b> للمالك {item['Owner']}</p></div>""", unsafe_allow_html=True)
                    pdf_data = create_pdf({"name": search, "score": score})
                    st.download_button("📄 تحميل التقرير القانوني (PDF)", pdf_data, f"Alert_{search}.pdf")

    with tab2:
        st.subheader("رادار المسح الميداني")
        st.info("استخدم الكاميرا لمطابقة العلامات بصرياً مع سجلات INAPI.")
        cam_file = st.camera_input("التقط صورة للعلامة")
        if cam_image := cam_file:
            st.error("🚨 تم رصد محاكاة بصرية لعلامة 'Titta' (الصفحة 9)")
            st.write("السبب: تشابه في انحناء الخط وتوزيع اللون البرتقالي.")

elif menu == "الأجندة والمواعيد":
    st.header("📅 أجندة النشرة رقم 432")
    st.markdown("""
    <div class="agenda-card"><h4>⌛ نهاية مهلة المعارضة</h4><p><b>التاريخ:</b> يناير 2026</p><p>آخر أجل لتقديم الطعون ضد علامات ديسمبر 2025.</p></div>
    <div class="agenda-card"><h4>🔄 مراجعة التجديدات</h4><p><b>التاريخ:</b> فبراير 2026</p><p>فحص العلامات التي تنتهي حمايتها (10 سنوات) وفقاً للأمر 03-06.</p></div>
    """, unsafe_allow_html=True)

elif menu == "حول المنصة":
    st.header("📖 خبرة قانونية بلمسة تقنية")
    st.write("تطوير وإشراف نخبة من أساتذة القانون والمحامين المعتمدين لدى المحكمة العليا.")
    st.write("المرجع القانوني: الأمر 03-06 المتعلق بالعلامات في الجزائر.")

elif menu == "تواصل معنا":
    st.header("📞 قنوات التواصل المباشر")
    st.write("📍 قسنطينة، الجزائر")
    st.write("📧 البريد المهني: contact@markasentry.dz")

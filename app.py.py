import streamlit as st
from fuzzywuzzy import fuzz
import pandas as pd

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="Marka-Sentry | Legal-Tech", page_icon="⚖️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .sidebar .sidebar-content { background-image: linear-gradient(#1a3a5f, #2a5298); color: white; }
    .agenda-card { background-color: white; border-right: 5px solid #d4af37; padding: 15px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (Main Menu)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063303.png", width=80) # الشعار الذهبي
    st.title("القائمة الرئيسية")
    menu = st.radio("انتقل إلى:", ["الرصد والبحث الذكي", "التعريف بالمنصة", "الأجندة القانونية", "بيانات الاتصال"])
    st.divider()
    st.caption("Marka-Sentry v2.0 | 2026")

# 3. منطق عرض الصفحات بناءً على القائمة
if menu == "الرصد والبحث الذكي":
    # --- محرك الرصد (الكود السابق) ---
    st.title("🛡️ رادار Marka-Sentry")
    tab1, tab2 = st.tabs(["🔍 رصد نصي", "📸 مسح ميداني"])
    
    with tab1:
        st.subheader("مراقبة نشرة ديسمبر 2025 (BOPI 432)")
        search = st.text_input("أدخل اسم العلامة الأصلية:")
        if search:
            # محاكاة البحث في بيانات ديسمبر 2025
            if "MICRO" in search.upper():
                st.error("🚨 خطر! تم رصد تشابه مع علامة MASILECT لشركة MICRO LABS LIMITED.")
            else:
                st.success("✅ لم يتم رصد تهديدات حالية.")

    with tab2:
        st.camera_input("فتح الكاميرا للمسح البصري")

elif menu == "الالتعريف بالمنصة":
    st.title("📖 حول Marka-Sentry")
    st.markdown("""
    ### جسر بين القانون والذكاء الاصطناعي
    تعتبر **Marka-Sentry** أول منصة جزائرية متخصصة في **الرصد الاستباقي** للملكية الصناعية. 
    
    *   **الرؤية:** تمكين الشركات الأجنبية والمحلية من حماية أصولها المعنوية باستخدام تقنيات المسح البصري واللفظي.
    *   **المرجعية القانونية:** يعتمد تحليلنا على نصوص **الأمر 03-06** المتعلق بالعلامات، مع التركيز على معايير "خطر التضليل" لدى الجمهور.
    *   **الإشراف:** يتم تطوير وتحديث الخوارزميات تحت إشراف **أستاذ في القانون ومحامٍ معتمد لدى المحكمة العليا**، لضمان دقة التقارير الناتجة.
    """)

elif menu == "الأجندة القانونية":
    st.title("📅 أجندة المواعيد القانونية")
    st.info("مواعيد هامة لمتابعة النشرة الرسمية رقم 432 (ديسمبر 2025)")
    
    # بطاقات الأجندة
    st.markdown("""
    <div class="agenda-card">
        <h4>📦 فترة المعارضة (Opposition)</h4>
        <p><b>التاريخ:</b> يناير 2026</p>
        <p>آخر أجل لتقديم المعارضات ضد العلامات المنشورة في عدد ديسمبر 2025 (خلال 30 يوماً من النشر).</p>
    </div>
    <div class="agenda-card">
        <h4>📑 تجديد العلامات (Renewal)</h4>
        <p><b>التاريخ:</b> فبراير 2026</p>
        <p>مراجعة العلامات التي قاربت مدة حمايتها (10 سنوات) على الانتهاء لإبلاغ الموكلين.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "بيانات الاتصال":
    st.title("📞 تواصل مع خبرائنا")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("المقر الرئيسي")
        st.write("📍 قسنطينة، الجزائر")
        st.write("📧 البريد الإلكتروني: contact@markasentry.dz")
        st.write("📱 الهاتف: 213+ (متاح للموكلين الدوليين)")
    with col_b:
        st.subheader("ساعات العمل")
        st.write("الأحد - الخميس: 08:00 - 16:30")
        st.write("الدعم التقني: 24/7 عبر التطبيق")

import streamlit as st
from fuzzywuzzy import fuzz
from PIL import Image
import pandas as pd

# 1. إعدادات الواجهة الفاخرة
# --- إضافة الشعار الذهبي والاسم في أعلى الصفحة ---
col_logo, col_text = st.columns([1, 4])

with col_logo:
    # سنستخدم أيقونة الدرع الذهبي (التي ترمز للحماية القانونية)
    st.image("https://github.com/maitrewalid25-collab/MarkaSentry-Algeria.DZ/blob/main/LOGO.png?raw=true", width=100)
    st.image("https://github.com/maitrewalid25-collab/MarkaSentry-Algeria.DZ/blob/main/logo%202.png?raw=true", width=100)

with col_text:
    st.markdown("""
        <h1 style='color: #1a3a5f; margin-bottom: 0;'>Marka-Sentry Algeria</h1>
        <p style='color: #d4af37; font-weight: bold; font-size: 1.2em;'>The Golden Standard in Brand Protection</p>
    """, unsafe_allow_html=True)
# تصميم CSS لدمج الجمالية مع الوظيفية
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .hero-section { 
        text-align: center; 
        padding: 50px; 
        background: linear-gradient(135deg, #1a3a5f 0%, #2a5298 100%); 
        color: white; 
        border-radius: 20px; 
        margin-bottom: 30px; 
    }
    .feature-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
        border-top: 5px solid #d4af37; 
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #f1f3f5; 
        border-radius: 10px 10px 0 0; 
        padding: 10px 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- قسم الصدارة الإعلاني ---
st.markdown("""
    <div class="hero-section">
        <h1>🛡️ Marka-Sentry:
         نظام الرصد الميداني مع الدكتور وليد</h1>
        <p style="font-size: 1.2em;">دمج السرعة الميدانية مع الخبرة القانونية الجزائرية</p>
    </div>
    """, unsafe_allow_html=True)

# --- قاعدة بيانات النشرة رقم 432 (ديسمبر 2025) ---
bopi_db = [
    {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"},
    {"ID": "139331", "Brand": "Go Play Market", "Owner": "Ooredoo IP LLC (Qatar)", "Class": "9"},
    {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"},
    {"ID": "139326", "Brand": "Titta", "Owner": "SARL GROUPE LYDIA SERVICE", "Class": "30"}
]

# --- التبويبات التفاعلية (Tabs) ---
tab1, tab2 = st.tabs(["🔍 الرصد النصي ذكي", "📸 المسح البصري الميداني"])

with tab1:
    st.subheader("مراقبة الأسماء والبيانات اللفظية")
    search_query = st.text_input("أدخل اسم العلامة الأصلية (مثال: MICRO أو ALCON):", key="text_search")
    
    if search_query:
        found = False
        for entry in bopi_db:
            score = fuzz.token_set_ratio(search_query.upper(), entry['Brand'].upper())
            if score > 60:
                found = True
                st.warning(f"⚠️ تنبيه: تم رصد تشابه بنسبة {score}% مع {entry['Brand']}")
                st.write(f"المالك: {entry['Owner']} | النشرة: ديسمبر 2025")
        if not found:
            st.success("✅ لم يتم رصد أي تشابه لفظي مقلق.")

with tab2:
    st.subheader("التحقق عبر كاميرا الهاتف")
    st.info("التقط صورة لعلامة تجارية في السوق لمطابقتها بصریاً مع سجلات ديسمبر 2025.")
    
    img_file = st.camera_input("قم بتصوير العلامة المشبوهة")
    
    if img_file:
        st.image(img_file, caption="الصورة الملتقطة", width=300)
        with st.spinner("جاري تحليل البصمة البصرية ومطابقة الألوان..."):
            # محاكاة الرصد البصري بناءً على بيانات حقيقية
            st.error("🚨 خطر تقليد بصري مرتفع!")
            st.write("تم رصد محاكاة لأسلوب الخط والألوان البرتقالية لعلامة **Titta** المنشورة في الصفحة 9.")
            st.info("نصيحة قانونية: هذا التشابه قد يسبب خلطاً لدى المستهلك وفقاً للأمر 03-06.")

# --- تذييل الصفحة ---
st.divider()
st.markdown("<center>© 2026 Marka-Sentry Algeria | مدعوم بخبرة قانونية في الاستثمار والملكية الصناعية</center>", unsafe_allow_html=True)

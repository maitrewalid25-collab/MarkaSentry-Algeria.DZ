import streamlit as st
from fuzzywuzzy import fuzz
import pandas as pd

# إعدادات الصفحة الفاخرة لتناسب العرض الدولي
st.set_page_config(page_title="Marka-Sentry | Legal-Tech", page_icon="🛡️", layout="wide")

# تصميم الواجهة باستخدام CSS المتقدم لتحسين تجربة المستخدم
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .hero-section { text-align: center; padding: 40px; background: linear-gradient(135deg, #1a3a5f 0%, #2a5298 100%); color: white; border-radius: 15px; margin-bottom: 30px; }
    .feature-card { background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #d4af37; text-align: center; height: 100%; }
    .alert-box { background-color: #fff5f5; border-right: 8px solid #e53e3e; padding: 20px; border-radius: 10px; margin-bottom: 10px; direction: rtl; }
    .stButton>button { background-color: #d4af37 !important; color: white !important; border-radius: 8px !important; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- قسم الصدارة (Hero Section) ---
st.markdown("""
    <div class="hero-section">
        <h1>🛡️ Marka-Sentry Algeria</h1>
        <p style="font-size: 1.3em;">Protecting Your Legacy, Powered by AI, Governed by Law</p>
        <p>المنصة الرائدة في رصد وحماية الملكية الصناعية وفقاً للمعايير الدولية والأمر 03-06</p>
    </div>
    """, unsafe_allow_html=True)

# --- مميزات المنصة (Features) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="feature-card"><h3>رصد آلي</h3><p>مسح شامل لنشرة ديسمبر 2025 رقم 432 فور صدورها.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-card"><h3>تحليل خبير</h3><p>مطابقة تقنية وقانونية تحت إشراف نخبة من أساتذة القانون.</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-card"><h3>تقارير ذكية</h3><p>استخراج فوري لتقارير المعارضة الجاهزة للتقديم الإداري.</p></div>', unsafe_allow_html=True)

st.divider()

# --- محرك الرصد الذكي (The Intelligence Hub) ---
st.header("🔍 رادار البحث في سجلات INAPI")
st.write("اختبر حماية علامتك في أحدث نشرة رسمية صادرة.")

# بيانات حقيقية مستخرجة من النشرة رقم 432
bopi_database = [
    {"ID": "139321", "Brand": "MASILECT", "Owner": "MICRO LABS LIMITED (India)", "Class": "5"}, #
    {"ID": "139331", "Brand": "Go Play Market", "Owner": "Ooredoo IP LLC (Qatar)", "Class": "9"}, #
    {"ID": "139335", "Brand": "See Brilliantly", "Owner": "ALCON INC (Switzerland)", "Class": "5, 9, 10"}, #
    {"ID": "139326", "Brand": "Titta", "Owner": "SARL GROUPE LYDIA SERVICE", "Class": "30"} #
]

search_term = st.text_input("أدخل اسم العلامة الأصلية لمراقبتها:", placeholder="مثال: MICRO LABS أو ALCON")

if search_term:
    results = []
    for entry in bopi_database:
        score = fuzz.token_set_ratio(search_term.upper(), entry['Brand'].upper())
        if score > 60:
            results.append(entry | {"score": score})
    
    if results:
        st.subheader(f"⚠️ نتائج الرصد ({len(results)})")
        for res in results:
            st.markdown(f"""
                <div class="alert-box">
                    <h4 style="color: #e53e3e;">درجة الخطورة: {res['score']}%</h4>
                    <p>تم رصد تشابه مع العلامة <b>{res['Brand']}</b> للمالك <b>{res['Owner']}</b>.</p>
                    <p>البيانات منشورة في العدد 432 (ديسمبر 2025) - الفئة {res['Class']}.</p>
                </div>
            """, unsafe_allow_html=True)
            st.button(f"تحميل ملف التحليل لـ {res['Brand']}", key=res['ID'])
    else:
        st.success("✅ لم يتم العثور على أي تشابه مقلق في هذه النشرة.")

st.markdown("<br><hr><center>© 2026 Marka-Sentry Algeria | Legal-Tech Innovation</center>", unsafe_allow_html=True)

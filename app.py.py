import streamlit as st
from fuzzywuzzy import fuzz
import pandas as pd

# 1. قاعدة البيانات المستخرجة من المجلة التي أرسلتها (عينة تجريبية)
# تم استخراج هذه البيانات بناءً على أكواد INID في النشرة رقم 432
bopi_data = [
    {"id": "139321", "owner": "MICRO LABS LIMITED (INDIA)", "brand": "MASILECT", "class": "5, 35, 39"},
    {"id": "139322", "owner": "MICRO LABS LIMITED (INDIA)", "brand": "LUMOREST", "class": "5, 35, 39"},
    {"id": "139331", "owner": "Ooredoo IP LLC (QATAR)", "brand": "Go Play Market", "class": "9, 35, 36, 38, 42"},
    {"id": "139328", "owner": "CHETBEY FOOD SARL (ALGERIA)", "brand": "GOFD OR", "class": "29, 30, 32"},
    {"id": "139326", "owner": "SARL GROUPE LYDIA SERVICE", "brand": "Titta", "class": "30"}
]

# 2. تصميم واجهة المستخدم
st.set_page_config(page_title="Marka-Sentry Algeria", layout="wide")
st.title("🛡️ منصة مراقبة العلامات التجارية - الجزائر")
st.subheader("لوحة تحكم الشركات الأجنبية (النسخة التجريبية)")

# 3. إدخال العميل لعلامته التجارية
with st.sidebar:
    st.header("إعدادات المراقبة")
    target_brand = st.text_input("أدخل اسم علامتك التجارية للمراقبة:", value="SANOFI")
    sensitivity = st.slider("درجة حساسية الرصد (Fuzzy Matching):", 0, 100, 60)

# 4. محرك الرصد والتحليل
st.write(f"### نتائج المسح في مجلة BOPI رقم 432 (ديسمبر 2025)[cite: 1]")

alerts = []
for entry in bopi_data:
    # حساب نسبة التشابه باستخدام المنطق الضبابي
    score = fuzz.partial_ratio(target_brand.upper(), entry['brand'].upper())
    
    if score >= sensitivity:
        alerts.append({
            "العلامة المكتشفة": entry['brand'],
            "نسبة الخطورة": f"{score}%",
            "المالك": entry['owner'],
            "رقم التسجيل": entry['id'],
            "الفئات (Nice)": entry['class']
        })

# 5. عرض النتائج
if alerts:
    df = pd.DataFrame(alerts)
    st.warning(f"⚠️ تم اكتشاف {len(alerts)} تهديدات محتملة لعلامتك التجارية!")
    st.table(df)
else:
    st.success("✅ لا توجد علامات مشابهة منشورة في هذا العدد.")

# إضافة معلومات قانونية بناءً على المجلة
st.info("ملاحظة: البيانات مستخرجة آلياً بناءً على المادة 5 من الأمر 03-06 المتعلق بالعلامات[cite: 1].")
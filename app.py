import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Truth Detective AI", page_icon="🕵️")

# ستايل احترافي
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🕵️ TRUTH DETECTIVE AI</h1>", unsafe_allow_html=True)

# جلب المفتاح من Vercel
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    uploaded_file = st.file_uploader("ارفع الصورة أو الفيديو للفحص...", type=['png', 'jpg', 'jpeg', 'mp4'])
    
    if uploaded_file and st.button("إبدأ الفحص الملكي 🔥"):
        with st.spinner('يتم الآن التحليل بعقل الذكاء الاصطناعي...'):
            try:
                # معالجة الملف
                img = uploaded_file.read()
                response = model.generate_content(["حلل هذا الملف بدقة وأخبرني هل هو حقيقي أم مزيف وماذا يوجد فيه؟", {"mime_type": uploaded_file.type, "data": img}])
                st.success("تم التحليل بنجاح!")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
else:
    st.warning("الرجاء إضافة مفتاح GEMINI_API_KEY في إعدادات Vercel")

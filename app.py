import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد واجهة التطبيق
st.set_page_config(page_title="لوحة المبيعات", layout="wide")
st.title("📊 أداء الفروع اليومي")

try:
    # محاولة قراءة ملف البيانات الذي سنرفعه في الخطوة القادمة
    df = pd.read_csv('data.csv')
    
    # عرض ملخص سريع
    col1, col2 = st.columns(2)
    col1.metric("إجمالي المبيعات", f"{df.iloc[:, 1].sum():.2f} جرام")
    col2.metric("عدد الفروع", len(df))

    # رسم بياني للمقارنة
    fig = px.bar(df, x=df.columns[0], y=[df.columns[1], df.columns[2]], 
                 title="المبيعات الفعلية مقابل الهدف", barmode='group')
    st.plotly_chart(fig, use_container_width=True)

except Exception:
    st.warning("بانتظار رفع ملف البيانات (data.csv)...")

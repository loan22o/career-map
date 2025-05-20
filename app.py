import streamlit as st
import pandas as pd
import plotly.express as px
from mbti import mbti_quiz, suggest_career

@st.cache_data
def load_data():
    df = pd.read_csv("data/Cleaned data.csv")
    df = df.dropna(subset=['Industry', 'Location.1', 'Min Salary', 'Max Salary'])
    return df

df = load_data()

st.set_page_config(page_title="CareerMap", layout="wide")
st.title("🎯 CareerMap – Nền tảng hướng nghiệp cá nhân hóa")

st.header("🧠 Trắc nghiệm MBTI đơn giản")
mbti_type = mbti_quiz()

st.header("🛠️ Kỹ năng và ngành học")
skills = st.multiselect("Bạn có những kỹ năng nào?", ["Phân tích dữ liệu", "Lập trình", "Giao tiếp", "Thiết kế", "Quản lý dự án"])
major = st.selectbox("Ngành bạn đang học là gì?", ["Kinh tế", "Công nghệ thông tin", "Truyền thông", "Kỹ thuật", "Du lịch"])

if mbti_type and st.button("🎯 Xem gợi ý nghề nghiệp"):
    suggestions = suggest_career(mbti_type, skills, major)
    st.subheader("🔍 Nghề nghiệp phù hợp với bạn:")
    for job in suggestions:
        st.markdown(f"- {job}")

st.header("📊 Phân tích xu hướng thị trường")

col1, col2 = st.columns(2)

with col1:
    avg_salary_industry = df.groupby("Industry")["Min Salary"].mean().reset_index()
    fig1 = px.bar(avg_salary_industry, x="Industry", y="Min Salary", title="💼 Lương trung bình theo ngành")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    avg_salary_location = df.groupby("Location.1")["Min Salary"].mean().reset_index()
    fig2 = px.bar(avg_salary_location, x="Location.1", y="Min Salary", title="🌍 Lương theo địa điểm")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Lương trung bình theo kinh nghiệm")
df["EXP"] = df["EXP"].astype(int)
avg_exp = df.groupby("EXP")["Min Salary"].mean().reset_index()
fig3 = px.line(avg_exp, x="EXP", y="Min Salary", markers=True, title="📈 Lương theo số năm kinh nghiệm")
st.plotly_chart(fig3, use_container_width=True)

st.caption("Nguồn dữ liệu: TopCV, VietnamWorks – xử lý bởi nhóm CareerMap")

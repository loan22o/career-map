import streamlit as st

questions = {
    "Bạn thích làm việc một mình hơn làm nhóm?": "I/E",
    "Bạn dựa vào cảm xúc nhiều hơn lý trí khi quyết định?": "T/F",
    "Bạn thường lên kế hoạch trước thay vì linh hoạt thích ứng?": "J/P",
    "Bạn thích sự thật hơn là ý tưởng sáng tạo?": "S/N"
}

def mbti_quiz():
    result = {"I": 0, "E": 0, "T": 0, "F": 0, "J": 0, "P": 0, "S": 0, "N": 0}
    for q, dim in questions.items():
        ans = st.radio(q, ["Đúng", "Sai"], key=q)
        if dim == "I/E":
            result["I" if ans == "Đúng" else "E"] += 1
        elif dim == "T/F":
            result["F" if ans == "Đúng" else "T"] += 1
        elif dim == "J/P":
            result["J" if ans == "Đúng" else "P"] += 1
        elif dim == "S/N":
            result["S" if ans == "Đúng" else "N"] += 1

    if st.button("Xem kết quả MBTI"):
        return summarize_mbti(result)
    return None

def summarize_mbti(res):
    return (
        ("I" if res["I"] >= res["E"] else "E") +
        ("S" if res["S"] >= res["N"] else "N") +
        ("T" if res["T"] >= res["F"] else "F") +
        ("J" if res["J"] >= res["P"] else "P")
    )

def suggest_career(mbti, skills, major):
    careers = []
    if "Phân tích dữ liệu" in skills:
        careers.append("Data Analyst")
    if "Lập trình" in skills:
        careers.append("Web Developer")
    if "Giao tiếp" in skills:
        careers.append("Chuyên viên tư vấn")
    if "Thiết kế" in skills:
        careers.append("Graphic Designer")
    if "Quản lý dự án" in skills:
        careers.append("Project Manager")

    if not careers:
        if mbti.startswith("I"):
            careers.append("Kế toán")
        else:
            careers.append("Marketing")
    return careers

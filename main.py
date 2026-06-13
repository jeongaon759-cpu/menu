import streamlit as st

st.set_page_config(
    page_title="지금 뭐 먹지?",
    page_icon="🍽️",
    layout="centered"
)

# ----------------------------
# 음식 데이터 (속성 기반)
# ----------------------------

foods = [
    {"name":"짜장면","type":"면","hot":True,"meat":False,"soup":False},
    {"name":"짬뽕","type":"면","hot":True,"meat":True,"soup":True},
    {"name":"돈까스","type":"밥","hot":True,"meat":True,"soup":False},
    {"name":"초밥","type":"밥","hot":False,"meat":False,"soup":False},
    {"name":"김밥","type":"밥","hot":False,"meat":False,"soup":False},
    {"name":"떡볶이","type":"분식","hot":True,"meat":False,"soup":False},
    {"name":"냉면","type":"면","hot":False,"meat":False,"soup":True},
    {"name":"비빔밥","type":"밥","hot":True,"meat":False,"soup":False},
    {"name":"삼겹살","type":"고기","hot":True,"meat":True,"soup":False},
    {"name":"갈비탕","type":"국","hot":True,"meat":True,"soup":True},
]

# ----------------------------
# 상태
# ----------------------------

if "start" not in st.session_state:
    st.session_state.start = False

# ----------------------------
# 시작 화면
# ----------------------------

if not st.session_state.start:

    st.markdown(
        "<h1 style='text-align:center;'>🍕🍜🍔🍣🍙</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;'>지금 뭐 먹지?</h2>",
        unsafe_allow_html=True
    )

    if st.button("시작하기 🍽️", use_container_width=True):
        st.session_state.start = True
        st.rerun()

# ----------------------------
# 질문 화면
# ----------------------------

else:

    st.title("🍽️ 음식 추천 테스트")

    q1 = st.radio("1. 지금 시간대?", ["아침","점심","저녁","야식"])
    q2 = st.slider("2. 배고픔 (1~10)", 1, 10, 5)
    q3 = st.radio("3. 원하는 종류", ["밥","면","고기","분식","상관없음"])
    q4 = st.radio("4. 뜨거운 음식?", ["예","아니오","상관없음"])
    q5 = st.radio("5. 국물?", ["필수","상관없음","싫음"])

    if st.button("🍀 추천 받기", use_container_width=True):

        results = []

        for food in foods:

            score = 0

            # 종류
            if q3 != "상관없음" and food["type"] == q3:
                score += 3

            # 뜨거운 음식
            if q4 == "예" and food["hot"]:
                score += 2
            if q4 == "아니오" and not food["hot"]:
                score += 2

            # 국물
            if q5 == "필수" and food["soup"]:
                score += 3
            if q5 == "싫음" and not food["soup"]:
                score += 2

            # 배고픔 보정
            if q2 >= 8 and food["meat"]:
                score += 2

            results.append((food["name"], score))

        # 점수 정렬
        results.sort(key=lambda x: x[1], reverse=True)

        top = results[:5]

        st.balloons()

        st.success("추천 완료!")

        st.markdown("## 🍽️ 추천 결과")

        for name, score in top:
            st.write(f"🍴 {name} (점수: {score})")

        st.markdown("---")

        if st.button("다시 하기"):
            st.session_state.start = False
            st.rerun()

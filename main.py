
import streamlit as st

st.set_page_config(
    page_title="지금 뭐 먹지?",
    page_icon="🍽️",
    layout="centered"
)

# -------------------------
# 상태
# -------------------------

if "start" not in st.session_state:
    st.session_state.start = False

# -------------------------
# 음식 데이터 (50개)
# -------------------------

foods = [
    {"name":"짜장면","type":["면","중식"],"hot":True,"soup":False,"meat":False,"spicy":0},
    {"name":"짬뽕","type":["면","중식","국물"],"hot":True,"soup":True,"meat":True,"spicy":4},
    {"name":"탕수육","type":["중식","튀김"],"hot":True,"soup":False,"meat":True,"spicy":0},
    {"name":"초밥","type":["밥","일식","차가움"],"hot":False,"soup":False,"meat":False,"spicy":0},
    {"name":"회덮밥","type":["밥","해산물","차가움"],"hot":False,"soup":False,"meat":False,"spicy":1},
    {"name":"돈까스","type":["밥","양식"],"hot":True,"soup":False,"meat":True,"spicy":0},
    {"name":"김밥","type":["밥","분식"],"hot":False,"soup":False,"meat":False,"spicy":0},
    {"name":"떡볶이","type":["분식","매움"],"hot":True,"soup":False,"meat":False,"spicy":5},
    {"name":"냉면","type":["면","차가움"],"hot":False,"soup":True,"meat":False,"spicy":0},
    {"name":"비빔밥","type":["밥"],"hot":True,"soup":False,"meat":False,"spicy":2},

    {"name":"삼겹살","type":["고기"],"hot":True,"soup":False,"meat":True,"spicy":0},
    {"name":"갈비찜","type":["고기"],"hot":True,"soup":True,"meat":True,"spicy":1},
    {"name":"곰탕","type":["국물"],"hot":True,"soup":True,"meat":True,"spicy":0},
    {"name":"설렁탕","type":["국물"],"hot":True,"soup":True,"meat":True,"spicy":0},
    {"name":"순두부찌개","type":["국물","매움"],"hot":True,"soup":True,"meat":False,"spicy":3},

    {"name":"쌀국수","type":["면","국물"],"hot":True,"soup":True,"meat":True,"spicy":1},
    {"name":"우동","type":["면","국물"],"hot":True,"soup":True,"meat":False,"spicy":0},
    {"name":"라면","type":["면","국물","매움"],"hot":True,"soup":True,"meat":False,"spicy":3},
    {"name":"볶음우동","type":["면"],"hot":True,"soup":False,"meat":True,"spicy":1},

    {"name":"비빔국수","type":["면"],"hot":False,"soup":False,"meat":False,"spicy":3},
    {"name":"쫄면","type":["면","매움"],"hot":False,"soup":False,"meat":False,"spicy":4},

    {"name":"육개장","type":["국물","매움"],"hot":True,"soup":True,"meat":True,"spicy":4},
    {"name":"갈비탕","type":["국물"],"hot":True,"soup":True,"meat":True,"spicy":0},

    {"name":"치킨","type":["고기","튀김"],"hot":True,"soup":False,"meat":True,"spicy":1},
    {"name":"치맥","type":["고기","튀김"],"hot":True,"soup":False,"meat":True,"spicy":2},

    {"name":"피자","type":["양식"],"hot":True,"soup":False,"meat":True,"spicy":0},
    {"name":"햄버거","type":["양식"],"hot":True,"soup":False,"meat":True,"spicy":0},

    {"name":"파스타","type":["양식"],"hot":True,"soup":False,"meat":True,"spicy":1},
    {"name":"스테이크","type":["고기","양식"],"hot":True,"soup":False,"meat":True,"spicy":0},

    {"name":"부대찌개","type":["국물","고기","매움"],"hot":True,"soup":True,"meat":True,"spicy":4},
    {"name":"김치찌개","type":["국물","매움"],"hot":True,"soup":True,"meat":True,"spicy":4},

    {"name":"회","type":["해산물"],"hot":False,"soup":False,"meat":False,"spicy":0},
    {"name":"물회","type":["해산물","차가움"],"hot":False,"soup":True,"meat":False,"spicy":2},

    {"name":"족발","type":["고기"],"hot":True,"soup":False,"meat":True,"spicy":1},
    {"name":"보쌈","type":["고기"],"hot":True,"soup":False,"meat":True,"spicy":0},

    {"name":"덮밥","type":["밥"],"hot":True,"soup":False,"meat":True,"spicy":1},
    {"name":"볶음밥","type":["밥"],"hot":True,"soup":False,"meat":True,"spicy":1},

    {"name":"죽","type":["밥","가벼움"],"hot":True,"soup":True,"meat":False,"spicy":0},

    {"name":"떡국","type":["국물","떡"],"hot":True,"soup":True,"meat":True,"spicy":0},

    {"name":"마라탕","type":["국물","매움"],"hot":True,"soup":True,"meat":True,"spicy":5},

    {"name":"마라샹궈","type":["매움"],"hot":True,"soup":False,"meat":True,"spicy":5}
]

# -------------------------
# 시작 화면
# -------------------------

if not st.session_state.start:

    st.markdown("<h1 style='text-align:center;'>🍕🍜🍱🍣🍔</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>지금 뭐 먹지?</h2>", unsafe_allow_html=True)

    if st.button("시작하기", use_container_width=True, type="primary"):
        st.session_state.start = True
        st.rerun()

# -------------------------
# 질문 화면
# -------------------------

else:

    st.title("🍽️ 음식 추천")

    q1 = st.radio("시간대", ["아침","점심","저녁","야식"])
    q2 = st.slider("배고픔", 1, 10, 5)
    q3 = st.radio("종류", ["밥","면","고기","국물","상관없음"])
    q4 = st.radio("온도", ["뜨거운","차가운","상관없음"])
    q5 = st.radio("국물 필요?", ["필수","상관없음","싫음"])

    if st.button("🍀 추천 받기", use_container_width=True):

        best_food = None
        best_score = -1

        for food in foods:

            score = 0

            # 종류
            if q3 != "상관없음" and q3 in food["type"]:
                score += 3

            # 온도
            if q4 == "뜨거운" and food["hot"]:
                score += 2
            if q4 == "차가운" and not food["hot"]:
                score += 2

            # 국물
            if q5 == "필수" and food["soup"]:
                score += 3
            if q5 == "싫음" and not food["soup"]:
                score += 2

            # 배고픔
            if q2 >= 8 and food["meat"]:
                score += 2

            if score > best_score:
                best_score = score
                best_food = food["name"]

        st.balloons()

        st.success("추천 완료!")

        st.markdown("## 🍽️ 오늘의 추천 메뉴")
        st.markdown(f"# {best_food}")

        st.write(f"점수: {best_score}")

        st.markdown("---")

        if st.button("다시 하기"):
            st.session_state.start = False
            st.rerun()

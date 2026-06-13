import streamlit as st
import random

st.set_page_config(
    page_title="지금 뭐먹고싶니?",
    page_icon="🍜",
    layout="centered"
)

# -------------------
# 상태 관리
# -------------------

if "started" not in st.session_state:
    st.session_state.started = False

# -------------------
# 음식 데이터
# -------------------

foods = [
    "간장게장","족발","수육","잔치국수","탕수육","물냉면","비빔냉면",
    "차돌된장찌개","짜장면","월남쌈","짬뽕","잡탕밥","돼지갈비","소갈비",
    "참치김치찌개","보리밥","육개장","팔보채","벌집삼겹살","평양냉면",
    "알밥","대패삼겹살","초밥","오징어버터구이","연탄불고기",
    "회덮밥","깐풍기","미역국","물회","콩나물국밥","오징어회",
    "참치회","고등어구이","크림카레우동","갈비찜","치맥",
    "돈까스","숯불닭갈비","소고기무국","곰탕","갈비탕",
    "케밥","비빔국수","참치비빔밥","수제비","파전",
    "양념게장","팟타이","떡볶이","뼈해장국","가리비구이",
    "비지찌개","간장새우","김밥","생새우초밥","남산왕돈까스",
    "김치만두","군만두","물만두","쫄면","순대",
    "곱창","대창","막창","LA갈비","깐쇼새우",
    "유산슬","돼지국밥","새우죽","고추장찌개","엽떡",
    "회냉면","생선까스","안동찜닭","까르보나라떡볶이","설렁탕",
    "육회비빔밥","어묵꼬치","열무비빔밥","광어회","고추잡채",
    "닭도리탕","양념갈비","한우스테이크","돌솥비빔밥",
    "돼지갈비찜","명란스파게티","후쿠오카함바그","떡갈비",
    "양꼬치","짬뽕밥","볶음우동","닭강정","치즈돈까스정식",
    "쟁반짜장","삼계탕","카레우동","순두부찌개","국물닭발",
    "해물순두부","규동","쌀국수","볶음밥","김치전",
    "소갈비찜","동그랑땡","우삼겹","스테키동","주먹김밥"
]

# -------------------
# 시작 화면
# -------------------

if not st.session_state.started:

    st.markdown(
        "<h1 style='text-align:center;'>🍕🍔🍜🍣🍗🍱🍙</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center;'>지금 뭐먹고싶니?</h1>",
        unsafe_allow_html=True
    )

    if st.button("시작하기", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()

# -------------------
# 질문 화면
# -------------------

else:

    st.title("🍽️ 음식 취향 검사")

    q1 = st.radio("1. 현재 시간대", ["아침","점심","저녁","야식"])
    q2 = st.slider("2. 배고픔 (1~10)", 1, 10, 5)
    q3 = st.radio("3. 원하는 종류", ["밥","면","빵","상관없음"])
    q4 = st.radio("4. 온도", ["뜨거운","차가운","상관없음"])
    q5 = st.radio("5. 맛", ["매운","단","짭짤","상관없음"])
    q6 = st.radio("6. 국물", ["무조건","있으면 좋음","필요없음"])
    q7 = st.radio("7. 고기", ["무조건","있으면 좋음","싫음"])
    q8 = st.radio("8. 예산", ["5000원 이하","10000원 이하","20000원 이하","상관없음"])
    q9 = st.radio("9. 기분", ["가볍게","적당히","든든하게","특별하게"])
    q10 = st.radio("10. 새로운 음식", ["좋다","보통","익숙한게 좋다"])
    q11 = st.multiselect("11. 싫은 음식", ["해산물","고기","면","매운","없음"])

    if st.button("🍀 결과 보기", use_container_width=True):

        candidates = foods.copy()

        # -------------------
        # 필터
        # -------------------

        if "해산물" in q11:
            sea = ["간장게장","새우","회","물회","가리비구이","광어회","참치회"]
            candidates = [x for x in candidates if x not in sea]

        if "고기" in q11:
            meat = ["족발","수육","삼겹살","갈비","불고기","곱창","막창","대창"]
            candidates = [x for x in candidates if x not in meat]

        if "면" in q11:
            noodle = ["짜장면","짬뽕","냉면","쌀국수","우동","비빔국수","라면"]
            candidates = [x for x in candidates if x not in noodle]

        if "매운" in q11:
            spicy = ["떡볶이","엽떡","짬뽕","닭도리탕","닭갈비"]
            candidates = [x for x in candidates if x not in spicy]

        # -------------------
        # 가중치
        # -------------------

        if q2 >= 8:
            candidates += ["족발","삼겹살","갈비찜","곰탕"] * 3

        elif q2 <= 3:
            candidates += ["냉면","연두부","김밥","잔치국수"] * 2

        if q3 == "면":
            candidates += ["짜장면","짬뽕","쌀국수","우동"] * 3

        if q3 == "밥":
            candidates += ["볶음밥","비빔밥","덮밥","김밥"] * 3

        # -------------------
        # 결과
        # -------------------

        if candidates:

            result = random.choice(candidates)

            st.balloons()

            st.markdown("## 🎉 추천 결과")
            st.markdown(f"# 🍽️ {result}")

            st.success("추천 완료!")

            st.write("")
            st.write("아직도 마음에 안드시나요?")

            if st.button("다시 검사하기"):
                st.session_state.started = False
                st.rerun()

        else:
            st.error("조건에 맞는 음식이 없습니다 😢")

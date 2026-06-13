    import streamlit as st
    import random
    
    st.set_page_config(
        page_title="지금 뭐먹고싶니?",
        page_icon="🍜",
        layout="centered"
    )
    
    # -------------------
    # 세션 상태
    # -------------------
    
    if "started" not in st.session_state:
        st.session_state.started = False
    
    if "result" not in st.session_state:
        st.session_state.result = None
    
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
            """
            <div style='text-align:center;font-size:38px;'>
            🍕🍔🍟🌭🍗🍖🍜🍝🍣🍤🍙🥟🍛🍰🍩🍦
            </div>
            """,
            unsafe_allow_html=True
        )
    
        st.markdown("<h1 style='text-align:center;'>지금 뭐먹고싶니?</h1>",
                    unsafe_allow_html=True)
    
        st.write("")
        st.write("")
    
        if st.button("시작하기", use_container_width=True, type="primary"):
            st.session_state.started = True
            st.rerun()
    
    # -------------------
    # 질문 화면
    # -------------------
    
    else:
    
        st.title("🍽️ 음식 취향 검사")
    
        q1 = st.radio(
            "1. 지금 현재 시각은?",
            ["아침", "점심", "저녁", "새벽"]
        )
    
        q2 = st.slider(
            "2. 배고픔 정도",
            1, 10, 5
        )
    
        q3 = st.radio(
            "3. 어떤 종류가 땡기나요?",
            ["밥", "면", "빵", "상관없음"]
        )
    
        q4 = st.radio(
            "4. 음식 온도는?",
            ["뜨거운 음식", "차가운 음식", "상관없음"]
        )
    
        q5 = st.radio(
            "5. 원하는 맛은?",
            ["매운맛", "달콤한 맛", "짭짤한 맛", "새콤한 맛", "상관없음"]
        )
    
        q6 = st.radio(
            "6. 국물은?",
            ["무조건", "있으면 좋음", "필요 없음"]
        )
          q7 = st.radio(
            "7. 고기 메뉴는?",
            ["무조건 고기", "있으면 좋음", "고기 말고"]
        )
    
        q8 = st.radio(
            "8. 예산은?",
            ["5000원 이하", "10000원 이하", "20000원 이하", "상관없음"]
        )
    
        q9 = st.radio(
            "9. 오늘 기분은?",
            [
                "가볍게 먹고 싶다",
                "적당히 먹고 싶다",
                "든든하게 먹고 싶다",
                "특별한 음식 먹고 싶다"
            ]
        )
    
        q10 = st.radio(
            "10. 새로운 음식 도전?",
            [
                "새로운 메뉴도 좋다",
                "적당히",
                "익숙한 메뉴가 좋다"
            ]
        )
    
        q11 = st.multiselect(
            "11. 오늘 먹기 싫은 것은?",
            [
                "해산물",
                "고기",
                "매운 음식",
                "면 요리",
                "국물 음식",
                "없음"
            ]
        )
    
        st.divider()
    
        if st.button("🍀 결과 보기", use_container_width=True):
    
            candidates = foods.copy()
    
            # -----------------
            # 불호 필터
            # -----------------
    
            seafood_foods = [
                "간장게장","양념게장","간장새우","물회",
                "광어회","참치회","오징어회",
                "생새우초밥","가리비구이","회덮밥",
                "연어알","관자"
            ]
    
            meat_foods = [
                "족발","수육","돼지갈비","소갈비",
                "벌집삼겹살","대패삼겹살",
                "연탄불고기","갈비찜","숯불닭갈비",
                "곱창","대창","막창","LA갈비",
                "안동찜닭","양념갈비","한우스테이크",
                "돼지갈비찜","떡갈비","양꼬치",
                "우삼겹"
            ]
    
            noodle_foods = [
                "잔치국수","물냉면","비빔냉면",
                "짜장면","짬뽕","크림카레우동",
                "비빔국수","팟타이","쫄면",
                "회냉면","명란스파게티",
                "볶음우동","카레우동","쌀국수"
            ]
    
            soup_foods = [
                "육개장","미역국","콩나물국밥",
                "소고기무국","곰탕","갈비탕",
                "뼈해장국","비지찌개",
                "돼지국밥","고추장찌개",
                "설렁탕","삼계탕",
                "순두부찌개","해물순두부",
                "참치김치찌개","차돌된장찌개"
            ]
    
            spicy_foods = [
                "짬뽕","육개장","떡볶이",
                "엽떡","국물닭발","닭도리탕",
                "양꼬치","고추잡채",
                "까르보나라떡볶이"
            ]
    
            if "해산물" in q11:
                candidates = [
                    x for x in candidates
                    if x not in seafood_foods
                ]
    
            if "고기" in q11:
                candidates = [
                    x for x in candidates
                    if x not in meat_foods
                ]
    
            if "면 요리" in q11:
                candidates = [
                    x for x in candidates
                    if x not in noodle_foods
                ]
    
            if "국물 음식" in q11:
                candidates = [
                    x for x in candidates
                    if x not in soup_foods
                ]
    
            if "매운 음식" in q11:
                candidates = [
                    x for x in candidates
                    if x not in spicy_foods
                ]
    
            # -----------------
            # 배고픔 반영
            # -----------------
    
            if q2 >= 8:
    
                heavy_foods = [
                    "족발","수육","갈비찜",
                    "돼지갈비","소갈비",
                    "삼계탕","설렁탕",
                    "곰탕","갈비탕",
                    "한우스테이크",
                    "양꼬치",
                    "육회비빔밥",
                    "돌솥비빔밥"
                ]
    
                candidates.extend(heavy_foods)
                candidates.extend(heavy_foods)
    
            elif q2 <= 3:
    
                light_foods = [
                    "물냉면","비빔냉면",
                    "연두부","새우죽",
                    "미역국","잔치국수",
                    "콩나물국밥"
                ]
    
                candidates.extend(light_foods)
                candidates.extend(light_foods)
    
            # -----------------
            # 종류 반영
            # -----------------
    
            if q3 == "면":
    
                noodle_bonus = [
                    "잔치국수","물냉면","비빔냉면",
                    "짜장면","짬뽕","쫄면",
                    "팟타이","볶음우동",
                    "카레우동","쌀국수"
                ]
    
                candidates.extend(noodle_bonus * 3)
    
            elif q3 == "밥":
    
                rice_bonus = [
                    "알밥","잡탕밥","돌솥비빔밥",
                    "열무비빔밥","육회비빔밥",
                    "규동","볶음밥",
                    "짬뽕밥","주먹김밥",
                    "김밥"
                ]
    
                candidates.extend(rice_bonus * 3)
                      # -----------------
            # 온도 반영
            # -----------------
    
            if q4 == "뜨거운 음식":
                hot_foods = [
                    "짬뽕","육개장","설렁탕","갈비탕",
                    "삼계탕","순두부찌개","뼈해장국",
                    "김치찌개","차돌된장찌개","수제비",
                    "부대찌개","닭도리탕"
                ]
                candidates.extend(hot_foods * 2)
    
            elif q4 == "차가운 음식":
                cold_foods = [
                    "물냉면","비빔냉면","회덮밥",
                    "물회","연두부","버블티"
                ]
                candidates.extend(cold_foods * 2)
    
            # -----------------
            # 국물 여부
            # -----------------
    
            if q6 == "무조건":
                soup_foods = [
                    "짬뽕","육개장","설렁탕","갈비탕",
                    "순두부찌개","뼈해장국","콩나물국밥",
                    "미역국","곰탕","수제비"
                ]
                candidates.extend(soup_foods * 3)
    
            elif q6 == "필요 없음":
                no_soup = [
                    "돈까스","초밥","족발","수육",
                    "볶음밥","비빔밥","스테키동",
                    "치맥","김밥"
                ]
                candidates.extend(no_soup * 2)
    
            # -----------------
            # 고기 여부
            # -----------------
    
            if q7 == "무조건 고기":
                meat_foods = [
                    "족발","수육","돼지갈비","소갈비",
                    "삼겹살","대패삼겹살","곱창",
                    "막창","막창","한우스테이크",
                    "양꼬치","닭갈비","불고기"
                ]
                candidates.extend(meat_foods * 3)
    
            elif q7 == "고기 말고":
                veg_foods = [
                    "비빔냉면","잔치국수","쌀국수",
                    "비빔밥","김밥","연두부",
                    "쫄면","열무비빔밥"
                ]
                candidates.extend(veg_foods * 2)
    
            # -----------------
            # 결과 선택
            # -----------------
    
            if candidates:
                result = random.choice(candidates)
    
                st.session_state.result = result
    
                st.balloons()
    
                st.markdown("## 🎉 오늘의 추천 메뉴 🎉")
                st.markdown(f"# 🍽️ {result}")
    
                st.success("추천 완료!")
    
                st.write("")
    
                st.markdown("---")
    
                st.write("아직도 마음에 안드시나요?")
    
                if st.button("다시 검사하기"):
                    st.session_state.started = False
                    st.session_state.result = None
                    st.rerun()
    
            else:
                st.error("조건에 맞는 음식이 없어요 😢 다시 선택해주세요")

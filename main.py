import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="PUMP UP! 오늘의 루틴",
    page_icon="💪",
    layout="centered"
)

# 2. 화려한 CSS 스타일링
st.markdown("""
    <style>
    /* 메인 배경 그라데이션 */
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a40 100%);
        color: white;
    }
    
    /* 타이틀 애니메이션 효과 */
    @keyframes glow {
        0% { text-shadow: 0 0 10px #ff4b4b; }
        50% { text-shadow: 0 0 20px #ff4b4b, 0 0 30px #ff8e53; }
        100% { text-shadow: 0 0 10px #ff4b4b; }
    }
    
    .title-text {
        font-size: 3.5rem !important;
        font-weight: 900;
        text-align: center;
        color: white;
        animation: glow 2s infinite;
        margin-bottom: 10px;
    }

    /* 카드 스타일링 */
    .stSelectbox, .stSlider, .stButton {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 10px;
    }

    /* 결과 박스 디자인 */
    .routine-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }

    .exercise-item {
        font-size: 1.2rem;
        margin-bottom: 10px;
        padding: 10px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 운동 데이터베이스
exercise_db = {
    "가슴 🔥": ["Push-ups", "Bench Press", "Incline Dumbbell Press", "Chest Fly"],
    "등 🦅": ["Pull-ups", "Lat Pull Down", "Seated Row", "Deadlift"],
    "하체 🍗": ["Squat", "Lunge", "Leg Press", "Leg Extension"],
    "어깨 🛡️": ["Shoulder Press", "Side Lateral Raise", "Front Raise"],
    "팔 💪": ["Bicep Curl", "Tricep Extension", "Hammer Curl"],
    "복근 🍫": ["Plank", "Crunch", "Leg Raise", "Russian Twist"]
}

# 4. 메인 UI
st.markdown('<p class="title-text">⚡ PUMP UP YOUR DAY ⚡</p>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #ccc;'>오늘의 한계를 뛰어넘을 준비가 되셨나요?</h4>", unsafe_allow_html=True)
st.markdown("---")

# 입력 세션
col1, col2 = st.columns(2)

with col1:
    target = st.selectbox("🎯 어디를 태워볼까요?", list(exercise_db.keys()))
    intensity = st.select_slider("🔥 오늘의 강도", options=["하 (순한맛)", "중 (보통맛)", "상 (매운맛)"], value="중 (보통맛)")

with col2:
    condition = st.selectbox("🔋 현재 몸 컨디션", ["🚀 에너자이저", "🆗 나쁘지 않음", "💤 약간 피곤", "🤕 근육통 주의"])
    workout_time = st.slider("⏰ 운동 가능 시간 (분)", 10, 120, 40, step=10)

# 5. 루틴 생성 로직
if st.button("🔥 나만의 루틴 생성하기!", use_container_width=True):
    with st.spinner('🚀 최적의 효율을 계산하는 중...'):
        time.sleep(1.5)
    
    # 강도 및 컨디션에 따른 세트/수행 조절
    sets = 3
    if intensity == "상 (매운맛)": sets = 5
    elif intensity == "하 (순한맛)": sets = 2
    
    if condition == "🚀 에너자이저": sets += 1
    elif condition == "🤕 근육통 주의": sets -= 1

    # 시간당 종목 수 (대략 1종목당 10~15분 소요 가정)
    num_exercises = max(2, workout_time // 15)
    selected_exercises = random.sample(exercise_db[target], min(num_exercises, len(exercise_db[target])))

    # 결과 발표
    st.balloons() # 박수 대신 축하 풍선 애니메이션!
    
    st.markdown(f"""
        <div class="routine-card">
            <h2 style='color: #ff4b4b;'>🏆 오늘의 {target} 정복 루틴</h2>
            <p style='color: #aaa;'>선택한 강도: <b>{intensity}</b> | 목표 시간: <b>{workout_time}분</b></p>
            <hr style='border: 0.5px solid rgba(255,255,255,0.1);'>
    """, unsafe_allow_html=True)
    
    for ex in selected_exercises:
        st.markdown(f"""
            <div class="exercise-item">
                ✨ <b>{ex}</b> : {sets} 세트 (세트당 12-15회)
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.success(f"💪 {condition} 상태에 맞춘 완벽한 구성입니다. 지금 바로 시작하세요!")

# 6. 동기부여 섹션
st.markdown("---")
quotes = [
    "남들이 그만둘 때 한 번 더 하는 사람이 승리한다. 🔥",
    "고통은 지나가지만, 근육은 남는다. 💪",
    "오늘의 노력이 내일의 나를 만든다. 🚀",
    "운동할 시간이 없다는 건 핑계일 뿐입니다. ⏰"
]
st.info(f"💡 **오늘의 한마디:** {random.choice(quotes)}")

# 푸터
st.markdown("<br><p style='text-align: center; color: #666;'>© 2026 WORKOUT ADVENTURE | Stay Strong!</p>", unsafe_allow_html=True)

import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="PUMP UP! 영상 튜토리얼",
    page_icon="🎬",
    layout="centered"
)

# 2. 화려한 CSS 스타일링 (애니메이션 및 디자인 강화)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .title-text {
        font-size: 3.2rem !important;
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(#ff4b4b, #ff8e53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 3s infinite;
        margin-bottom: 5px;
    }

    .routine-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }

    .video-section {
        border-left: 4px solid #ff4b4b;
        padding-left: 15px;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 운동 데이터베이스 (종목명과 검색용 키워드 포함)
exercise_info = {
    "가슴 🔥": [
        {"name": "Push-ups", "url": "https://www.youtube.com/watch?v=IODxDxX7oi4"},
        {"name": "Bench Press", "url": "https://www.youtube.com/watch?v=rT7DgVCn7iU"},
        {"name": "Incline Dumbbell Press", "url": "https://www.youtube.com/watch?v=8iPEnn-ltC8"}
    ],
    "하체 🍗": [
        {"name": "Squat", "url": "https://www.youtube.com/watch?v=q6hBSSfokzY"},
        {"name": "Lunge", "url": "https://www.youtube.com/watch?v=COKYKgQ8KR0"},
        {"name": "Leg Press", "url": "https://www.youtube.com/watch?v=IZxyjW7MPJQ"}
    ],
    "등 🦅": [
        {"name": "Pull-ups", "url": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
        {"name": "Lat Pull Down", "url": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
        {"name": "Seated Row", "url": "https://www.youtube.com/watch?v=GZbfZ033f74"}
    ],
    "어깨 🛡️": [
        {"name": "Shoulder Press", "url": "https://www.youtube.com/watch?v=qEwK6jnz8sI"},
        {"name": "Side Lateral Raise", "url": "https://www.youtube.com/watch?v=3VcKaXpzqRo"}
    ],
    "복근 🍫": [
        {"name": "Plank", "url": "https://www.youtube.com/watch?v=ASdvN_XEl_c"},
        {"name": "Russian Twist", "url": "https://www.youtube.com/watch?v=wkD8rjkodUI"}
    ]
}

# 4. 메인 화면 구성
st.markdown('<p class="title-text">🔥 ULTIMATE WORKOUT 🔥</p>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #aaa;'>정확한 자세가 완벽한 몸을 만듭니다!</h4>", unsafe_allow_html=True)

# 입력 위젯
with st.container():
    st.markdown("### ⚙️ 오늘의 운동 설정")
    c1, c2, c3 = st.columns(3)
    with c1:
        target = st.selectbox("🎯 타겟 부위", list(exercise_

import streamlit as st
import time

# 1. 페이지 설정 (제목, 아이콘, 레이아웃)
st.set_page_config(
    page_title="🌈 MBTI 꿈 찾기 어드벤처",
    page_icon="🚀",
    layout="centered"
)

# 2. 화려한 디자인을 위한 Custom CSS 적용
st.markdown("""
    <style>
    /* 전체 배경에 그라데이션 적용 */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* 제목 스타일링 */
    .title-text {
        font-size: 3rem !important;
        font-weight: 800;
        color: #4A90E2;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0px;
    }
    
    /* 서브 타이틀 스타일링 */
    .subtitle-text {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }

    /* 결과 카드 스타일링 */
    .result-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
        border-left: 10px solid #4A90E2;
        transition: transform 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 구성 (MBTI별 직업 및 설명)
mbti_data = {
    "ISTJ": {"job": "🎯 회계사, 공무원, 분석가", "desc": "철저하고 계획적이며 책임감이 강해요!"},
    "ISFJ": {"job": "🏥 간호사, 교사, 사회복지사", "desc": "타인을 돕는 것에 보람을 느끼는 따뜻한 마음의 소유자!"},
    "INFJ": {"job": "✍️ 작가, 심리상담사, 예술가", "desc": "통찰력이 뛰어나고 사람들에게 영감을 줘요!"},
    "INTJ": {"job": "💻 전략가, 과학자, 시스템 분석가", "desc": "논리적이고 독립적이며 미래를 설계하는 능력이 탁월해요!"},
    "ISTP": {"job": "🛠️ 엔지니어, 파일럿, 프로그래머", "desc": "도구 활용 능력이 뛰어나고 상황 적응력이 빨라요!"},
    "ISFP": {"job": "🎨 디자이너, 사진작가, 작곡가", "desc": "감수성이 풍부하고 현재의 아름다움을 즐길 줄 알아요!"},
    "INFP": {"job": "🌈 시인, 만화가, 환경운동가", "desc": "이상주의적이며 자신만의 가치관이 뚜렷해요!"},
    "INTP": {"job": "🔬 연구원, 철학자, 데이터 사이언티스트", "desc": "호기심이 많고 비판적인 분석 능력이 뛰어난 천재형!"},
    "ESTP": {"job": "🏎️ 기업가, 운동선수, 경찰관", "desc": "에너지가 넘치고 문제를 즉각적으로 해결하는 능력자!"},
    "ESFP": {"job": "🎭 배우, 이벤트 플래너, 연예인", "desc": "분위기 메이커이며 사람들과 어울리는 것을 정말 좋아해요!"},
    "ENFP": {"job": "📢 홍보 전문가, 여행가, 크리에이티브 디렉터", "desc": "상상력이 풍부하고 열정적으로 새로운 도전을 즐겨요!"},
    "ENTP": {"job": "🎤 발명가, 변호사, 마케팅 전문가", "desc": "말솜씨가 좋고 기발한 아이디어로 세상을 놀라게 해요!"},
    "ESTJ": {"job": "👔 경영자, 프로젝트 매니저, 군인", "desc": "조직을 이끄는 리더십과 실행력이 완벽해요!"},
    "ESFJ": {"job": "🤝 호텔리어, 승무원, 영업 전문가", "desc": "사교성이 좋고 주변 사람들을 잘 챙기는 친절왕!"},
    "ENFJ": {"job": "🏛️ 정치인, 코치, 외교관", "desc": "사람들의 성장을 돕고 공동체를 이끄는 리더!"},
    "ENTJ": {"job": "🚀 CEO, 컨설턴트, 판사", "desc": "비전이 뚜렷하고 목표 달성을 위해 거침없이 나아가요!"}
}

# 4. 메인 화면 구성
st.markdown('<p class="title-text">✨ 내 꿈을 찾는 MBTI 여행 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">여러분의 MBTI를 선택하고 딱 맞는 미래 직업을 확인해보세요! 🎈</p>', unsafe_allow_html=True)

# 중앙 정렬을 위한 컬럼 배치
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_mbti = st.selectbox(
        "당신의 MBTI는 무엇인가요? 🤔",
        options=list(mbti_data.keys()),
        index=0
    )
    
    predict_button = st.button("🚀 추천 직업 확인하기")

# 5. 결과 로직
if predict_button:
    with st.spinner('🌟 별들이 당신의 미래를 분석 중입니다...'):
        time.sleep(1.5)  # 분석하는 느낌을 주기 위한 지연
    
    st.balloons() # 축하 풍선 애니메이션
    
    data = mbti_data[selected_mbti]
    
    st.markdown(f"""
        <div class="result-card">
            <h2 style="color: #4A90E2; margin-top: 0;">🎉 {selected_mbti}를 위한 추천 진로</h2>
            <hr>
            <h3 style="margin-bottom: 10px;">🌟 추천 직업: {data['job']}</h3>
            <p style="font-size: 1.1rem; color: #555;">"{data['desc']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(f"💡 **{selected_mbti}** 유형의 친구들은 이런 직업에서 자신의 능력을 가장 잘 발휘할 수 있어요! 하지만 이건 참고일 뿐, 여러분의 꿈은 무한하답니다! ✈️")

# 6. 하단 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>© 2026 미래 진로 교육 연구소 🏫 | 멋진 꿈을 응원합니다!</p>", unsafe_allow_html=True)

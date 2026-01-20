import streamlit as st


# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="SCIENCE PULSE 2026", page_icon="🧬", layout="wide")

# 화려한 사이언스 테마 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .main {
        background: radial-gradient(circle, #001220 0%, #000000 100%);
        color: #ffffff;
    }
    
    .title-container {
        text-align: center;
        padding: 40px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 20px #00f2ff;
        margin-bottom: 40px;
    }

    .title-main {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem !important;
        background: linear-gradient(90deg, #00f2ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 0px;
    }

    .news-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00f2ff;
        margin-bottom: 20px;
        transition: 0.3s;
    }

    .news-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.12);
        box-shadow: 0 5px 15px rgba(0, 242, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 뉴스 소스 설정 (실제 RSS 피드 주소)
SOURCES = {
    "🚀 NASA Breaking News": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "🧪 Science Magazine": "https://www.science.org/rss/news_current.xml",
    "💻 MIT Tech Review": "https://www.technologyreview.com/feed/",
    "🌍 Shell Global News": "https://www.shell.com/media/news-and-media-releases.rss"
}

# 3. 사이드바 - 카테고리 선택
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/science.png")
    st.markdown("## 🔍 탐색 설정")
    selected_source = st.selectbox("잡지사 선택", list(SOURCES.keys()))
    num_news = st.slider("가져올 뉴스 개수", 5, 20, 10)
    st.markdown("---")
    st.info("💡 **Tip:** 최신 AI 및 물리학 뉴스는 과학 영재학교 입시와 탐구 대회 준비에 큰 도움이 됩니다!")

# 4. 메인 타이틀 섹션
st.markdown("""
    <div class="title-container">
        <p class="title-main">SCIENCE PULSE</p>
        <p style='font-size: 1.5rem;'>🛰️ 2026 글로벌 과학 트렌드 실시간 브리핑</p>
    </div>
    """, unsafe_allow_html=True)

# 5. 뉴스 데이터 파싱 및 출력
def display_news(url, limit):
    feed = feedparser.parse(url)
    if not feed.entries:
        st.error("뉴스를 불러올 수 없습니다. 링크를 확인해 주세요!")
        return

    for i, entry in enumerate(feed.entries[:limit]):
        with st.container():
            # 날짜 포맷팅
            date = getattr(entry, 'published', '날짜 정보 없음')
            
            st.markdown(f"""
                <div class="news-card">
                    <span style='color: #00f2ff; font-weight: bold;'>NEWS {i+1}</span>
                    <h3 style='margin-top: 5px;'>{entry.title}</h3>
                    <p style='color: #cccccc; font-size: 0.9rem;'>📅 {date}</p>
                    <p style='margin-bottom: 15px;'>{entry.summary[:200] if hasattr(entry, 'summary') else '내용 요약이 없습니다.'}...</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"🔗 기사 원문 읽기", entry.link)
            st.markdown("<br>", unsafe_allow_html=True)

# 실행
st.subheader(f"✨ {selected_source}의 최신 헤드라인")
display_news(SOURCES[selected_source], num_news)

# 6. 교육용 인터랙티브 섹션 (하단)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧠 오늘의 과학 퀴즈")
    st.write("인공지능(AI)이 스스로 학습하여 인간의 지능을 뛰어넘는 지점을 무엇이라 할까요?")
    if st.button("정답 확인 💡"):
        st.success("정답은 **'특이점(Singularity)'**입니다! 미래 과학의 핵심 키워드죠.")

with col2:
    st.markdown("### 🧪 탐구 아이디어 뱅크")
    ideas = [
        "기계학습을 이용한 교내 에너지 절약 알고리즘",
        "액체 금속을 활용한 물리 시뮬레이션 연구",
        "기후 변화에 따른 미세 조류의 산소 발생량 비교"
    ]
    st.write(f"추천 주제: **{random.choice(ideas)}**")

# 푸터
st.markdown("<br><p style='text-align: center; color: #444;'>© 2026 Future Science Academy | Inspired by Innovation</p>", unsafe_allow_html=True)

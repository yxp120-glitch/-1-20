import streamlit as st
import feedparser
import random
from datetime import datetime

# 1. 페이지 레이아웃 및 스타일 설정
st.set_page_config(
    page_title="SCIENCE HUB 2026",
    page_icon="🧪",
    layout="wide"
)

# 화려한 시각 효과를 위한 CSS
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 */
    .stApp {
        background: linear-gradient(to bottom, #000428, #004e92);
        color: white;
    }
    
    /* 메인 타이틀 스타일 */
    .main-title {
        font-size: 50px !important;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(#00f2ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* 뉴스 카드 디자인 */
    .news-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 242, 255, 0.3);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    
    .news-box:hover {
        transform: scale(1.02);
        background-color: rgba(255, 255, 255, 0.15);
    }

    /* 이모지 강조 */
    .emoji-icon {
        font-size: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 뉴스 데이터 소스 (RSS 피드)
NEWS_SOURCES = {
    "🚀 NASA 뉴스": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "🧬 Science Magazine": "https://www.science.org/rss/news_current.xml",
    "💻 MIT Tech Review": "https://www.technologyreview.com/feed/",
    "🐚 Shell Global News": "https://www.shell.com/media/news-and-media-releases.rss"
}

# 3. 사이드바 구성
with st.sidebar:
    st.markdown("# 🧭 탐사 메뉴")
    st.write("원하는 과학 잡지를 선택하세요!")
    choice = st.radio("매체 선택", list(NEWS_SOURCES.keys()))
    
    st.markdown("---")
    st.markdown("### 📊 오늘의 과학 지수")
    st.metric(label="지적 호기심", value="100%", delta="5%")
    st.metric(label="탐구 열정", value="MAX", delta="🔥")

# 4. 메인 화면 출력
st.markdown('<p class="main-title">🧪 SCIENCE EXPLORER 2026</p>', unsafe_allow_html=True)
st.write("<p style='text-align:center; font-size:1.2rem;'>최첨단 과학 소식을 실시간으로 만나보세요! 🛰️</p>", unsafe_allow_html=True)
st.markdown("---")

# 뉴스 불러오기 함수
def fetch_news(url):
    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            return None
        return feed.entries
    except Exception as e:
        return None

# 뉴스 표시 로직
entries = fetch_news(NEWS_SOURCES[choice])

if entries:
    # 상위 10개 뉴스만 표시
    for i, entry in enumerate(entries[:10]):
        with st.container():
            st.markdown(f"""
                <div class="news-box">
                    <h3>📢 {entry.title}</h3>
                    <p style='color: #00f2ff;'>📅 {getattr(entry, 'published', '2026-01-20')}</p>
                    <p>{entry.summary[:250] if hasattr(entry, 'summary') else '상세 내용은 본문 링크를 확인해주세요.'}...</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"🔗 {choice} 원문 보기", entry.link)
            st.write("") # 간격 조절
else:
    st.warning("⚠️ 뉴스를 불러오는 중입니다. 잠시 후 다시 시도하거나 다른 소스를 선택해 주세요!")

# 5. 교육용 인터랙티브 섹션 (하단 하이라이트)
st.markdown("---")
st.markdown("### 💡 미래 과학도를 위한 한 줄 아이디어")

ideas = [
    "🤖 생성형 AI가 과학 논문을 검증할 수 있을까?",
    "⚛️ 양자 컴퓨터가 실생활에 들어오는 시점은 언제일까?",
    "🚀 화성 거주지 설계를 위한 물리 시뮬레이션 만들기",
    "🧬 유전자 가위 기술로 질병 없는 세상을 만들 수 있을까?"
]

random_idea = random.choice(ideas)
st.success(f"**오늘의 탐구 주제:** {random_idea}")

# 박수 및 축하 애니메이션 (선택사항)
if st.button("🎉 오늘 공부 완료! 클릭해서 축하하기"):
    st.balloons()
    st.toast("훌륭합니다! 미래의 과학자님! 👨‍🔬👩‍🔬")

# 푸터
st.markdown("<br><p style='text-align: center; color: #888;'>Powered by Streamlit & Python 2026</p>", unsafe_allow_html=True)

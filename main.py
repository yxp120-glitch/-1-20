import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 (화려한 제목과 아이콘)
st.set_page_config(page_title="🚀 사이언스 뉴스 익스플로러", page_icon="🧬", layout="wide")

# 2. 커스텀 CSS (최대한 화려하게!)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a40 100%);
        color: white;
    }
    .stApp {
        background-color: #0e1117;
    }
    h1 {
        color: #00f2fe;
        text-shadow: 2px 2px #4facfe;
    }
    .news-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00f2fe;
        margin-bottom: 15px;
        transition: transform 0.3s;
    }
    .news-card:hover {
        transform: scale(1.02);
        background-color: #374151;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 뉴스 데이터 가져오기 함수
def get_news(url):
    feed = feedparser.parse(url)
    return feed.entries[:5]  # 최신 5개만

# 뉴스 소스 설정
NEWS_SOURCES = {
    "🧬 Science Magazine": "https://www.science.org/rss/news_current.xml",
    "🤖 MIT Tech Review": "https://www.technologyreview.com/topnews.rss",
    "⚡ Energy & Innovation (Shell/Phys.org)": "https://phys.org/rss-feed/energy-news/",
    "🧠 AI & Machine Learning": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml",
    "⚛️ Physics & Math": "https://phys.org/rss-feed/physics-news/"
}

# 4. 사이드바 구성
st.sidebar.title("🧬 Science Menu")
st.sidebar.markdown("---")
choice = st.sidebar.selectbox("보고 싶은 카테고리를 골라봐!", list(NEWS_SOURCES.keys()))
st.sidebar.info(f"선택된 뉴스: {choice}")

# 교육용 섹션 - 오늘의 과학 팁
st.sidebar.markdown("---")
st.sidebar.subheader("💡 오늘의 과학 상식")
st.sidebar.write("상대성 이론에 따르면, 움직이는 물체의 시간은 느리게 간답니다! 🕒✨")

# 5. 메인 화면 구성
st.title("🚀 사이언스 뉴스 익스플로러 🧬")
st.markdown(f"### ✨ 현재 카테고리: **{choice}**")

# 뉴스 불러오기 및 표시
with st.spinner('최신 뉴스를 가져오는 중... 🏃‍♂️💨'):
    news_items = get_news(NEWS_SOURCES[choice])

    if not news_items:
        st.warning("뉴스를 불러올 수 없어요. 잠시 후 다시 시도해봐요! 🛠️")
    
    for item in news_items:
        with st.container():
            st.markdown(f"""
                <div class="news-card">
                    <h4>🔗 <a href="{item.link}" style="text-decoration:none; color:#00f2fe;">{item.title}</a></h4>
                    <p style="font-size: 0.9rem; color: #cbd5e1;">{item.published if 'published' in item else ''}</p>
                    <p>{item.summary[:200] if 'summary' in item else '내용 요약이 없습니다.'}...</p>
                </div>
            """, unsafe_allow_html=True)

# 6. 특별 교육 섹션 (하단)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 과학 탐구 토론 주제 추천")
    st.write("방금 본 뉴스 중 가장 흥미로운 것은 무엇인가요? 친구들과 **AI의 윤리**나 **미래 에너지**에 대해 토론해보세요! 🗣️")

with col2:
    st.subheader("📊 나의 학습 현황")
    st.progress(75, text="이번 주 과학 뉴스 정복률 75%")
    st.write("멋져요! 오늘 벌써 3개의 기사를 읽었네요! 🏆")

# 7. 푸터
st.markdown("<p style='text-align: center; color: gray;'>Designed for Science High School Aspirants 🧪📐</p>", unsafe_allow_html=True)

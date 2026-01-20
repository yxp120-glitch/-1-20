import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(
    page_title="🚀 사이언스 갤럭시 뉴스 허브",
    page_icon="🧬",
    layout="wide"
)

# ---------- RSS 소스 ----------
SOURCE_INFO = {
    "Science Magazine 🧪": "https://www.science.org/rss/news_current.xml",
    "MIT Technology Review 🤖": "https://www.technologyreview.com/feed",
    "MIT News – School of Science 🎓": "https://news.mit.edu/rss/school/science",
    "ScienceDaily – Top Science 🌍": "https://www.sciencedaily.com/rss/top/science.xml",
    "Science News Magazine 📰": "https://www.sciencenews.org/feed",
}

# ---------- 사이드바 ----------
st.sidebar.markdown("## 🔭 Science Galaxy")
st.sidebar.markdown(
    """
중·고등학생을 위한 **초신박 과학 뉴스 허브** 🌌  
전 세계 과학 기사들을 한 번에 모아서 보여줘요!
"""
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛰 뉴스 소스 선택")

selected_sources = st.sidebar.multiselect(
    "불러올 뉴스 사이트를 골라보세요:",
    options=list(SOURCE_INFO.keys()),
    default=list(SOURCE_INFO.keys())
)

st.sidebar.markdown(

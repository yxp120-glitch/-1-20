import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(
    page_title="🚀 사이언스 갤럭시 뉴스 허브",
    page_icon="🧬",
    layout="wide"
)

# ---------- 사이드바 ----------
st.sidebar.markdown("## 🔭 Science Galaxy")
st.sidebar.markdown("""
중·고등학생을 위한 **초신박 과학 뉴스 허브** 🌌  
전 세계 과학 기사들을 한 번에 모아서 보여줘요!
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛰 뉴스 소스 선택")

SOURCE_INFO = {
    "Science Magazine 🧪": "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science",
    "MIT Technology Review 🤖": "https://www.technologyreview.com/feed",
    "MIT News – School of Science 🎓": "https://news.mit.edu/rss/school/science",
    "ScienceDaily – Top Science 🌍": "https://www.sciencedaily.com/rss/top/science.xml",
    "Science News Magazine 📰": "https://www.sciencenews.org/feed",
}

selected_sources = st.sidebar.multiselect(
    "불러올 뉴스 사이트를 골라보세요:",
    options=list(SOURCE_INFO.keys()),
    default=list(SOURCE_INFO.keys())
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎨 테마 옵션")
theme = st.sidebar.radio(
    "전체 분위기",
    ["🌈 레인보우 하이틴", "🌌 다크 우주", "☀️ 라이트 깔끔"]
)

max_items = st.sidebar.slider("각 사이트에서 불러올 기사 수", 3, 15, 7)


# ---------- 스타일 ----------
if theme == "🌈 레인보우 하이틴":
    bg_color = "#0f172a"
    card_color = "#020617"
    accent = "#f97316"
elif theme == "🌌 다크 우주":
    bg_color = "#020617"
    card_color = "#020617"
    accent = "#38bdf8"
else:
    bg_color = "#f9fafb"
    card_color = "#ffffff"
    accent = "#6366f1"

custom_css = f"""
<style>
    body {{
        background: radial-gradient(circle at top, #1d4ed8 0, {bg_color} 45%, #020617 100%);
        color: #e5e7eb;
    }}
    .main {{
        background: transparent;
    }}
    .news-card {{
        background: linear-gradient(135deg, {card_color}, #020617);
        border-radius: 18px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        border: 1px solid rgba(148, 163, 184, 0.4);
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.9);
    }}
    .news-title {{
        font-size: 1.05rem;
        font-weight: 700;
        color: #e5e7eb;
    }}
    .news-meta {{
        font-size: 0.8rem;
        color: #9ca3af;
    }}
    .news-summary {{
        font-size: 0.9rem;
        color: #cbd5f5;
    }}
    .source-pill {{
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.75rem;
        margin-right: 0.3rem;
        background: rgba(148, 163, 184, 0.

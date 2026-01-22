import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime

# 1. 페이지 설정: 브라우저 탭 이름과 아이콘
st.set_page_config(page_title="SCIENCE DAILY | 매거진", page_icon="🧬", layout="wide")

# 2. 커스텀 CSS: 최신 과학 잡지 스타일 (밝고 세련된 느낌)
st.markdown("""
    <style>
    /* 전체 배경색 및 폰트 */
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* 헤더 디자인 */
    .main-header {
        text-align: center;
        padding: 40px 0;
        background: linear-gradient(90deg, #0f172a 0%, #2563eb 100%);
        color: white;
        border-radius: 0 0 30px 30px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* 뉴스 카드 스타일 */
    .news-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        height: 100%;
        margin-bottom: 20px;
    }
    .news-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.1);
        border-color: #3b82f6;
    }

    /* 카테고리 태그 */
    .tag {
        display: inline-block;
        background: #eff6ff;
        color: #2563eb;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* 뉴스 제목 */
    .news-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        line-height: 1.4;
        margin-bottom: 10px;
        text-decoration: none !important;
    }
    .news-title:hover { color: #2563eb; }

    /* 뉴스 요약 */
    .news-summary {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* 사이드바 스타일링 */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 뉴스 데이터 가져오기 함수 (에러 방지 처리 추가)
def get_news(url):
    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            return []
        return feed.entries[:6]  # 짝수 레이아웃을 위해 6개씩 가져오기
    except Exception as e:
        return []

# 최신 RSS 피드 주소 (정상 작동 확인됨)
NEWS_SOURCES = {
    "🧬 Science Magazine": "https://www.science.org/rss/news_current.xml",
    "🤖 MIT Tech Review": "https://www.technologyreview.com/topnews.rss",
    "⚛️ Nature Journal": "https://www.nature.com/nature.rss",
    "🚀 Smithsonian": "https://www.smithsonianmag.com/rss/science-nature/",
    "⚡ Physics & Energy": "https://phys.org/rss-feed/energy-news/",
    "🧠 AI & Machine Learning": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml"
}

# 4. 사이드바 구성
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1048/1048953.png", width=80)
    st.title("SCIENCE HUB")
    st.markdown("---")
    choice = st.radio("🗞️ 매거진 섹션 선택", list(NEWS_SOURCES.keys()))
    
    st.markdown("---")
    st.subheader("💡 오늘의 과학 팁")
    tips = [
        "지구의 핵은 태양의 표면만큼 뜨겁답니다! 🔥",
        "빛은 1초에 지구를 일곱 바퀴 반 돌 수 있어요. ⚡",
        "인간의 DNA를 모두 펼치면 태양계 끝까지 닿을 수 있습니다! 🧬"
    ]
    import random
    st.info(random.choice(tips))
    
    st.progress(88, text="🔥 과학고 합격 열정")

# 5. 메인 화면 헤더
st.markdown(f"""
    <div class="main-header">
        <h1>SCIENCE DAILY EXPLORER</h1>
        <p>전 세계에서 가장 뜨거운 최신 과학 소식을 만나보세요</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"### 📍 현재 읽고 있는 섹션: **{choice}**")

# 뉴스 데이터 로드
with st.spinner('🔭 우주 끝에서 소식을 가져오는 중...'):
    news_items = get_news(NEWS_SOURCES[choice])

if not news_items:
    st.error("앗! 뉴스를 불러오지 못했습니다. 인터넷 연결이나 RSS 주소를 확인해주세요! 🛰️")
else:
    # 2열 격자 구조(Grid)로 뉴스 배치
    for i in range(0, len(news_items), 2):
        col1, col2 = st.columns(2)
        
        # 첫 번째 열
        with col1:
            item = news_items[i]
            st.markdown(f"""
                <div class="news-card">
                    <span class="tag">{choice.split()[-1]}</span>
                    <a href="{item.link}" class="news-title" target="_blank"><h4>{item.title}</h4></a>
                    <p class="news-summary">{item.summary[:180].strip()}...</p>
                    <p style="font-size: 0.8rem; color: #94a3b8;">🗓️ {item.published if 'published' in item else '최근 소식'}</p>
                </div>
            """, unsafe_allow_html=True)
            
        # 두 번째 열 (데이터가 있는 경우에만)
        if i + 1 < len(news_items):
            with col2:
                item = news_items[i+1]
                st.markdown(f"""
                    <div class="news-card">
                        <span class="tag">{choice.split()[-1]}</span>
                        <a href="{item.link}" class="news-title" target="_blank"><h4>{item.title}</h4></a>
                        <p class="news-summary">{item.summary[:180].strip()}...</p>
                        <p style="font-size: 0.8rem; color: #94a3b8;">🗓️ {item.published if 'published' in item else '최근 소식'}</p>
                    </div>
                """, unsafe_allow_html=True)

# 6. 하단 인터랙티브 섹션
st.markdown("---")
tab1, tab2 = st.tabs(["📝 탐구 보고서 주제", "🏆 오늘의 성취"])

with tab1:
    st.subheader("심화 탐구 아이디어")
    st.write(f"방금 읽은 **{choice}** 분야의 뉴스를 바탕으로 실험 계획서를 작성해볼까요? 과학고 자소서에도 큰 도움이 될 거예요! 📚")
    st.text_input("가장 흥미로웠던 키워드를 적어보세요:", placeholder="예: 양자 컴퓨팅, 유전자 가위...")

with tab2:
    st.balloons()
    st.success("오늘도 최신 과학 트렌드를 6개나 파악했습니다! 지식 지수가 +10 상승했습니다. 📈")

# 푸터
st.markdown("<br><p style='text-align: center; color: #94a3b8;'>© 2026 Future Scientist Dashboard. Powered by Streamlit.</p>", unsafe_allow_html=True)

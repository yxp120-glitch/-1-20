import streamlit as st
import feedparser
import random

# 1. 페이지 설정: 브라우저 탭 이름과 아이콘
st.set_page_config(page_title="SCIENCE DAILY | 매거진", page_icon="🧪", layout="wide")

# 2. 커스텀 CSS: 최신 과학 잡지 스타일 (밝고 전문적인 느낌)
st.markdown("""
    <style>
    /* 전체 배경색 및 폰트 */
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* 뉴스 카드 스타일 */
    .news-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        height: 320px;
        margin-bottom: 20px;
        overflow: hidden;
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
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* 뉴스 제목 */
    .news-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1e293b;
        line-height: 1.4;
        margin-bottom: 10px;
        text-decoration: none !important;
        display: block;
    }
    .news-title:hover { color: #2563eb; }

    /* 뉴스 요약 */
    .news-summary {
        color: #64748b;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* 배너 이미지 컨테이너 */
    .banner-container {
        border-radius: 25px;
        overflow: hidden;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        height: 280px;
    }
    
    .banner-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 뉴스 데이터 가져오기 함수 (문법 오류 수정 완료!)
def get_news(url):
    try:
        # 뉴스 데이터를 가져오려고 시도합니다.
        feed = feedparser.parse(url, agent='Mozilla/5.0')
        if not feed.entries:
            return []
        return feed.entries[:6]
    except Exception as e:
        # 에러 발생 시 앱이 멈추지 않도록 빈 리스트를 반환합니다.
        return []

# 뉴스 소스 및 카테고리별 매칭 이미지
NEWS_SOURCES = {
    "🧬 Science Magazine": "https://www.science.org/rss/news_current.xml",
    "🤖 MIT Tech Review": "https://www.technologyreview.com/topnews.rss",
    "⚛️ Nature Journal": "https://www.nature.com/nature.rss",
    "🚀 Smithsonian Space": "https://www.smithsonianmag.com/rss/science-nature/",
    "⚡ Physics & Energy": "https://phys.org/rss-feed/energy-news/",
    "🧠 AI & Machine Learning": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml"
}

CATEGORY_IMAGES = {
    "🧬 Science Magazine": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?q=80&w=1200", 
    "🤖 MIT Tech Review": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=1200", 
    "⚛️ Nature Journal": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200", 
    "🚀 Smithsonian Space": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=1200", 
    "⚡ Physics & Energy": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?q=80&w=1200", 
    "🧠 AI & Machine Learning": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1200"
}

# 4. 사이드바 구성
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1048/1048953.png", width=60)
    st.title("SCIENCE HUB")
    st.markdown("---")
    choice = st.radio("🗞️ 매거진 섹션", list(NEWS_SOURCES.keys()))
    
    st.markdown("---")
    st.subheader("💡 오늘의 과학 상식")
    tips = [
        "지구의 핵은 태양 표면만큼 뜨겁답니다! 🔥",
        "빛은 1초에 지구를 일곱 바퀴 반 돌 수 있어요. ⚡",
        "인간의 DNA를 펼치면 태양계 끝까지 닿을 수 있습니다! 🧬"
    ]
    st.info(random.choice(tips))
    
    st.progress(92, text="📖 탐구 지수 상승 중")

# 5. 메인 화면 구성
# 상단 비주얼 배너
st.markdown(f"""
    <div class="banner-container">
        <img src="{CATEGORY_IMAGES[choice]}" class="banner-image">
    </div>
    """, unsafe_allow_html=True)

st.title(f"🔭 {choice[2:]} Explorer")
st.markdown("최신 과학 기술과 연구 성과를 한눈에 확인하세요.")

# 뉴스 로드
with st.spinner('🔭 우주 끝에서 데이터를 전송받는 중...'):
    news_items = get_news(NEWS_SOURCES[choice])

if not news_items:
    st.error("뉴스를 불러오지 못했습니다. RSS 피드 주소를 확인하거나 잠시 후 다시 시도해주세요! 🛰️")
else:
    # 2열 격자 배치
    for i in range(0, len(news_items), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            item = news_items[i]
            st.markdown(f"""
                <div class="news-card">
                    <span class="tag">LATEST</span>
                    <a href="{item.link}" class="news-title" target="_blank">{item.title}</a>
                    <p class="news-summary">{item.summary[:160].strip()}...</p>
                    <p style="font-size: 0.8rem; color: #94a3b8; margin-top: 10px;">🗓️ {item.published[:16] if 'published' in item else 'Recent'}</p>
                </div>
            """, unsafe_allow_html=True)
            
        if i + 1 < len(news_items):
            with col2:
                item = news_items[i+1]
                st.markdown(f"""
                    <div class="news-card">
                        <span class="tag">LATEST</span>
                        <a href="{item.link}" class="news-title" target="_blank">{item.title}</a>
                        <p class="news-summary">{item.summary[:160].strip()}...</p>
                        <p style="font-size: 0.8rem; color: #94a3b8; margin-top: 10px;">🗓️ {item.published[:16] if 'published' in item else 'Recent'}</p>
                    </div>
                """, unsafe_allow_html=True)

# 6. 하단 인터랙티브 섹션 (요청하신 대로 텍스트 수정)
st.markdown("---")
t1, t2 = st.tabs(["📝 탐구 노트", "✨ 투데이 성취"])

with t1:
    st.subheader("심화 탐구 질문 만들기")
    st.write(f"오늘 읽은 **{choice[2:]}** 소식 중 가장 놀라웠던 점은 무엇인가요? 나만의 가설을 세우고 탐구해보세요!")
    st.text_input("탐구 키워드 기록:", placeholder="예: 양자 역학, 탄소 중립 기술...")

with t2:
    st.success("🎉 오늘 총 6개의 최신 과학 지식을 습득하셨습니다! 당신의 탐구 열정을 응원합니다.")
    st.balloons()

# 푸터
st.markdown("<br><p style='text-align: center; color: #94a3b8;'>© 2026 Future Scientist Portal. Powered by Science RSS.</p>", unsafe_allow_html=True)

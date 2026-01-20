import streamlit as st
from PIL import Image

# 1. 페이지 설정
st.set_page_config(page_title="내 포트폴리오", page_icon="👤", layout="wide")

# 2. CSS를 이용한 스타일링 (선택 사항)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 사이드바 - 연락처 및 기본 정보
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="내 사진") # 실제 사진 경로로 변경하세요
    st.title("snu (snu)")
    st.write("📍 서울특별시, 대한민국")
    st.write("📧 snu@gmail.com")
    st.write("🔗 [GitHub](https://github.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    
    st.divider()
    st.subheader("Languages")
    st.write("Korean (Native)")
    st.write("English (Professional)")

# 4. 메인 화면 - 자기소개 및 상세 내용
col1, col2 = st.columns([2, 1])

with col1:
    st.title("안녕하세요, 데이터를 사랑하는 개발자 snu입니다! 👋")
    st.subheader("About Me")
    st.info("""
    저는 복잡한 문제를 해결하고 효율적인 시스템을 구축하는 것에 열정을 가지고 있습니다. 
    현재 파이썬과 스트림릿을 활용하여 데이터 시각화 도구를 개발하고 있으며, 
    항상 새로운 기술을 배우는 것을 즐깁니다.
    """)

    st.write("---")
    
    # 경력/프로젝트 섹션
    st.subheader("🚀 주요 프로젝트")
    
    with st.expander("1. 데이터 시각화 대시보드 구축"):
        st.write("**기술 스택:** Python, Pandas, Streamlit")
        st.write("- 기업 내부 데이터를 활용한 실시간 매출 지표 시각화")
        st.write("- 데이터 전처리 자동화로 업무 효율 30% 향상")
        
    with st.expander("2. 웹 크롤링 기반 뉴스 요약 봇"):
        st.write("**기술 스택:** BeautifulSoup, OpenAI API")
        st.write("- 특정 키워드 뉴스를 수집하여 매일 아침 슬랙으로 요약본 전송")

with col2:
    st.subheader("🛠 My Skills")
    
    # 기술 스택 시각화
    st.write("Python")
    st.progress(90)
    st.write("Data Analysis (Pandas/NumPy)")
    st.progress(85)
    st.write("Machine Learning")
    st.progress(70)
    st.write("Web Development (Streamlit)")
    st.progress(80)

    st.write("---")
    st.subheader("🎓 Education")
    st.write("**한국대학교**")
    st.caption("컴퓨터공학 학사 (2018 - 2022)")

# 5. 하단 컨택트 폼
st.write("---")
st.subheader("📫 나에게 메시지 보내기")
with st.form("contact_form"):
    name = st.text_input("이름")
    email = st.text_input("이메일 주소")
    message = st.text_area("내용")
    submit_button = st.form_submit_button("보내기")
    
    if submit_button:
        st.success(f"{name}님, 메시지가 성공적으로 전송되었습니다! (실제 기능은 백엔드 연결 필요)")

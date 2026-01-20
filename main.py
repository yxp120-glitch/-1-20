import streamlit as st


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MBTI 진로 추천 ✨",
    page_icon="🧭",
    layout="wide",
)

# -----------------------------
# Fancy CSS
# -----------------------------
CSS = """
<style>
:root{
  --bg1:#0f172a;
  --bg2:#1f2937;
  --card:#0b1220cc;
  --glass: rgba(255,255,255,0.08);
  --stroke: rgba(255,255,255,0.14);
  --text: rgba(255,255,255,0.92);
  --muted: rgba(255,255,255,0.72);
  --accent1:#22c55e;
  --accent2:#60a5fa;
  --accent3:#f472b6;
  --accent4:#f59e0b;
}

.block-container{
  padding-top: 2.2rem;
  padding-bottom: 2.5rem;
  max-width: 1200px;
}

.stApp{
  background:
    radial-gradient(1200px 600px at 15% 10%, rgba(96,165,250,0.22), transparent 55%),
    radial-gradient(900px 500px at 85% 25%, rgba(244,114,182,0.20), transparent 55%),
    radial-gradient(1000px 700px at 50% 90%, rgba(34,197,94,0.16), transparent 60%),
    linear-gradient(145deg, var(--bg1), var(--bg2));
  color: var(--text);
}

h1, h2, h3, h4{
  color: var(--text) !important;
  letter-spacing: -0.02em;
}
p, li{
  color: var(--muted) !important;
}

.badge{
  display:inline-flex;
  align-items:center;
  gap:.5rem;
  padding:.35rem .6rem;
  border-radius:999px;
  background: linear-gradient(90deg, rgba(96,165,250,.25), rgba(244,114,182,.25));
  border: 1px solid rgba(255,255,255,0.16);
  box-shadow: 0 10px 30px rgba(0,0,0,0.20);
  font-weight:700;
  font-size:.92rem;
}

.hero{
  border-radius: 24px;
  padding: 1.4rem 1.4rem;
  background: linear-gradient(135deg, rgba(255,255,255,0.09), rgba(255,255,255,0.04));
  border: 1px solid rgba(255,255,255,0.14);
  box-shadow: 0 18px 55px rgba(0,0,0,0.35);
  position: relative;
  overflow:hidden;
}
.hero:before{
  content:"";
  position:absolute;
  inset:-2px;
  background:
    radial-gradient(800px 300px at 20% 0%, rgba(96,165,250,0.35), transparent 55%),
    radial-gradient(800px 400px at 80% 20%, rgba(244,114,182,0.28), transparent 60%),
    radial-gradient(900px 600px at 50% 100%, rgba(34,197,94,0.20), transparent 60%);
  filter: blur(12px);
  opacity: .8;
  z-index:0;
}
.hero > div{ position:relative; z-index:1; }

.grid{
  display:grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
}
.card{
  grid-column: span 6;
  border-radius: 18px;
  padding: 1.05rem 1.05rem;
  background: rgba(11,18,32,0.52);
  border: 1px solid rgba(255,255,255,0.14);
  box-shadow: 0 16px 40px rgba(0,0,0,0.32);
  backdrop-filter: blur(10px);
}
@media (max-width: 900px){
  .card{ grid-column: span 12; }
}

.card h3{
  margin: 0 0 .4rem 0;
  font-size: 1.15rem;
}

.kpi{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  margin-top:.5rem;
}
.pill{
  display:inline-flex;
  align-items:center;
  gap:.45rem;
  padding:.35rem .55rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  color: rgba(255,255,255,0.85);
  font-weight: 600;
  font-size: .92rem;
}

.glow-btn button{
  background: linear-gradient(90deg, rgba(96,165,250,0.9), rgba(244,114,182,0.88)) !important;
  border: 0 !important;
  color: white !important;
  font-weight: 800 !important;
  border-radius: 14px !important;
  padding: 0.75rem 1rem !important;
  box-shadow: 0 18px 35px rgba(96,165,250,0.22), 0 18px 35px rgba(244,114,182,0.18) !important;
}
.glow-btn button:hover{
  transform: translateY(-1px);
  filter: brightness(1.03);
}

hr{
  border: none;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
  margin: 1rem 0;
}

.small-note{
  font-size:.92rem;
  color: rgba(255,255,255,0.68);
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------
# Data (교육용 추천: 절대적 진단 X)
# -----------------------------
MBTI_INFO = {
    "ISTJ": {
        "name": "세밀한 관리자 🧾",
        "keywords": ["책임감", "정확성", "규칙", "체계"],
        "careers": [
            ("회계/세무 💰", "꼼꼼함과 규정 이해가 강점! 숫자·기록·정산 업무에 안정적으로 강해요."),
            ("품질관리(QA) 🔍", "표준과 체크리스트 기반으로 오류를 잡아내는 역할에 잘 맞아요."),
            ("공무원/행정 🏛️", "규정과 절차에 맞춰 안정적으로 운영하는 능력이 돋보여요."),
            ("프로젝트 운영/PMO 🧭", "일정·리스크·문서관리 등 ‘관리형’ 업무에서 빛나요."),
        ],
        "skills": ["문서화", "리스크 체크", "프로세스 설계", "정확한 보고"],
        "activities": ["엑셀/회계 기초", "품질관리 사례 분석", "행정/정책 리포트 작성"]
    },
    "ISFJ": {
        "name": "따뜻한 수호자 🛡️",
        "keywords": ["배려", "헌신", "안정", "세심함"],
        "careers": [
            ("간호/보건 🩺", "세심한 케어와 책임감이 강점! 사람을 돌보는 일에 잘 맞아요."),
            ("상담/코칭 💬", "경청과 공감으로 상대를 편안하게 만드는 힘이 있어요."),
            ("교육/행정 지원 📚", "학생·조직을 뒤에서 든든하게 받치는 역할에 강해요."),
            ("HR/조직문화 🤝", "사람 중심으로 팀 분위기와 제도를 다듬는 일에 적합해요."),
        ],
        "skills": ["공감", "상담 기초", "서비스 마인드", "관계 조율"],
        "activities": ["멘토링/봉사", "상담 기초 독서", "학교 행사 운영 참여"]
    },
    "INFJ": {
        "name": "통찰하는 조언자 🔮",
        "keywords": ["의미", "비전", "성장", "깊이"],
        "careers": [
            ("심리/상담 🧠", "사람의 내면을 이해하고 성장에 기여하는 역할에 강해요."),
            ("콘텐츠 기획/작가 ✍️", "메시지·의미 중심의 글과 기획을 잘 만들어요."),
            ("교육 기획/연구 📑", "가치 있는 교육 경험을 설계하고 개선하는 일에 적합해요."),
            ("사회혁신/NGO 🌍", "세상을 더 낫게 만드는 방향에 몰입이 잘 돼요."),
        ],
        "skills": ["리서치", "스토리텔링", "비전 설계", "윤리·가치 판단"],
        "activities": ["주제 탐구 보고서", "사회문제 프로젝트", "글쓰기/독서 클럽"]
    },
    "INTJ": {
        "name": "전략가 설계자 🧠",
        "keywords": ["전략", "시스템", "효율", "독립성"],
        "careers": [
            ("데이터/AI 🔢", "문제를 구조화하고 최적화를 설계하는 데 강해요."),
            ("전략기획/컨설팅 🧩", "복잡한 상황을 분석해 방향을 세우는 역할에 적합!"),
            ("R&D 연구원 🧪", "가설→실험→개선 사이클을 즐길 확률이 높아요."),
            ("제품기획(PO) 🧭", "사용자 문제를 논리적으로 풀어 제품으로 만드는 일에 좋아요."),
        ],
        "skills": ["문제분해", "모델링", "논리적 글쓰기", "장기 플래닝"],
        "activities": ["데이터 분석 미니프로젝트", "논문/리포트 읽기", "서비스 개선 제안서"]
    },
    "ISTP": {
        "name": "현장 해결사 🛠️",
        "keywords": ["실용", "즉흥 문제해결", "도구", "분석"],
        "careers": [
            ("엔지니어/개발자 👩‍💻", "직접 만들고 고치며 배우는 환경에 강해요."),
            ("기계/전기/로봇 🤖", "장치·구조를 이해하고 개선하는 데 적합!"),
            ("응급/안전 분야 🚑", "상황 판단이 빠르고 침착함이 강점이에요."),
            ("UX 프로토타이핑 🎛️", "아이디어를 빠르게 시제품으로 구현하는 역할에 좋아요."),
        ],
        "skills": ["디버깅", "실험 설계", "툴 활용", "현장 대응"],
        "activities": ["메이커/아두이노", "해커톤 참가", "분해/조립 프로젝트"]
    },
    "ISFP": {
        "name": "감각적인 크리에이터 🎨",
        "keywords": ["감성", "미감", "자유", "경험"],
        "careers": [
            ("디자인/일러스트 🎨", "감각과 표현력이 강점! 시각·감성 전달에 좋아요."),
            ("영상/사진 📷", "순간을 포착하고 분위기를 만드는 능력이 빛나요."),
            ("브랜딩/콘텐츠 🎁", "스토리와 감성을 살린 콘텐츠에 강해요."),
            ("공연/예술 🎭", "자기 표현과 몰입이 큰 분야에 잘 맞아요."),
        ],
        "skills": ["감각적 표현", "툴(포토샵 등)", "브랜딩 감각", "관찰력"],
        "activities": ["포트폴리오 만들기", "촬영/편집 루틴", "전시/공연 리뷰 쓰기"]
    },

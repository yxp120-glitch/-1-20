import streamlit as st
import feedparser
import random

# 1. 페이지 설정
st.set_page_config(page_title="SCIENCE DAILY | 매거진", page_icon="🧬", layout="wide")

# 2. 커스텀 CSS (세련된 잡지 스타일 유지)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
    
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
    .news-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        line-height: 1.4;
        margin-bottom: 10px;
        text-decoration: none !important;
        display: block;
    }
    .news-title:hover { color: #2563eb; }
    .news-summary { color: #64748b; font-size: 0.95rem; line-height: 1.6; }
    
    /* 배너 이미지 스타일 */
    .banner-container {
        border-radius: 30px;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 뉴스 데이터 가져오기 함수
def get_news(url):
    try:
        feed = feedparser

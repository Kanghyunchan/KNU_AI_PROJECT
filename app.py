import streamlit as st
from ai_core import review_code_logic
import os

st.set_page_config(page_title="AI 코드 리뷰어", page_icon="🕵️")

st.title("🕵️ AI 시니어 개발자 코드 리뷰 에이전트")
st.write("작성한 파이썬 코드를 꼼꼼하게 분석해 드립니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("코드 입력")

    if st.button("샘플 코드 불러오기"):
        if os.path.exists("test_code.py"):
            with open("test_code.py", "r", encoding="utf-8") as f:
                st.session_state.sample_code = f.read()
    
    code_input = st.text_area("여기에 코드를 붙여넣으세요:", 
                              value=st.session_state.get('sample_code', ''), 
                              height=400)
    
    if st.button("리뷰 시작하기 🚀"):
        if code_input.strip():
            with st.spinner("AI가 분석 중입니다..."):
                st.session_state.result = review_code_logic(code_input)
        else:
            st.warning("코드를 먼저 입력해 주세요.")

with col2:
    st.subheader("리뷰 리포트")
    if 'result' in st.session_state:
        st.markdown(st.session_state.result)
        st.download_button("리포트 다운로드(.md)", st.session_state.result, "report.md")
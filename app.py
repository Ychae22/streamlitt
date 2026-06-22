import streamlit as st

st.title("건강 데이터 탐험기 👼 ✨ 🛡️")
st.write("이 앱은 당신의 건강 데이터를 파악해주고 당신을 지켜줄거에요")

name = st.text_input("이름을 입력하세요")

if name :
    st.write(f"반가워요, {name}님 ! 함께 시작해요~")
    
else:
    st.info("위에 이름을 입력하면 인사를 드릴게요")
    


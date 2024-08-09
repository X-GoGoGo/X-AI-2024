import streamlit as st
st.write("### 通过会话储存信息")
if "a" not in st.session_state:
    st.session_state.a = 0
buttonA = st.button("加1")
if buttonA:
    st.session_state.a += 1
st.write(f"{st.session_state.a}")
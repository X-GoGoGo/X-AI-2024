import streamlit as st
"## 展示各种输入组件"
username = st.text_input("请输入你的名字：")
if username:
    st.write(f"你好，{username}")
password = st.text_input("请输入你的密码：",type="password")
fword = st.text_area("请输入你的经验")
usernumble = st.number_input("请输入你的号码：",value=20,min_value=0,max_value=120,step=3)
if usernumble:
    st.write(f"你的号码是{usernumble}")
checked = st.checkbox("你是否同意条款")
if checked:
    st.write("感谢你的同意~~~")
submitted = st.button("提交")
if submitted:
    st.write("提交成功")
radio = st.radio("你的岗位是",['产品','开发','测试'],index=0) #返回一个字符串
contactA = st.selectbox("你希望的联系方式",["邮件","电话","微信"],index=1) #返回一个字符串
contactB = st.multiselect("你喜欢的水果",["apple","orange","banana"]) #返回一个列表
height = st.slider("你的身高是：",value=160,min_value=0,max_value=230,step=1)
inputfile = st.file_uploader("请上传文件",type=["jpg",'png'])
if inputfile:
    st.write(f"您的文件内容是：{inputfile.read()}")
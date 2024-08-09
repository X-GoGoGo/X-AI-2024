import streamlit as st
import pandas as pd
st.title("这是一个网站标题") #创建网站标题
st.write("## Hello,Streamlit") #创建一个文本
"你好"  #创建一个文本
# st.image('C:\phthon-相关\pythonProject2\.venv\标签-火热.png',width=50) #创建图片
st.divider() #创建分割线
df = pd.DataFrame(  #创建一个dataframe
    {
        'ID':['01','02'],
        'name':['W','A']
    }
)
st.dataframe(df) #创建交互式表
st.table(df) #创建非交互的表
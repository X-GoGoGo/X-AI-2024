import streamlit as st
import pandas as pd
st.title("这是一个网站标题") #创建网站标题
st.write("## Hello,Streamlit") #创建一个文本
"你好"  #创建一个文本
st.image('https://raw.githubusercontent.com/X-GoGoGo/X-AI-2024/main/%E6%A0%87%E7%AD%BE-%E7%81%AB%E7%83%AD.png',width=50) #创建图片
st.divider() #创建分割线
df = pd.DataFrame(  #创建一个dataframe
    {
        'ID':['01','02'],
        'name':['W','A']
    }
)
st.dataframe(df) #创建交互式表
st.table(df) #创建非交互的表
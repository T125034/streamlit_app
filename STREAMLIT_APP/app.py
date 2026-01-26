import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('人口動態調査 人口動態統計 確定数 出生')
df=pd.read_csv('FEH_00450011_260126102708.csv')

with st.sidebar:
    st.subheader('抽出条件')
    year=st.multiselect('年代を選択してください（複数選択可）',
                          df['時間軸(年次)'].unique())
    st.subheader('色分け')
    color=st.selectbox('分類を選択してください',
                       ['合計','男','女'])
    
if color == '合計':
    color_column = '出生数_総数【人】'
elif color == '男':
    color_column = '出生数_男【人】'
elif color == '女':
    color_column = '出生数_女【人】'
    
df=df[df['prod_category'].isin(year)]

st.dataframe(df,width=600,height=200)

fig=px.scatter(df,
               x='year',
               y='num',
               color=color_column,
               labels={'year': '年代', 'num': '出生数'},
               title='年代別出生数',
               trendline='ols')
st.plotly_chart(fig)
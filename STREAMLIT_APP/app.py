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
    
df=df[df['時間軸(年次)'].isin(year)]

st.dataframe(df,width=600,height=200)

df_long = df.melt(
    id_vars='時間軸(年次)',
    value_vars=['出生数_総数【人】', '出生数_男【人】', '出生数_女【人】'],
    var_name='分類',
    value_name='出生数'
)

df_long['分類'] = df_long['分類'].replace({
    '出生数_総数【人】': '合計',
    '出生数_男【人】': '男',
    '出生数_女【人】': '女'
})


fig=px.scatter(df,
               x='時間軸(年次)',
               y='出生数_総数【人】',
               color='分類',
               labels={'時間軸(年次)': '年代', '出生数_総数【人】': '出生数'},
               title='年代別出生数',
               trendline='ols')
st.plotly_chart(fig)
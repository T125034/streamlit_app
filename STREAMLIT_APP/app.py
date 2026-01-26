import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('人口動態調査 人口動態統計 確定数 出生')
df=pd.read_csv('FEH_00450011_260126102708.csv')

# 「2023年」→ 2023 に変換
df['時間軸(年次)'] = df['時間軸(年次)'].str.replace('年', '').astype(int)

# カンマ付き数値をすべて数値化
cols = ['出生数_総数【人】', '出生数_男【人】', '出生数_女【人】']
for c in cols:
    df[c] = df[c].str.replace(',', '').astype(int)


with st.sidebar:
    st.subheader('抽出条件')
    year=st.multiselect('年代を選択してください（複数選択可）',
                          df['時間軸(年次)'].unique())
    
df=df[df['時間軸(年次)'].isin(year)]

st.dataframe(df,width=600,height=200)

df['時間軸(年次)'] = pd.to_numeric(df['時間軸(年次)'], errors='coerce')

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


fig=px.scatter(df_long,
               x='時間軸(年次)',
               y='出生数',
               color='分類',
               labels={'時間軸(年次)': '年代', '出生数_総数【人】': '出生数'},
               title='年代別出生数',
               trendline='ols')
st.plotly_chart(fig)


df_bar = df.copy()
df_bar['時間軸(年次)'] = df_bar['時間軸(年次)'].astype(str)

fig_rate = px.bar(
    df,
    x='時間軸(年次)',
    y='合計特殊出生率',
    title='年代別 合計特殊出生率',
    labels={'時間軸(年次)': '年代', '合計特殊出生率': '合計特殊出生率'},
)

st.plotly_chart(fig_rate)

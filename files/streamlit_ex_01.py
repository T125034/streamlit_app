import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('広告費と売り上げ')
df=pd.read_csv('ad_expense_sales.csv')

with st.sidebar:
    st.subheader('抽出条件')
    goods=st.multiselect('製品カテゴリを選択してください（複数選択可）',
                          df['prod_category'].unique())
    ad=st.selectbox('広告媒体を1つ選択してください',
                    df['media'].unique())
    st.subheader('色分け')
    color=st.selectbox('分類を選択してください',
                       ['性別','年齢層','季節'])
    
if color == '性別':
    color_column = 'sex'
elif color == '年齢層':
    color_column = 'age'
elif color == '季節':
    color_column = 'season'
    
df=df[df['prod_category'].isin(goods)]
df=df[df['media']==ad]

st.dataframe(df,width=600,height=200)

fig=px.scatter(df,
               x='ad_expense',
               y='sales',
               color=color_column,
               labels={'ad_expense': '広告費(万円)', 'sales': '売り上げ(万円)'},
               title='広告費と売り上げ',
               trendline='ols')
st.plotly_chart(fig)
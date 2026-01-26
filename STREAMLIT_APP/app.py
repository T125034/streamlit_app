import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('人口動態調査 人口動態統計 確定数 出生')
df=pd.read_csv('FEH_00450011_260126102708.csv')

with st.sidebar:
    st.subheader('抽出条件')
    goods=st.multiselect('年代を選択してください（複数選択可）',
                          df['時間軸(年次)'].unique())
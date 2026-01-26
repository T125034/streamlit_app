import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('出入国管理統計 出入（帰）国者数（2024年）')
df=pd.read_csv('FEH_00250011_260126095056.csv')
import streamlit as st
st.title("explore the insights and visuals")
import pandas as pd 
import seaborn as sns
import plotly.express as px
df = sns.load_dataset("titanic")
st.dataframe(df)

import streamlit as st
st.title("explore the insights and visuals")
import pandas as pd 
import seaborn as sns
import plotly.express as px
df = sns.load_dataset("titanic")
st.dataframe(df)
st.sidebar.subheader("Filter Options")
gender = st.sidebar.multiselect('Gender', 
                                options = df['sex'].unique(),
                                default = df['sex'].unique())
pclass = st.sidebar.multiselect('Passenger Class', 
                                options = df['class'].unique(),)
age = st.sidebar.slider('Age', 
                        min_value=int(df['age'].min()), 
                        max_value=int(df['age'].max()), 
                        value=(int(df['age'].min()), int(df['age'].max())))

# Apply filters
filtered_df = df[
    (df['sex'].isin(gender)) & #this line checks if the gender is in the selected options
    (df['class'].isin(pclass)) & #this line checks if the class is in the selected options
    (df['pclass'].isin(pclass)) &
    (df['age'] >= age[0]) &
    (df['age'] <= age[1])
]
st.dataframe(filtered_df)
fig = px.histogram(filtered_df, x="class", y="survived", color='class', barmode='overlay',title="Age distribution by class")
st.plotly_chart(fig)

fig = px.scatter(filtered_df, x="age", y="fare", color='class', title="Age vs Fare by Class")
st.plotly_chart(fig)

fig = px.bar(filtered_df, x="class", y="survived", color='class', title="Average Fare by Class and Sex")
st.plotly_chart(fig)


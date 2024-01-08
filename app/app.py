import streamlit as st
import pandas as pd

st.title('Testing file upload/download from within Docker')


uploaded_file = st.file_uploader('Choose a .csv', type = {'csv'})

if uploaded_file is not None:
    uploaded_data = pd.read_csv(uploaded_file)

df = uploaded_data*2
st.write(df)
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report 

# Title of web application
st.markdown('''
# **Exploratory Data Analysis (Web Application)**
This application is developed by Muhammad Faizan Akram called **EDA APP** 
 # ''')

 # How to upload a file from PC?

with st.sidebar.header("Upload your dataset (.csv"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=["csv"])
    df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")

# Profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**') 
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file, Upload kar b do ab yah kam nhi lena?')
    if st.button('Press to use example data'):
        # Example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame( np.random.rand(100,5),
                              columns=['age','banana','codanics','deutchland','ear'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Profiling Report with pandas**')
        st_profile_report(pr)
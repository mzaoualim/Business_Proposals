import streamlit as st
import pandas as pd

# loading data
data = pd.read_csv('Sales_Dashboard/production_files/data.xls')

# raw data preview
st.write('json_arrays_manipulation_project/demo_app/Reviews-Array.txt')

# data manipulation
df = pd.DataFrame.from_dict(data=data.iloc[:, 0].to_dict(), orient='index')
cols = df.columns

# select cols
st.select('Select desired columns', cols)

# display selected data
st.dataframe(data, use_container_width=True)

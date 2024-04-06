import streamlit as st
import pandas as pd

# loading data
data = pd.read_json('json_arrays_manipulation_project/demo_app/Reviews-Array.txt')
# data manipulation
df = pd.DataFrame.from_dict(data=data.iloc[:, 0].to_dict(), orient='index')
cols = df.columns


def main():
  # App Title
  st.markdown("<h1 style='text-align: center;'> Script Demo </h1>", unsafe_allow_html=True)
  st.write('---')
  
  # raw data preview 
  st.markdown("<h2 style='text-align: center;'> Raw Data </h2>", unsafe_allow_html=True)
  st.write(data)
  st.write('---')

  # select cols
  col_select = st.multiselect('Select desired columns', cols)
  
  # display selected data
  submit = st.button('Get filtered Data', use_container_width=True)
  if submit:
    st.dataframe(df[col_select], use_container_width=True)
    
    # prepare to download filtered data
    csv = df[col_select].to_csv()
    st.download_button(
          label="Download filtered data",
          data=csv,
          file_name='filered.csv',
          mime='text/csv',
          use_container_width=True
        )
  st.write('---')


if __name__ == '__main__':
  main()

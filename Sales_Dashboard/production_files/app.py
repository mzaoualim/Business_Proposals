import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb

def ploter(s, f , t):
  '''
  helper function to plot sales according to
   - smoothing level
   - categorical feature of choice
   - time horizon
  '''

  # filter data according to params
  data_filter = data.copy()
    

  return fig
  
def main():
  # loading data
  st.markdown("<h1 style='text-align: center;'> Raw Data </h1>", unsafe_allow_html=True)

  data = pd.read_csv('Sales_Dashboard/production_files/data.xls')
  st.write(data)
  st.write('---')

  
  # main dashboard title
  st.write("""
        # 
        """)
  st.markdown("<h1 style='text-align: center;'> Interactive Sales Dashboard </h1>", unsafe_allow_html=True)

  st.write('---')

  # Selecting params for visualizations
  # smoothing level
  st.markdown("<h2 style='text-align: center;'> Smoothing the sales </h2>", unsafe_allow_html=True)
  
  smooth = st.slider('Smoothing level', min_value=0, max_value=90, value=30, step=1)
  st.write(smooth)
  st.write('---')

  # features vs time horizon
  st.markdown("<h2 style='text-align: center;'> Features vs Time Horizon Sales Analysis </h2>", unsafe_allow_html=True)

  col1, col2 = st.columns(2)
  with col1:
          feat_list = data.select_dtypes(include='object')
          features = st.selectbox('Features:', feat_list)

  with col2:
          time_horizon = st.selectbox('Time Horizon', ('Hours', 'Days', 'Weeks', 'Months'))

  submit = st.button('Analyse the Data', use_container_width=True)
  st.write('---')

  fig = ploter(smooth, features, time_horizon)
  st.pyplot(fig, use_container_width=True)
  # Customer Satisfaction
  st.markdown("<h2 style='text-align: center;'> Rating </h2>", unsafe_allow_html=True)
  





if __name__ == '__main__':
  main()

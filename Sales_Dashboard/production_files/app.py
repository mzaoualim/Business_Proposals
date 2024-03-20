import streamlit as st
from streamlit_star_rating import st_star_rating
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb
from hepler_functions import ploter, data_prep

  
def main():
  # raw data overview
  st.markdown("<h1 style='text-align: center;'> Raw Data </h1>", unsafe_allow_html=True)

  # loading data
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
  
  smooth = st.slider('Smoothing level', min_value=1, max_value=90, value=30, step=1)
  # st.write(smooth)
  st.write('---')

  # features vs time horizon
  st.markdown("<h2 style='text-align: center;'> Features vs Time Horizon Sales Analysis </h2>", unsafe_allow_html=True)

  col1, col2, col3 = st.columns(3)
  with col1:
          feat_list = ['City', 'Customer type', 'Gender', 'Product line', 'Payment']
          features = st.selectbox('Features:', feat_list)
  
  with col2:
          Sub_features = st.selectbox('Sub features:', data[features].unique())

  with col3:
          time_horizon = st.selectbox('Time Horizon', ('Working hours', 'Days of Week', 'Weeks', 'Days of Month','Months'))

  submit = st.button('Analyse the Data', use_container_width=True)

  if submit:
    fig, stars = ploter(smooth, features, Sub_features, time_horizon)
    st.pyplot(fig)
    
    st.write('---')

    # Customer Satisfaction
    st.markdown("<h2 style='text-align: center;'> Customer Satisfaction Rating </h2>", unsafe_allow_html=True)
  
    star = st_star_rating('', 10, stars, 60, None, None, None, 
                          None, None, None, None)
    





if __name__ == '__main__':
  main()

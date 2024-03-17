import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb

# def ploter(s, f, sf, t):
#   '''
#   helper function to plot sales according to
#    - smoothing level
#    - categorical feature of choice
#    - time horizon
#   '''

#   fig, ax = plt.subplot()
#   filterd_data = data.where(data.f == sf).groupby(data['DateTime'].dt.t).agg(['min', 'mean', 'median', 'max'])
#   ax = filterd_data['Total'].plot(kind='barh')
#   plt.set_x
#   plt.set_y
#   plt.set_title()
#   return fig
  
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

  col1, col2, col3 = st.columns(3)
  with col1:
          feat_list = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
          features = st.selectbox('Features:', feat_list)
  
  with col2:
          Sub_features = st.selectbox('Sub_features:', data[features].unique())

  with col3:
          time_horizon = st.selectbox('Time Horizon', ('Hours', 'Days', 'Weeks', 'Months'))

  submit = st.button('Analyse the Data', use_container_width=True)

  if submit:
    data.where(data.Branch == 'A').groupby(data['DateTime']\
                                       .dt.day_of_week).agg(['min', 'mean', 'median', 'max'])\
                                        ['Total'].plot(kind='bar', 
                                                       figsize=(10, 5),
                                                       stacked=True)
  st.write('---')

  # fig = ploter(smooth, features, time_horizon)
  # st.pyplot(fig, use_container_width=True)
  # Customer Satisfaction
  st.markdown("<h2 style='text-align: center;'> Rating </h2>", unsafe_allow_html=True)
  





if __name__ == '__main__':
  main()

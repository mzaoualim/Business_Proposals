import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb

def data_prep(data):
  '''
  preprocessing raw data
  '''
  
  clean_data = data[['City', 'Customer type', 'Gender', 'Product line', 'Total', 'Date', 'Time', 'Payment', 'Rating']].copy()
  clean_data['DateTime'] = clean_data['Date']+ 'T' +clean_data['Time']
  clean_data['DateTime'] = pd.to_datetime(clean_data['DateTime'])
  clean_data.drop(columns=['Date', 'Time'], inplace=True)
  clean_data['Rating'] = clean_data['Rating'].round(0)
  clean_data = clean_data.set_index('DateTime').sort_index()
  
  return clean_data
  
def ploter(smooth, feat, sub_feat, time_horizon):
  '''
  helper function to plot sales according to
   - smoothing level
   - categorical feature & sub feature of choice
   - time horizon
  '''

  dataset = data_prep(data)
  dataset['Total Sales'] = dataset['Total'].rolling(smooth).mean()
  dataset.dropna(inplace=True)

  time_dict = {
  'Hours': dataset.index.hour,
  'Days': dataset.index.dayofweek,
  'Weeks': dataset.index.week,
  'Months': dataset.index.month
            }

  fig, ax = plt.subplots()
  y = dataset.groupby(time_dict[time_horizon]).agg('mean')['Total Sales']
  bars = ax.bar(y, align='center')
  ax.bar_label(hbars, fmt='%.2f')
  ax.set_xlim(right=15)  # adjust xlim to fit labels
  
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
    fig = ploter(smooth, feat, sub_feat, time_horizon)
    st.pyplot(fig)
    
  st.write('---')

  # fig = ploter(smooth, features, time_horizon)
  # st.pyplot(fig, use_container_width=True)
  # Customer Satisfaction
  st.markdown("<h2 style='text-align: center;'> Customer Satisfaction Rating </h2>", unsafe_allow_html=True)
  





if __name__ == '__main__':
  main()

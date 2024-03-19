import streamlit as st
from streamlit_star_rating import st_star_rating
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb

# loading data
data = pd.read_csv('Sales_Dashboard/production_files/data.xls')


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
  'Working hours': dataset.index.hour,
  'Days of Week': dataset.index.dayofweek,
  'Weeks': dataset.index.isocalendar().week,
  'Months': dataset.index.month
            }

  fig, ax = plt.subplots()
  ax = dataset.where(dataset[feat] == sub_feat).groupby(time_dict[time_horizon]).mean(numeric_only=True)['Total Sales'].plot()
  stars = dataset.where(dataset[feat] == sub_feat).groupby(time_dict[time_horizon]).mean(numeric_only=True)['Rating'].mean().round(0) 
  ax.set_xlabel(time_horizon)
  ax.set_ylabel('Sales')
  ax.set_title('Mean Sales by %s %s over the %s' %(feat, sub_feat, time_horizon))  
  return fig, stars
  
def main():
  # raw data overview
  st.markdown("<h1 style='text-align: center;'> Raw Data </h1>", unsafe_allow_html=True)

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
          feat_list = ['City', 'Customer type', 'Gender', 'Product line', 'Payment']
          features = st.selectbox('Features:', feat_list)
  
  with col2:
          Sub_features = st.selectbox('Sub features:', data[features].unique())

  with col3:
          time_horizon = st.selectbox('Time Horizon', ('Working hours', 'Days of Week', 'Weeks', 'Months'))

  submit = st.button('Analyse the Data', use_container_width=True)

  if submit:
    fig, stars = ploter(smooth, features, Sub_features, time_horizon)
    st.pyplot(fig)
    
  st.write('---')

  # fig = ploter(smooth, features, time_horizon)
  # st.pyplot(fig, use_container_width=True)
  # Customer Satisfaction
  st.markdown("<h2 style='text-align: center;'> Customer Satisfaction Rating </h2>", unsafe_allow_html=True)
  satisf = st.button('Satisfied?', use_container_width=True)
  if satisf:

    star = st_star_rating('', amount_of_stars=stars,
    default_value=5, size=100, 
    emoticons=False, read_only=True, 
    dark_theme=True, resetButton=False, 
    resetLabel=False,
    customCSS=False, on_click=None)

    st.write(star)





if __name__ == '__main__':
  main()

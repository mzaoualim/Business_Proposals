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
  'Working hours': dataset.index.hour,
  'Days of Week': dataset.index.dayofweek,
  'Weeks': dataset.index.isocalendar().week,
  'Days of Month': dataset.index.day,
  'Months': dataset.index.month
            }

  fig, ax = plt.subplots()
  ax = dataset.where(dataset[feat] == sub_feat).groupby(time_dict[time_horizon]).mean(numeric_only=True)['Total Sales'].plot()
  stars = dataset.where(dataset[feat] == sub_feat).groupby(time_dict[time_horizon]).mean(numeric_only=True)['Rating'].mean().round(0) 
  ax.set_xlabel(time_horizon)
  ax.set_ylabel('Sales')
  ax.set_title('Mean Sales by %s %s over the %s' %(sub_feat, feat, time_horizon))  
  return fig, stars

# loading data
data = pd.read_csv('Sales_Dashboard/production_files/data.xls')  
import streamlit as st
import pandas as pd
import numpy as np
#import re

#----------------------------------------------------------------------
# Inputs to function

# dictionnary of city codes
city = {
    'Aachen': 1,
    'Augsburg': 2,
    'Baden-Baden': 3,
    'Bad Tölz': 4,
    'Bamberg': 5,
    'Bayreuth': 6,
    'Bergisch Gladbach': 7,
    'Berlin': 8,
        }

# dictionnary of home types by code
home = {
    'Flatshares': 0,
    '1 Room Flats': 1,
    'Flats': 2,
    'Houses': 3
    }
#----------------------------------------------------------------------
def scraper(city_name:str, home_type:str):
  '''
  starter function to retrieve latest rental listing from wg-gesucht.de website
  takes as input city_name and home_type
  return dataframe of available and latest max 20 listed rentals
  '''
  #default link
  link = 'https://www.wg-gesucht.de/en/wohnungen-in-Berlin.%d.%d.0.0.html' %(city[city_name], home[home_type])

  # raw results
  result = pd.read_html(link)
  # preprocessing

  ## select columns and drop empty rows
  if home_type == '1 Room Flats':
      result = result[0][['Published', 'Rent', 'Size', 'District']].dropna()
  else:
      result = result[0][['Rooms', 'Published', 'Rent', 'Size', 'District']].dropna()
  ## drop ads rows
  # result = result[result["District"].str.contains(re.escape("*")) == False]
  result[result["District"].str.contains('from') == False]
  ## reset index
  result.reset_index(drop=True, inplace=True)

  return result
#----------------------------------------------------------------------

def main():
  # raw data overview
  st.markdown("<h1 style='text-align: center;'> Rental listings from wg-gesucht.de </h1>", unsafe_allow_html=True)
  st.write('---')


  # loading data
  st.markdown("<h2 style='text-align: center;'> Select City and Rental Type </h2>", unsafe_allow_html=True)

  col1, col2 = st.columns(2)
  with col1:
          cities = [c for c in city.keys()]
          city_ = st.selectbox('City:', cities)

  with col2:
          rentals = [r for r in home.keys()]
          types = st.selectbox('Rental Types:', rentals)

  submit = st.button('Get latest listings', use_container_width=True)

  if submit:
      st.dataframe(scraper(city_, types), use_container_width=True)
      
  st.write('---')


if __name__ == '__main__':
  main()
















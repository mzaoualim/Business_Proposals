import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sb

def main():
  # main dashboard title
  st.write("""
        # 
        """)
  st.markdown("<h1 style='text-align: center;'> Interactive Sales Dashboard </h1>", unsafe_allow_html=True)

  st.write('---')

  # Selecting params for visualizations
  # smoothing level
  st.markdown("<h2 style='text-align: center;'> Smoothing the sales </h2>", unsafe_allow_html=True)
  
  smooth = st.slider(label, min_value=0, max_value=90, value=30, step=1)
  st.write(smooth)
  





if __name__ == '__main__':
  main()

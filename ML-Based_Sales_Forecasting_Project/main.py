        
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

from prophet import Prophet
from prophet.serialize import model_from_json




def main():
        st.write("""
        # 
        """)
        st.markdown("<h1 style='text-align: center;'> Sales Forcaster </h1>", unsafe_allow_html=True)

        st.write('---')

        st.markdown("<h2 style='text-align: center;'> Demographic based EDA </h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
                Demographic_Feature = st.selectbox('Demographic Feature:', ('Age Groups', 'Gender'))

        with col2:
                Sales_Features = st.selectbox('Sales Features:', ('Total Amount', 'Quantity'))

        submit = st.button('Analyse the Data', use_container_width=True)

        if submit:
                data = pd.read_csv('ML-Based_Sales_Forecasting_Project/retail_sales_dataset.csv')
                data['Age Groups'] = pd.cut(data['Age'], bins=[0, 25, 65, 100], labels=['Young', 'Middle Aged', 'Seniors'])
        
                # ploting
                # Generate plots
        
                plt.figure(figsize=(10, 6))
                fig, ax = plt.subplots()
                
                if Demographic_Feature == 'Age':
                    if Sales_Features == 'Total Amount':
                        plt.title('Total Sales by Age Groups')
                    else:
                        plt.title('Quantity Sales by Age Groups')
                else:
                    if Sales_Features == 'Total Amount':
                        plt.title('Total Sales by Gender')
                    else:
                        plt.title('Quantity Sales by Gender')
        
                ax = sn.histplot(data=data, x=Sales_Features , hue = Demographic_Feature, bins=4)
                plt.ylabel('Frequency')
                st.pyplot(fig, use_container_width=True)
        st.write('---')
        st.markdown("<h2 style='text-align: center;'> Sample Sales Predictions vs Actuals </h2>", unsafe_allow_html=True)
        
        predict = st.button('Predict', use_container_width=True)
        if predict:
                with open(f'ML-Based_Sales_Forecasting_Project/fbprophet_model.json', 'r') as f:
                        model = model_from_json(f.read())
                        
                data_test = pd.read_csv('ML-Based_Sales_Forecasting_Project/data_test')
                data_test['ds'] = pd.to_datetime(data_test['ds'])
                        
                preds = model.predict(data_test)
                
                plt.figure(figsize=(10, 6))
                fig, ax = plt.subplots()
                ax1 = sn.lineplot(data=data_test, x=data_test['ds'], y=data_test['y'])
                ax2 = sn.lineplot(data=preds, x=preds['ds'], y=preds['yhat'])
                ax1.set_ylabel('Total Sales', rotation=90)
                ax1.set_xlabel('Date', rotation=0)
                fig.autofmt_xdate()
                plt.show()
                
                plt.title('Predicted vs Actuals')
                st.pyplot(fig, use_container_width=True)

        st.write('---')
        st.markdown("<h2 style='text-align: center;'> Future Sales Forcasting </h2>", unsafe_allow_html=True)

        with open(f'ML-Based_Sales_Forecasting_Project/fbp_model_future.json', 'r') as f:
                model_future = model_from_json(f.read())
        
        a, b = st.columns(2)
        with a:
            freqq = st.selectbox('Trying to predict next', ('days', 'weeks', 'months'))
        with b:
            periodss = st.number_input("Forcasting Horizon", value=0, placeholder="Numbers of days or weeks...")
        
        future = st.button('Back to the future', use_container_width=True)
        if future:
                if freqq == 'days':
                   futures = model_future.make_future_dataframe(periods=periodss, freq='D', include_history=False)
                elif freqq == 'weeks':
                   futures = model_future.make_future_dataframe(periods=periodss, freq='D', include_history=False)
                else:
                   futures = model_future.make_future_dataframe(periods=periodss, freq='M', include_history=False)

                fcst = model_future.predict(futures)
                fig = model_future.plot(fcst)
                plt.xlabel('Dates')
                plt.ylabel('Predicted Total Sales')
                st.pyplot(fig, use_container_width=True)
                        
















if __name__ == "__main__":
    main()

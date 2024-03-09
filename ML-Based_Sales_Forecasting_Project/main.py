
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

from prophet import Prophet
# from prophet.serialize import model_from_json

st.set_option('deprecation.showPyplotGlobalUse', False)





def main():
        st.write("""
        # 
        """)
        st.markdown("<h1 style='text-align: center;'> Sales Forcaster </h1>", unsafe_allow_html=True)

        st.write('---')

        st.markdown("<h2 style='text-align: center;'> Demographic based EDA </h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
                Demographic_Feature = st.selectbox('Demographic Feature:', ('Age_group', 'Gender'))

        with col2:
                Sales_Features = st.selectbox('Sales Features:', ('Total Amount', 'Quantity'))

        
        data = pd.read_csv('/retail_sales_dataset.csv')
        data['Age_group'] = pd.cut(data['Age'], bins=[0, 25, 65, 100], labels=['Young', 'Middle_Aged', 'Seniors'])

        # ploting
        # Generate plots

        plt.figure(figsize=(10, 6))
        sn.histplot(data=data, x=Sales_Features , hue = Demographic_Feature, kde=True, bins=4, common_norm=True)
        
        if Sales_Features == 'Total Amount':
            plt.xlabel('Total Sales')
        else:
             plt.xlabel('Quantity Sales')

        plt.ylabel('Frequency')

        if Demographic_Feature == 'Age':
            if Sales_Features == 'Total Amount':
                plt.title('Total Sales by Age_group')
            else:
                plt.title('Quantity Sales by Age_group')
        else:
            if Sales_Features == 'Total Amount':
                plt.title('Total Sales by Gender')
            else:
                plt.title('Quantity Sales by Gender')

        st.pyplot(use_container_width=True)

        st.write('---')

        st.markdown("<h2 style='text-align: center;'> Sales Predictions vs Actuals </h2>", unsafe_allow_html=True)
        
        best_params = {'changepoint_prior_scale': 9.997445406286284,
                    'changepoint_range': 0.7457189514230351,
                    'seasonality_prior_scale': 1.2645281821240346,
                    'holidays_prior_scale': 6.233667468012274,
                    'seasonality_mode': 'multiplicative',
                    'growth': 'logistic',
                    'weekly_seasonality': 40,
                    'yearly_seasonality': 3
                    }
        
        model = Prophet(**best_params)
        data_train = pd.read_csv('/data_train')
        data_test = pd.read_csv('/data_test')
        model.fit(data_train)
        preds = model.predict(data_test)

        plt.plot(data_test['y'].values, color='blue')
        plt.plot(preds['yhat'].values, color='red')
        plt.title('Predicted vs Actuals')
        st.pyplot(use_container_width=True)

        st.write('---')

        st.markdown("<h2 style='text-align: center;'> Future Sales Forcasting </h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            freqq = st.selectbox('Trying to predict next', ('days', 'weeks'))
        with col2:
            periodss = st.number_input('How many days/weeks are you trying to forcast?')

        if freqq == 'days':
            future = model.make_future_dataframe(periods=periodss, freq='D')
        else:
            future = model.make_future_dataframe(periods=periodss, freq='D')

        fcst = model.predict(future)
        fig = model.plot(fcst)

        st.pyplot(use_container_width=True)
















if __name__ == "__main__":
    main()

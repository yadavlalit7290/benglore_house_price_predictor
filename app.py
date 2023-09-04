import streamlit as st
import pandas as pd
import numpy as np
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df1 = pickle.load(open('df.pkl','rb'))

st.title('Banglore House Price Predictor')


location = st.selectbox('Select the location',df1['location'].unique())

total_sqft = st.number_input('Enter the total square feet',min_value=0.0)

bath = st.number_input('Enter the number of bathrooms',min_value=0)

bhk = st.number_input('Enter the number of BHK',min_value=0)

if st.button('Predict Price'):
    result = pipe.predict([[location,total_sqft,bath,bhk]])
    if result[0]<0:
        st.error('Sorry, your inputs are wrong')
    else:
        st.subheader('Price is' + ' ' + 'Rs' + ' ' + str(np.round(result[0], 2))+' '+'lakh' )
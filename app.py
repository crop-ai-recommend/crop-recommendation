import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('crop_model.pkl', 'rb'))

st.title('🌾 AI Crop Recommendation System')
st.write('Enter the soil and climate details below:')

N = st.number_input('Nitrogen (N)', min_value=0, max_value=200)
P = st.number_input('Phosphorus (P)', min_value=0, max_value=200)
K = st.number_input('Potassium (K)', min_value=0, max_value=200)
temperature = st.number_input('Temperature (°C)', min_value=0.0, max_value=50.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0)
ph = st.number_input('pH Level', min_value=0.0, max_value=14.0)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=500.0)

if st.button('🌱 Recommend Crop'):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f'Recommended Crop: {prediction[0]} 🌾')

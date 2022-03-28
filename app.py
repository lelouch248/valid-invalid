import streamlit as st
import joblib
model = joblib.load('valid-invalid')
st.title('valid invalid Classifier')            
ip = st.text_input('Enter your message')       
op = model.predict([ip])           
if st.button('Predict'):   
  st.title(op[0]) 
  

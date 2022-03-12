import streamlit as st
import pandas as pd
import pickle
import numpy as np


@st.cache(allow_output_mutation=True)
def prep_stage():
    print("Cache load")

prep_stage()


st.write("""
# Cat Prediction App!
This app predicts the probability 
""")



IndoorTemp = st.sidebar.slider('Indoor Temp C', 10.0 , 35.0, 22.0)
HourOfDay = st.sidebar.slider('Hour of day', 0 , 23, 8)

# print(HourOfDay)

st.write('IndoorTemp {}.'.format(IndoorTemp))
st.write('HourOfDay {}.'.format(HourOfDay))


data = {'indoor_temp':[IndoorTemp], 
        'hr_of_day':[HourOfDay],}
    
features = pd.DataFrame(data)
# print (features)

# Reads in saved classification model
load_clf = pickle.load(open('../notebooks/cat_predictor_simple_clf.pkl', 'rb'))

df = features

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
churn_labels = np.array(['Somewhere else','Nicho room'])
st.write(churn_labels[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
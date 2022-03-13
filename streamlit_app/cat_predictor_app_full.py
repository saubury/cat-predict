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



IndoorTemp = st.sidebar.slider('Indoor Temp C', 10 , 35, 22)
OutdoorTemp = st.sidebar.slider('Outdoor Temp C', 10 , 35, 22)
HourOfDay = st.sidebar.slider('Hour of day', 0 , 23, 8)
DayOfWeek = st.sidebar.slider('Day of week', 0 , 6, 0)
IsRaining = st.sidebar.selectbox('Raining',('True', 'False'))


# print(HourOfDay)

st.write('IndoorTemp {}.'.format(IndoorTemp))
st.write('HourOfDay {}.'.format(HourOfDay))


# data = {'indoor_temp':[IndoorTemp], 
#         'hr_of_day':[HourOfDay],}
    
# features = pd.DataFrame(data)
# print (features)

# Try a prediction
data = {'indoor_temp':[IndoorTemp], 
        'outside_temp':[OutdoorTemp], 
        'hr_of_day':[HourOfDay], 
        'day_of_week':[DayOfWeek], 
        'is_raining':[IsRaining=='True'],}
pdf = pd.DataFrame(data)

# Reads in saved classification model
load_clf = pickle.load(open('../notebooks/cat_predictor_full_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(pdf)
prediction_proba = load_clf.predict_proba(pdf)


st.subheader('Prediction')
# churn_labels = np.array(['Somewhere else','Nicho room'])
st.write(prediction[0])

st.subheader('Prediction Probability')
st.write(prediction_proba)
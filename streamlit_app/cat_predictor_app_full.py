import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image

# Settings
daysList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', ]
labelsList = ['bedroom', 'dining', 'lounge', 'nicholas', 'outside', 'study', 'winter_garden', ]

@st.cache(allow_output_mutation=True)
def prepClassification():
    ret = pickle.load(open('../notebooks/cat_predictor_full_clf.pkl', 'rb'))
    print("Classification loaded")
    return ret

@st.cache(allow_output_mutation=True)
def prepImageData():
    imageData = []
    for i in labelsList:
        # print(i)
        imageFileName = './images/{}.jpg'.format(i)
        image = Image.open(imageFileName)  
        imageData.append(image)
    print("Images loaded")
    return imageData

# Reads in saved classification model
load_clf = prepClassification()
load_image = prepImageData()

# Main page render
st.write("""
# Cat Prediction App!
This app predicts the probability 
""")


IndoorTemp = st.sidebar.slider('Indoor Temp C', 10 , 35, 22)
OutdoorTemp = st.sidebar.slider('Outdoor Temp C', 10 , 35, 22)
HourOfDay = st.sidebar.slider('Hour of day', 0 , 23, 8)
DayOfWeek = st.sidebar.selectbox('Day Of Week', daysList)
IsRaining = st.sidebar.selectbox('Raining',('True', 'False'))

# Try a prediction
data = {'indoor_temp':[IndoorTemp], 
        'outside_temp':[OutdoorTemp], 
        'hr_of_day':[HourOfDay], 
        'day_of_week':[daysList.index(DayOfWeek)], 
        'is_raining':[IsRaining=='True'],}
pdf = pd.DataFrame(data)


# Apply model to make predictions
prediction = load_clf.predict(pdf)
prediction_proba = load_clf.predict_proba(pdf)
predictionText = load_clf.predict(pdf)[0]

# Write text prediction
st.subheader('Prediction')
st.write('Prediction : **{}**'.format(predictionText))

# Update image prediction
image = load_image[labelsList.index(predictionText)]
st.image(image)


# st.subheader('Prediction Probability')
# st.write(prediction_proba)
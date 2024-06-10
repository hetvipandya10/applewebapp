import streamlit as st

st.title("Welcome to apple App")
from PIL import Image
img = Image.open("apple quality.jpg")

st.image(img, width=200)

S=st.slider("Select size=",-7.1,6.4)
W=st.slider("Select wieght=",--7.1,5.7)
SW=st.slider("Select sweetness=",-6.8,6.3)
C=st.slider("Select cruchiness=",-6.0,7.6)
J=st.slider("Select juiciness=",-5.9,7.3)
R=st.slider("Select Ripeness=",-5.8,7.2)
A=st.slider("Select Acidity=",-7.0,7.4)

import pickle
model=pickle.load(open("Apple.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[S,W,SW,C,J,R,A]])
    st.success("The Apple Quality is "+ prd[0])


import streamlit as st
import requests
import os

# Default to localhost if not specified
API_URL = "https://deployable-ml-model.onrender.com/predict"

st.title("Insurance Premium Category Predictor")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        # We use the 'json' parameter so 'requests' sets the Content-Type header automatically
        response = requests.post(API_URL, json=input_data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if "response" in result:
                prediction = result["response"]
                st.success(f"Predicted Category: **{prediction['predicted_category']}**")
                st.info(f"Confidence: {prediction['confidence']}")
                
                with st.expander("Show Details"):
                    st.write(prediction)
            else:
                st.error("Key 'response' not found in API result.")
                st.json(result)
        else:
            st.error(f"API Error! Status: {response.status_code}")
            try:
                st.json(response.json())
            except:
                st.text(response.text)

    except requests.exceptions.ConnectionError:
        st.error(f"❌ Connection Refused. Ensure the API is running at: {API_URL}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
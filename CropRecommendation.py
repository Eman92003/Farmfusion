import streamlit as st
import pandas as pd
import pickle  # Assuming the trained model is saved as a pickle file

# Load the trained model
model_path = 'C:/Users/Eman Yaser/Downloads/Project/Project/CropPrediction.sav'  # Replace with your model's path
with open(model_path, 'rb') as file:
    model = pickle.load(file)

scaler_path = 'C:/Users/Eman Yaser/Downloads/Project/Project/MinMaxScaler.sav'  # Replace with your scaler's path
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

# App Title
st.title("🌱 Crop Recommendation System")
st.write("This app recommends the best crop to grow based on soil and environmental conditions.")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")

def user_inputs():
    st.sidebar.write("Enter the following parameters:")
    try:
        Nitrogen = float(st.sidebar.text_input("Nitrogen Content (N)", value="70"))
        Phosphorus = float(st.sidebar.text_input("Phosphorus Content (P)", value="40"))
        Potassium = float(st.sidebar.text_input("Potassium Content (K)", value="40"))
        Temperature = float(st.sidebar.text_input("Temperature (°C)", value="25"))
        Humidity = float(st.sidebar.text_input("Humidity (%)", value="50"))
        pH_Value = float(st.sidebar.text_input("pH Level", value="7"))
        Rainfall = float(st.sidebar.text_input("Rainfall (mm)", value="100"))
    except ValueError:
        st.error("Please enter valid numerical values for all fields.")
        return None

    return pd.DataFrame({
        'Nitrogen': [Nitrogen],
        'Phosphorus': [Phosphorus],
        'Potassium': [Potassium],
        'Temperature': [Temperature],
        'Humidity': [Humidity],
        'pH_Value': [pH_Value],
        'Rainfall': [Rainfall]
    })

# Collect user inputs
input_data = user_inputs()

if input_data is not None:
    # Display user inputs
    st.subheader("Your Input Parameters")
    st.write(input_data)

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Crop mapping
    crops = [
        'Rice', 'Maize', 'Chickpea', 'Kidney Beans', 'Pigeon Peas', 'Moth Beans',
        'Mung Bean', 'Blackgram', 'Lentil', 'Pomegranate', 'Banana', 'Mango', 'Grapes',
        'Watermelon', 'Muskmelon', 'Apple', 'Orange', 'Papaya', 'Coconut', 'Cotton',
        'Jute', 'Coffee'
    ]
    encoded_crops = [
        20, 11, 3, 9, 18, 13, 14, 2, 10, 19, 1, 12, 7, 21, 15, 0, 16,
        17, 4, 6, 8, 5
    ]
    crop_mapping = {encoded_crops[i]: crops[i] for i in range(len(crops))}

    # Prediction
    if st.button("Predict Crop"):
        prediction = model.predict(input_data_scaled)
        result = prediction[0]
        recommended_crop = crop_mapping.get(result, "Unknown Crop")
        st.subheader("Recommended Crop")
        st.write(f" {recommended_crop}")

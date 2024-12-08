# Farm Fusion: Crop Recommendation System

*Farm Fusion* is an intelligent crop recommendation system designed to help farmers make better planting decisions based on key environmental and soil factors. The system takes input such as nitrogen, phosphorus, potassium levels, and environmental factors (temperature, humidity, pH, and rainfall) to recommend the most suitable crops for planting. The model was trained using a dataset of 2200 entries with information on various crops.

### *Project Overview*

The system utilizes machine learning techniques to predict the most appropriate crop to grow based on the following inputs:
- *Soil Conditions*: Nitrogen (N), Phosphorus (P), Potassium (K)
- *Environmental Factors*: Temperature, Humidity, pH Value, Rainfall

The dataset includes data for a variety of crops, including:
- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Moth Beans
- Mung Bean
- Blackgram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

### *Machine Learning Models Tested*

The following machine learning algorithms were tested to predict the best crop to grow:
1. *Naive Bayes*
2. *Decision Tree*
3. *K-Nearest Neighbors (KNN)*
4. *Logistic Regression*
5. *AdaBoost*

### *Best Model*
After testing the models, *Naive Bayes* achieved the highest accuracy of *99.48%*, making it the selected model for deployment in this crop recommendation system.

### *Streamlit Deployment*

The application has been deployed using *Streamlit*. To run the application, follow these steps:

1. Launch the Streamlit app:
   ```bash
   streamlit run CropRecommendation.py
This will open the app in your default web browser, allowing you to input values for the following features:

- *Nitrogen (N)*
- *Phosphorus (P)*
- *Potassium (K)*
- *Temperature (°C)*
- *Humidity (%)*
- *pH Value*
- *Rainfall (mm)*

Click on the *"Predict Crop"* button to receive a crop recommendation based on the entered data.

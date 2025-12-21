import streamlit as st
import joblib
import pandas as pd

# Load the model (Updated to match your actual filename)
model = joblib.load('titanic_survival_model.pkl')

st.title("🚢 Titanic Survival Predictor")
st.write("Enter the details of the passenger to predict survival.")

# --- INPUT FIELDS ---
pclass = st.selectbox('Passenger Class', [1, 2, 3], format_func=lambda x: f"{x}st Class")
sex = st.selectbox('Sex', ["Male", "Female"])
age = st.slider('Age', 0, 100, 30)
sibsp = st.number_input('Siblings/Spouses Aboard', 0, 10, 0)
parch = st.number_input('Parents/Children Aboard', 0, 10, 0)
fare = st.number_input('Fare Price (£)', 0.0, 512.0, 32.0)
embarked = st.selectbox('Port of Embarkation', ["Southampton (S)", "Cherbourg (C)", "Queenstown (Q)"])

# --- PRE-PROCESSING ---
if st.button('Predict Survival'):
    # 1. Calculate Derived Features
    family_size = sibsp + parch + 1
    is_alone = 1 if family_size == 1 else 0

    # 2. Encode Categorical Variables
    sex_encoded = 1 if sex == "Female" else 0
    
    embarked_q = 1 if "Queenstown" in embarked else 0
    embarked_s = 1 if "Southampton" in embarked else 0

    # 3. Create DataFrame
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex_encoded],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'FamilySize': [family_size],
        'IsAlone': [is_alone],
        'Embarked_Q': [embarked_q],
        'Embarked_S': [embarked_s]
    })

    # 4. Predict
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success(f"Prediction: Survived! 🟢")
    else:
        st.error(f"Prediction: Did Not Survive 🔴")
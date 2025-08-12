# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model
try:
    model = joblib.load('liver_cirrhosis_model.pkl')
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Streamlit app
st.title('Liver Cirrhosis Stage Detection')
st.write("""
This app predicts the stage of liver cirrhosis based on patient data.
The model uses a Random Forest classifier trained on Mayo Clinic data.
""")

# Input form
st.header('Patient Information')
with st.form("patient_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        drug = st.selectbox('Drug', ['D-penicillamine', 'Placebo'])
        sex = st.radio('Sex', ['Male', 'Female'])
        ascites = st.radio('Ascites', ['No', 'Yes'])
        hepatomegaly = st.radio('Hepatomegaly', ['No', 'Yes'])
        spiders = st.radio('Spiders', ['No', 'Yes'])
        
    with col2:
        edema = st.select_slider('Edema', options=['No edema', 'Edema without diuretics', 'Edema with diuretics'])
        age = st.number_input('Age (days)', min_value=0, max_value=40000, value=18000)
        bilirubin = st.number_input('Bilirubin (mg/dl)', min_value=0.0, value=1.5, step=0.1)
        cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=0, value=200)
        albumin = st.number_input('Albumin (gm/dl)', min_value=0.0, value=3.5, step=0.1)
        
    col3, col4 = st.columns(2)
    with col3:
        copper = st.number_input('Copper (ug/day)', min_value=0, value=50)
        alk_phos = st.number_input('Alkaline Phosphatase (U/liter)', min_value=0, value=100)
        sgot = st.number_input('SGOT (U/ml)', min_value=0, value=40)
        
    with col4:
        triglycerides = st.number_input('Triglycerides (mg/dl)', min_value=0, value=100)
        platelets = st.number_input('Platelets (per ml/1000)', min_value=0, value=200)
        prothrombin = st.number_input('Prothrombin Time (seconds)', min_value=0.0, value=11.0, step=0.1)
    
    submit_button = st.form_submit_button("Predict Stage")

# Process form submission
if submit_button:
    # Map inputs to model format
    input_data = {
        'Drug': 'D-penicillamine' if drug == 'D-penicillamine' else 'Placebo',
        'Sex': 'M' if sex == 'Male' else 'F',
        'Ascites': 'Y' if ascites == 'Yes' else 'N',
        'Hepatomegaly': 'Y' if hepatomegaly == 'Yes' else 'N',
        'Spiders': 'Y' if spiders == 'Yes' else 'N',
        'Edema': 'N' if edema == 'No edema' else ('S' if edema == 'Edema without diuretics' else 'Y'),
        'Age': age,
        'Bilirubin': bilirubin,
        'Cholesterol': cholesterol,
        'Albumin': albumin,
        'Copper': copper,
        'Alk_Phos': alk_phos,
        'SGOT': sgot,
        'Triglycerides': triglycerides,
        'Platelets': platelets,
        'Prothrombin': prothrombin
    }
    
    # Create input DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    try:
        prediction = model.predict(input_df)
        stage = prediction[0]
        
        st.subheader(f'Predicted Stage: {stage}')
        
        # Stage interpretation
        stage_info = {
            1: 'Stage 1: Mild fibrosis (early stage)',
            2: 'Stage 2: Moderate fibrosis',
            3: 'Stage 3: Cirrhosis (advanced scarring)'
        }
        st.info(f'**Interpretation:** {stage_info.get(stage, "Unknown stage")}')
        
        # Show input data
        st.subheader('Input Data Summary')
        st.dataframe(input_df)
        
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# Add sidebar information
st.sidebar.header("About")
st.sidebar.info("""
This predictive model uses data from the Mayo Clinic trial on primary biliary cirrhosis (1974-1984).

**Stage Definitions:**
- Stage 1: Mild fibrosis
- Stage 2: Moderate fibrosis
- Stage 3: Cirrhosis (advanced scarring)
""")
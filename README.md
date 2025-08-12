# Liver Cirrhosis Stage Prediction

A machine learning project that predicts the stage of liver cirrhosis based on patient clinical data using a Random Forest classifier. The project includes both a Jupyter notebook for model training and a Streamlit web application for interactive predictions.

## 📋 Project Overview

This project uses data from the Mayo Clinic trial on primary biliary cirrhosis (1974-1984) to predict liver cirrhosis stages:
- **Stage 1**: Mild fibrosis (early stage)
- **Stage 2**: Moderate fibrosis  
- **Stage 3**: Cirrhosis (advanced scarring)

## 🚀 Features

- **Interactive Web App**: User-friendly Streamlit interface for predictions
- **Comprehensive Model Training**: Jupyter notebook with full ML pipeline
- **Data Preprocessing**: Handles missing values and feature scaling
- **Model Evaluation**: Includes accuracy metrics and feature importance analysis
- **Professional UI**: Clean, medical-grade interface with input validation

## 📁 Project Structure

```
liver_cirrhosis_stage/
├── README.md                           # Project documentation
├── app.py                             # Streamlit web application
├── train.ipynb                        # Jupyter notebook for training
├── train_fixed.py                     # Fixed training script (recommended)
├── requirements.txt                   # Python dependencies
├── liver_cirrhosis.csv               # Dataset (25,000 records)
├── liver_cirrhosis_model.pkl         # Trained model file
└── Liver Cirrhosis Stage Detection.pdf # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Clone the Project
```bash
git clone https://github.com/ShubhamMallick/Liver_Cirrhosis_stage.git
cd Liver_Cirrhosis_stage
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Web Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📊 Dataset Information

**Source**: Mayo Clinic Primary Biliary Cirrhosis Data (1974-1984)
**Size**: 25,000 records with 19 features

### Input Features:
- **Demographics**: Age, Sex
- **Clinical Signs**: Ascites, Hepatomegaly, Spiders, Edema
- **Laboratory Values**: 
  - Bilirubin (mg/dl)
  - Cholesterol (mg/dl) 
  - Albumin (gm/dl)
  - Copper (ug/day)
  - Alkaline Phosphatase (U/liter)
  - SGOT (U/ml)
  - Triglycerides (mg/dl)
  - Platelets (per ml/1000)
  - Prothrombin Time (seconds)
- **Treatment**: Drug (D-penicillamine or Placebo)

### Target Variable:
- **Stage**: Cirrhosis stage (1, 2, or 3)

## 🤖 Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: 16 clinical and laboratory features
- **Preprocessing**: 
  - Categorical encoding (One-hot and Ordinal)
  - Missing value imputation
  - Feature scaling for numerical variables
- **Performance**: Evaluated using accuracy, precision, recall, and F1-score

## 🖥️ Using the Web Application

1. **Launch the app**: `streamlit run app.py`
2. **Enter patient information**:
   - Fill in all required clinical parameters
   - Use the sidebar for reference information
3. **Get prediction**: Click "Predict Stage" to see results
4. **Interpret results**: View the predicted stage with clinical interpretation

### Example Usage:
- Enter typical values for a patient
- The model will predict the cirrhosis stage
- Results include confidence and feature importance

## 📈 Model Training

### Option 1: Use Jupyter Notebook
```bash
jupyter notebook train.ipynb
```

### Option 2: Use Fixed Training Script (Recommended)
```bash
python train_fixed.py
```

The fixed script includes:
- ✅ Corrected column name spelling
- ✅ Proper data preprocessing 
- ✅ Comprehensive evaluation metrics
- ✅ Feature importance analysis

## 🔧 Recent Fixes Applied

### Issues Resolved:
1. **Spelling Error**: Fixed 'Tryglicerides' → 'Triglycerides'
2. **Missing Dependencies**: Added `streamlit` and `joblib` to requirements.txt
3. **Data Preprocessing**: Created proper pipeline to handle non-predictive columns
4. **Model Consistency**: Ensured feature names match between training and prediction

## 📋 Requirements

```
pandas
scikit-learn
matplotlib
jupyter
notebook
seaborn
streamlit
joblib
```

## 🏥 Clinical Context

This model is designed for **educational and research purposes only**. It should not be used for actual medical diagnosis or treatment decisions. Always consult qualified healthcare professionals for medical advice.

### Limitations:
- Model trained on historical data (1974-1984)
- Limited to specific patient population
- Requires validation on current clinical data
- Not FDA approved for clinical use

## 📊 Performance Metrics

The model provides:
- **Accuracy Score**: Overall prediction accuracy
- **Classification Report**: Precision, recall, F1-score per class
- **Confusion Matrix**: Detailed prediction breakdown
- **Feature Importance**: Most influential clinical parameters

## 🤝 Contributing

To improve this project:
1. Fork the repository
2. Create a feature branch
3. Make improvements (data quality, model performance, UI/UX)
4. Submit a pull request

### Potential Improvements:
- Add more recent clinical data
- Implement additional ML algorithms
- Enhance web interface with visualizations
- Add model explainability features
- Include confidence intervals

## 📄 License

This project is for educational purposes. Please ensure compliance with medical data regulations in your jurisdiction.

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the training notebook for detailed explanations
3. Ensure all dependencies are properly installed

## 🏆 Acknowledgments

- Mayo Clinic for providing the primary biliary cirrhosis dataset
- Scikit-learn community for machine learning tools
- Streamlit team for the web application framework

---

**⚠️ Medical Disclaimer**: This tool is for educational purposes only and should not be used for medical diagnosis. Always consult healthcare professionals for medical decisions.

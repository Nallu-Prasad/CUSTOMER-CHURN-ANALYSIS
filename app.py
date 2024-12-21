from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Load the scaler and model
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to preprocess the input data
def preprocess_data(data):
    df_input = pd.DataFrame([data])

    le_gender = LabelEncoder()
    le_payment_method = LabelEncoder()

    if 'Gender' in df_input.columns:
        df_input['Gender'] = le_gender.fit_transform(df_input['Gender'])
    
    if 'PaymentMethod' in df_input.columns:
        df_input['PaymentMethod'] = le_payment_method.fit_transform(df_input['PaymentMethod'])
    
    if 'avg_spend_per_month' not in df_input.columns:
        df_input['avg_spend_per_month'] = df_input['TotalCharges'] / df_input['Tenure']
    
    df_input.replace([np.inf, -np.inf], np.nan, inplace=True)
    df_input.fillna(0, inplace=True)
    scaled_data = scaler.transform(df_input)

    return scaled_data

# Route to handle churn prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        scaled_data = preprocess_data(data)
        prediction = model.predict(scaled_data)
        churn_prob = model.predict_proba(scaled_data)[0][1]
        return jsonify({"Churn Prediction": int(prediction[0]), "Churn Probability": churn_prob})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

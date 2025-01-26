import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Load the dataset
data = pd.read_csv("D:/git_projects/Career-Prediction-App/dataset/jobroles_IT.csv")

# Preprocess the data
# Split the interested subjects and additional job roles into lists
data["Interested Subjects"] = data["Interested Subjects"].str.split(", ")
additional_roles_columns = ["Job Role", "Job Role 1", "Job Role 2", "Job Role 3", "Job Role 4"]
data["Job Roles"] = data[additional_roles_columns].values.tolist()
data["Job Roles"] = data["Job Roles"].apply(lambda x: list(filter(pd.notna, x)))

# Features and target
X = data[["Certifications", "Interested Subjects", "Education Level"]]
y = data["Job Roles"]

# Multi-label binarizer for target variable
mlb = MultiLabelBinarizer()
y_encoded = mlb.fit_transform(y)

# Convert 'Interested Subjects' from lists to strings for encoding
X["Interested Subjects"] = X["Interested Subjects"].apply(lambda x: ", ".join(x))

# One-hot encoding for categorical features
categorical_features = ["Certifications", "Education Level"]
textual_features = ["Interested Subjects"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("text", OneHotEncoder(handle_unknown="ignore"), textual_features),
    ]
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Build the pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", MultiOutputClassifier(RandomForestClassifier(random_state=42)))
    ]
)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump((pipeline, mlb), "career_predictor_model.pkl")

print("Model trained and saved as 'career_predictor_model.pkl'.")

# Function for predictions
def predict_job_roles(certifications, interested_subjects, education_level):
    input_data = pd.DataFrame({
        "Certifications": [certifications],
        "Interested Subjects": [interested_subjects],
        "Education Level": [education_level]
    })
    input_data["Interested Subjects"] = input_data["Interested Subjects"].apply(lambda x: ", ".join(x))
    predictions = pipeline.predict(input_data)
    predicted_roles = mlb.inverse_transform(predictions)
    return predicted_roles[0]

# Example usage
example_certifications = "AWS Certified Solutions Architect"
example_subjects = ["Cloud Computing", "Infrastructure Design"]
example_education = "Bachelor's"

predicted_roles = predict_job_roles(example_certifications, example_subjects, example_education)
print("Predicted Job Roles:", predicted_roles)

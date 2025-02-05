from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

# Load the pre-trained model and label binarizer
pipeline, mlb = joblib.load("career_predictor_model.pkl")

app = Flask(__name__)

# Home route - User selects details
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user inputs
        certifications = request.form.get("certifications")
        interested_subjects = request.form.getlist("interested_subjects")
        education_level = request.form.get("education_level")
        
        # Redirect to result page with user inputs
        return redirect(url_for("result", 
                                certifications=certifications, 
                                interested_subjects=",".join(interested_subjects), 
                                education_level=education_level))
    
    # Render the homepage
    return render_template("index.html")

# Result route - Show the prediction
@app.route("/result")
def result():
    # Get user inputs from query parameters
    certifications = request.args.get("certifications")
    interested_subjects = request.args.get("interested_subjects").split(",")
    education_level = request.args.get("education_level")
    
    # Prepare the input for prediction
    input_data = pd.DataFrame({
        "Certifications": [certifications],
        "Interested Subjects": [", ".join(interested_subjects)],
        "Education Level": [education_level]
    })
    
    # Make predictions
    predictions = pipeline.predict(input_data)
    predicted_roles = mlb.inverse_transform(predictions)[0]
    
    # Render the result page with predictions
    return render_template("result.html", roles=predicted_roles)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def start():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    technical_skills = request.form.get('technical_skills', '')
    soft_skills = request.form.get('soft_skills', '')
    education = request.form.get('education', '')
    certifications = request.form.get('certifications', '')
    hobbies = request.form.get('hobbies', '')
    
    prompt = (f"Suggest top 10 career options based on the following details:\n\n"
              f"Technical Skills: {technical_skills}\n"
              f"Soft Skills: {soft_skills}\n"
              f"Education: {education}\n"
              f"Certifications: {certifications}\n"
              f"Hobbies/Interests: {hobbies}\n\n"
              f"Format: Career Name - Short Explanation")
    
    try:
        command = ["ollama", "run", "llama3.2:1b", prompt]
        result = subprocess.run(command, capture_output=True, text=True, timeout=500)
        
        print("Command Output:", result.stdout)
        print("Error Output:", result.stderr)
        
        if result.stdout.strip():
            career_recommendations = result.stdout.strip().split("\n")
        else:
            career_recommendations = ["Error generating career recommendations. No response received."]
    except Exception as e:
        print("Exception:", str(e))
        career_recommendations = ["An error occurred while generating recommendations.", str(e)]
    
    return render_template('result.html', recommendations=career_recommendations)

@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    if request.method == 'POST':
        job_role = request.form.get('job_role', '')
        prompt = f"Provide a detailed roadmap to become a {job_role}, including necessary skills, education, and experience."
        
        try:
            command = ["ollama", "run", "llama3.2:1b", prompt]
            result = subprocess.run(command, capture_output=True, text=True, timeout=500)
            
            print("Command Output:", result.stdout)
            print("Error Output:", result.stderr)
            
            roadmap_steps = result.stdout.strip().split("\n") if result.stdout.strip() else ["Error generating roadmap."]
        except Exception as e:
            print("Exception:", str(e))
            roadmap_steps = ["An error occurred while generating the roadmap.", str(e)]
        
        return render_template('roadmap_result.html', roadmap=roadmap_steps)
    
    return render_template('roadmap.html')

@app.route('/skillgap', methods=['GET', 'POST'])
def skillgap():
    if request.method == 'POST':
        user_skills = request.form.get('user_skills', '')
        dream_job = request.form.get('dream_job', '')
        prompt = f"Compare the skills required for {dream_job} with the user's skills: {user_skills}. Identify gaps and suggest improvements."
        
        try:
            command = ["ollama", "run", "llama3.2:1b", prompt]
            result = subprocess.run(command, capture_output=True, text=True, timeout=500)
            
            print("Command Output:", result.stdout)
            print("Error Output:", result.stderr)
            
            skill_gaps = result.stdout.strip().split("\n") if result.stdout.strip() else ["Error generating skill gap analysis."]
        except Exception as e:
            print("Exception:", str(e))
            skill_gaps = ["An error occurred while generating skill gap analysis.", str(e)]
        
        return render_template('skillgap_result.html', gaps=skill_gaps)
    
    return render_template('skillgap.html')

if __name__ == '__main__':
    app.run(debug=True)
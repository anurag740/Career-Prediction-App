import pandas as pd
import random

# Define possible values for each field
certifications = {
    "Data Scientist": ["Data Science Certificate", "Certified Machine Learning Specialist", "Deep Learning Certification"],
    "Cloud Architect": ["AWS Certified Solutions Architect", "Google Cloud Architect", "Microsoft Certified: Azure Solutions Architect"],
    "Network Engineer": ["Cisco Certified Network Associate", "Juniper Networks Certified", "CompTIA Network+"],
    "Cybersecurity Analyst": ["CompTIA Security+", "Certified Information Systems Security Professional (CISSP)", "Certified Ethical Hacker (CEH)"],
    "Project Manager": ["Certified ScrumMaster (CSM)", "Project Management Professional (PMP)", "Agile Certified Practitioner (PMI-ACP)"],
    "Cloud Engineer": ["Microsoft Certified: Azure Fundamentals", "AWS Certified Developer", "Google Cloud Certified Associate"],
    "Software Developer": ["Oracle Certified Java Programmer", "Certified Python Developer", "Microsoft Certified: C# Specialist"],
    "Data Analyst": ["Tableau Desktop Specialist", "Power BI Certification", "Certified Business Analytics Specialist"],
    "Ethical Hacker": ["Certified Ethical Hacker (CEH)", "Offensive Security Certified Professional (OSCP)", "GIAC Penetration Tester (GPEN)"],
    "Data Engineer": ["Google Cloud Professional Data Engineer", "Microsoft Certified: Data Engineer Associate", "AWS Certified Big Data Specialist"]
}

interested_subjects = {
    "Data Scientist": ["Machine Learning", "Data Analysis", "Statistics"],
    "Cloud Architect": ["Cloud Computing", "DevOps", "Infrastructure Design"],
    "Network Engineer": ["Networking", "Routing and Switching", "Network Security"],
    "Cybersecurity Analyst": ["Cybersecurity", "Risk Management", "Penetration Testing"],
    "Project Manager": ["Agile Development", "Project Management", "Leadership"],
    "Cloud Engineer": ["Cloud", "Virtualization", "Automation"],
    "Software Developer": ["Java Development", "Coding", "Software Design"],
    "Data Analyst": ["Data Visualization", "Analytics", "SQL"],
    "Ethical Hacker": ["Hacking", "Cybersecurity", "Vulnerability Analysis"],
    "Data Engineer": ["Data Engineering", "Cloud Computing", "ETL Processes"]
}

additional_roles = {
    "Machine Learning": ["AI Engineer", "Machine Learning Engineer"],
    "Data Analysis": ["Business Analyst", "Data Scientist"],
    "Statistics": ["Statistician", "Data Scientist"],
    "Cloud Computing": ["Cloud Engineer", "DevOps Engineer"],
    "DevOps": ["DevOps Engineer", "Cloud Architect"],
    "Infrastructure Design": ["System Architect", "Cloud Architect"],
    "Networking": ["Network Administrator", "Network Security Specialist"],
    "Routing and Switching": ["Network Engineer", "Systems Engineer"],
    "Network Security": ["Security Analyst", "Network Security Specialist"],
    "Cybersecurity": ["Security Consultant", "Penetration Tester"],
    "Risk Management": ["Risk Analyst", "Cybersecurity Analyst"],
    "Penetration Testing": ["Ethical Hacker", "Penetration Tester"],
    "Agile Development": ["Scrum Master", "Agile Coach"],
    "Project Management": ["Project Manager", "Program Manager"],
    "Leadership": ["Team Lead", "Project Manager"],
    "Virtualization": ["Cloud Engineer", "Infrastructure Engineer"],
    "Automation": ["Automation Engineer", "DevOps Engineer"],
    "Java Development": ["Software Developer", "Backend Developer"],
    "Coding": ["Software Developer", "Programmer"],
    "Software Design": ["Software Architect", "UI/UX Designer"],
    "Data Visualization": ["Data Analyst", "BI Developer"],
    "Analytics": ["Data Analyst", "Business Analyst"],
    "SQL": ["Database Administrator", "Data Analyst"],
    "Hacking": ["Ethical Hacker", "Security Consultant"],
    "Vulnerability Analysis": ["Penetration Tester", "Security Analyst"],
    "Data Engineering": ["Data Engineer", "Big Data Specialist"],
    "ETL Processes": ["Data Engineer", "Data Integration Specialist"]
}

education_levels = ["Bachelor's", "Master's", "PhD"]

# Generate synthetic dataset
def generate_dataset(rows=100000):
    data = []
    for _ in range(rows):
        job_role = random.choice(list(certifications.keys()))
        cert = random.choice(certifications[job_role])
        subjects = random.sample(interested_subjects[job_role], k=random.randint(1, 3))
        education = random.choice(education_levels)

        # Determine additional job roles based on interested subjects
        additional_jobs = []
        for subject in subjects:
            if subject in additional_roles:
                additional_jobs.extend(additional_roles[subject])
        additional_jobs = list(set(additional_jobs))[:4]  # Limit to 4 additional roles

        # Create row with multiple job roles
        row = {
            "Certifications": cert,
            "Interested Subjects": ", ".join(subjects),
            "Education Level": education,
            "Job Role": job_role,
            "Job Role 1": additional_jobs[0] if len(additional_jobs) > 0 else None,
            "Job Role 2": additional_jobs[1] if len(additional_jobs) > 1 else None,
            "Job Role 3": additional_jobs[2] if len(additional_jobs) > 2 else None,
            "Job Role 4": additional_jobs[3] if len(additional_jobs) > 3 else None
        }
        data.append(row)
    return pd.DataFrame(data)

# Generate the dataset
dataset = generate_dataset(100000)

# Save to CSV
dataset.to_csv("it_job_roles_dataset.csv", index=False)
print("Large dataset with 100,000 rows and additional job roles created and saved as 'it_job_roles_dataset.csv'.")

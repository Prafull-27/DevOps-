from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dynamic portfolio payload using resume data
    resume_data = {
        "name": "Prafull Musale",
        "role": "Cloud Engineer / DevOps Enthusiast",
        "education": "B.Tech CS (Cloud Computing)",
        "location": "Pune, Maharashtra",
        "skills": {
            "Cloud & IaC": "AWS (EC2, IAM, VPC, S3, Lambda, CloudWatch, RDS), Terraform",
            "Containers": "Docker, Kubernetes",
            "Automation": "Python, Bash Scripting",
            "Networking": "TCP/IP, DNS, Routing, VPC Security Groups"
        },
        "experience": [
            {
                "title": "Cloud Intern",
                "company": "EmSphere Technologies Pvt. Ltd.",
                "duration": "May 2025 - August 2025",
                "highlights": [
                    "Developed a cloud-based task management and monitoring system for workflow tracking.",
                    "Built monitoring dashboards for system health, resource utilization, and application performance.",
                    "Integrated AWS services and automation mechanisms to enhance scalability and reliability."
                ]
            },
            {
                "title": "Python Intern",
                "company": "LiSYS Technocraft",
                "duration": "May 2024 - August 2024",
                "highlights": [
                    "Worked on computer vision projects involving face detection and recognition using OpenCV.",
                    "Applied prompt engineering techniques to improve AI model responses and output quality.",
                    "Enhanced detection accuracy through image processing, testing, and performance optimization."
                ]
            }
        ],
        "projects": [
            {
                "title": "SecuCloud Cloud Immune System",
                "description": "A real-time cloud security monitoring system on AWS to detect misconfigurations and threats. Integrated AWS Lambda, API Gateway, DynamoDB, and CloudWatch.",
                "tech": "Python, AWS Lambda, DynamoDB, Event Bridge, SNS, S3, EC2"
            },
            {
                "title": "Dockerized Application Deployment",
                "description": "Designed and deployed a multi-container application using Docker and Docker Compose. Optimized images to improve container performance.",
                "tech": "Docker, Docker Compose, AWS EC2, AWS ECS"
            }
        ],
        "deploy_env": {
            "runtime": "Python 3.14 / Flask 3.1",
            "platform": "AWS ECS"
        }
    }
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

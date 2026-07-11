# Dockerized Flask Portfolio Application

A modern portfolio web application built using **Flask** and containerized with **Docker**. This project demonstrates containerization of a Python web application and can be run locally using Docker.

## 🚀 Features

- Dynamic portfolio built with Flask
- Responsive user interface
- Displays:
  - Professional Profile
  - Technical Skills
  - Internship Experience
  - Cloud Projects
- Dockerized for easy deployment
- Lightweight and easy to run

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML5
- CSS3
- Jinja2
- Docker

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── templates
    └── index.html
```

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Prafull-27/DevOps-.git
cd DevOps-
```

---

## 🐳 Build Docker Image

```bash
docker build -t flask-portfolio .
```

---

## ▶️ Run Docker Container

If your Dockerfile exposes **port 80**:

```bash
docker run -d -p 5000:80 flask-portfolio
```

If your application runs on **port 5000**:

```bash
docker run -d -p 5000:5000 flask-portfolio
```

Open your browser:

```
http://localhost:5000
```

---

## 📸 Application Preview

The application includes:

- 👨‍💻 Personal Information
- ☁️ Cloud & DevOps Skills
- 💼 Internship Experience
- 🚀 Projects
- 📚 Education

---

## 💻 Technologies Used

### Programming
- Python
- Flask

### Cloud
- AWS (EC2, IAM, VPC, S3, Lambda, CloudWatch, RDS)

### DevOps
- Docker
- Kubernetes
- Terraform

### Networking
- TCP/IP
- DNS
- Routing
- VPC Security Groups

---

## 📋 Prerequisites

- Docker Desktop or Docker Engine
- Git

Verify installation:

```bash
docker --version
git --version
```

---

## 🧹 Stop the Container

```bash
docker ps
docker stop <container_id>
```

---

## 🗑️ Remove the Container

```bash
docker rm <container_id>
```

---

## 🗑️ Remove the Docker Image

```bash
docker rmi flask-portfolio
```

---

## 👨‍💻 Author

**Prafull Musale**

- GitHub: https://github.com/Prafull-27
- Email: prafullmusale01@gmail.com

---

## 📄 License

This project is created for learning, Docker practice, and portfolio demonstration purposes.

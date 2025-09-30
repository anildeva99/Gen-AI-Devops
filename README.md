# AI-Powered DevOps CI/CD Demo

## Overview
This project demonstrates end-to-end AI-powered DevOps CI/CD:
- **GitHub** → Source Code
- **Jenkins** → CI/CD Automation
- **Docker** → Containerization
- **Minikube / Kubernetes** → Deployment

## Folder Structure
app/          # Flask app + Dockerfile
k8s/          # Kubernetes manifests
Jenkinsfile   # Jenkins pipeline
ai_generate_pipeline.py # AI script to auto-generate files

## Steps
1. Run `python3 ai_generate_pipeline.py` to generate all files
2. Start Minikube on your EC2
3. Run Jenkins and configure pipeline pointing to this repo
4. Build & deploy using Jenkins
5. Access app: http://<EC2-Public-IP>:30080
# Computer Vision Data Pipeline & Kubernetes Containerization (SCT_ML_03)

[![Data Pipeline CI](https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/SCT_ML_03/actions/workflows/ci.yml/badge.svg)](https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/SCT_ML_03/actions)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Batch%20Job-blue.svg)

A production-grade, containerized ETL data pipeline designed to ingest, validate, transform, and normalize large-scale image datasets. Built with Python, OpenCV, Docker, and Kubernetes batch jobs to prepare high-dimensional image vector features for downstream machine learning workloads.

---

## 📌 System Architecture

```text
  ┌─────────────────┐       ┌────────────────────┐       ┌────────────────────────┐
  │  Raw Image Data │ ───►  │ Batch Extract (Py) │ ───►  │ OpenCV Transformations │
  └─────────────────┘       └────────────────────┘       └────────────────────────┘
                                                                      │
  ┌─────────────────┐       ┌────────────────────┐                    │
  │ K8s Execution   │ ◄───  │ Docker Container   │ ◄──────────────────┘
  │ (Batch Processing)│     │ Packaging          │     (Flattened Normalization)
  └─────────────────┘       └────────────────────┘


## 1. Local Python Setup & Unit Tests
# Clone the repository
git clone [https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/SCT_ML_03.git](https://github.com/Naga-Sai-Bestharapalli-Kakaraparthi/SCT_ML_03.git)
cd SCT_ML_03

# Install dependencies
pip install -r requirements.txt

# Run Unit Tests
pytest tests/

## 2. Docker Containerization
# Build the Docker image
docker build -t image-etl-pipeline:v1 .

# Run the batch extraction pipeline in Docker
docker run -v $(pwd)/PetImages:/app/PetImages image-etl-pipeline:v1

## 3. Deploy Batch Job to Kubernetes
# Deploy processing job to Kubernetes cluster
kubectl apply -f k8s/job.yaml

# Check batch execution status
kubectl get jobs
kubectl logs job/image-etl-job

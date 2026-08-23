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
kubectl apply -f k8s/job.yaml

# Check batch execution status
kubectl get jobs
kubectl logs job/image-etl-job

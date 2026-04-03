# 🚀 Application Monitoring using Prometheus & Grafana

This project demonstrates how to deploy a containerized application and implement monitoring using Prometheus and Grafana with Docker Compose.

## 📌 Project Overview

In this project, we:

Deploy a sample Flask application
Expose application metrics via /metrics
Collect metrics using Prometheus
Visualize metrics using Grafana
Monitor both application-level and infrastructure-level metrics
## 🧱 Architecture
```
User → Flask App → Prometheus → Grafana
                  ↑
            Node Exporter
```
## ⚙️ Prerequisites
Docker

Docker Compose

Basic knowledge of containers

Web browser
## 📁 Project Structure
```
monitoring-assessment/
│
├── docker-compose.yml
├── prometheus.yml
│
└── app/
    ├── app.py
    └── Dockerfile
```
## 🚀 Setup & Execution
### 1️⃣ Clone Repository
```git clone https://github.com/rishikkkkkk/monitoring-assessment.git```
### 2️⃣ Start Services
```docker-compose up --build```
### 3️⃣ Access Services
| Service     | URL                                                            |
| ----------- | -------------------------------------------------------------- |
| Application | [http://localhost:5000](http://localhost:5000)                 |
| Metrics     | [http://localhost:5000/metrics](http://localhost:5000/metrics) |
| Prometheus  | [http://localhost:9090](http://localhost:9090)                 |
| Grafana     | [http://localhost:3002](http://localhost:3002)                 |

## 📈 Grafana Setup
1.  Open Grafana → ```http://localhost:3002```
2.  Login → admin / admin
3.  Add data source:
  Type: Prometheus
  URL: ```http://prometheus:9090```

## 📊 Dashboards
### Infrastructure Monitoring
1.  CPU Usage
2.  Memory Usage
3.  Disk Availability
### Application Monitoring
1.  Total Requests
2.  Requests per Second
3.  Request Trends

## 🧪 Traffic Simulation
### Generate load using:
```for i in {1..1000}; do curl http://localhost:5000; done```

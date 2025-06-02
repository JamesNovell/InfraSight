
> ⚠️ This project is based on internal data and is not intended for public deployment.


# 📊 InfraSight: DevOps DataOps Dashboard

This repository demonstrates infrastructure and data engineering practices using simulated versions of internal telemetry from 2000+ devices. While the actual system is proprietary, this project highlights the architecture and approach I developed.
---

## 🚀 Features

* **Infrastructure-as-Code** with Terraform and Ansible
* **Automated Data Collection** from unit telemetry (BNR totals, odometers)
* **Data Transformation Pipelines** using Python
* **Grafana Dashboards** for lifecycle analytics and usage trends
* **CI/CD Pipelines** powered by GitHub Actions
* **Containerized Stack** for local or remote deployments

---

## 🧱 Tech Stack

| Layer         | Technology                |
| ------------- | ------------------------- |
| IaC           | Terraform, Ansible        |
| CI/CD         | GitHub Actions            |
| Scripting     | Python, Bash              |
| Monitoring    | Prometheus, Grafana       |
| Optional API  | Flask or FastAPI          |
| Orchestration | Docker / Kubernetes (opt) |

---

## 📂 Project Structure

```
infrasight/
├── terraform/              # AWS infrastructure
├── ansible/                # Host provisioning
├── scripts/                # Data pipeline scripts
├── monitoring/             # Grafana & Prometheus config
├── k8s/                    # Kubernetes manifests (optional)
├── api/                    # REST API for metrics (optional)
├── tests/                  # Pipeline unit tests
├── docs/                   # Architecture diagrams & docs
├── .github/workflows/      # CI/CD workflows
└── docker-compose.yml      # Dev stack setup
```

---

## 📊 Example Dashboard

Includes:

* Unit usage over time
* Forecasted part replacements
* Region-wise performance heatmaps

*Dashboard preview available in [`docs/`](docs/)*

---

## ⚙️ Getting Started

### Prerequisites

* Python 3.10+
* Docker & Docker Compose
* Terraform CLI
* AWS CLI & credentials

### Quickstart

```bash
# Clone the repository
git clone https://github.com/jamesnovell/infrasight.git
cd infrasight

# Set up environment
cp .env.example .env

# Build and run local stack
docker-compose up --build

# Run data pipeline
python scripts/fetch_metrics.py
python scripts/clean_data.py
```

---

## 📊 Data Pipeline Flow

1. **Collect Raw Data** → `fetch_metrics.py`
2. **Clean/Transform Data** → `clean_data.py`
3. **Ingest to Prometheus** → Exporter or bridge
4. **Visualize in Grafana**

---

## 🛡️ License

MIT License

---

## 🤛 Author

**James Novell**
[LinkedIn](https://www.linkedin.com/in/james-novell-3489a01b1/) · [Email](mailto:novell92@gmail.com)

---

## 📌 Roadmap

* [ ] Add FastAPI integration for REST metrics
* [ ] Enable predictive modeling on failure rates
* [ ] Schedule nightly S3 backups
* [ ] Kubernetes deployment setup

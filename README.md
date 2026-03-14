# System Monitoring API
A simple system monitoring project written in Python that collects CPU, memory, and disk usage metrics from a machine and stores them in PostgreSQL via a FastAPI backend.

## Features
- Collects real-time CPU, memory, and disk usage using psutil.
- Provides REST API to store and retrieve metrics with FastAPI.
- Stores metrics in PostgreSQL.
- Provides real-time metrics visualization in Grafana.
- Docker-ready for easy setup.

## Getting Started
### Required
- Python 3.11
- PostgreSQL
- Grafana 12.4.1
- (Optional) Docker & Docker Compose for easy setup.
### 1. Clone the repository
`git clone https://github.com/maxxzxv/system_monitoring.git`
`cd system_monitoring`
### 2. Install dependencies
`pip install -r requirements.txt`
### 3. Configure PostgreSQL
- Update docker-compose.yml with your information:
change the database name, username, and password
- Update app/database.py with your information:
`DATABASE_URL = "postgresql://monitoring_user:strongpassword@localhost:5432/monitoring_db"`
### 4. Run the API
`uvicorn app.main:app --reload`
- API docs available at https://127.0.0.1:8000/docs
- Endpoints:
    - GET / -> test endpoint
    - POST /metrics -> send CPU/memory/disk data
### 5. Run the Collector
`python collector/collect_metrics.py`
### 6. Configure Grafana
- Login into Grafana under `https://127.0.0.1:3000`
    - Default credentials `admin / admin`
- Create new dashboard
- Configure visualiations for cpu, memory, and disk. Example query:
`SELECT "timestamp" AS "time", cpu AS value FROM metrics ORDER BY timestamp ASC`
### 7. (Optional) Build with Docker
`docker-compose up --build`


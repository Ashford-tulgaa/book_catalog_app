# Book Catalog API

## Project Overview

Book Catalog API is a Django REST Framework application that provides CRUD operations for managing books.

The project demonstrates a complete DevOps workflow by combining:

* Django REST API development
* Docker containerization
* GitHub Actions CI/CD automation
* GitHub Container Registry (GHCR) image publishing
* Kubernetes deployment
* Helm-based application management
* Argo CD GitOps continuous deployment

The application exposes REST endpoints for creating, retrieving, updating, and deleting book records.

## Technology Stack

| Component             | Technology                       |
| --------------------- | -------------------------------- |
| Backend               | Django 5 + Django REST Framework |
| Database              | SQLite (development)             |
| Containerization      | Docker                           |
| Container Registry    | GitHub Container Registry (GHCR) |
| CI/CD                 | GitHub Actions                   |
| Kubernetes            | Kubernetes / k3d                 |
| Package Management    | Helm                             |
| Continuous Deployment | Argo CD                          |

---

# API Usage Examples

## Base URL

When running locally:

```
http://localhost:8000
```

---

## List All Books

### Request

```http
GET /api/books/
```

Example:

```bash
curl http://localhost:8000/api/books/
```

Example response:

```json
[
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "published_date": "2008-08-01"
    }
]
```

---

## Create a Book

### Request

```http
POST /api/books/
```

Example:

```bash
curl -X POST http://localhost:8000/api/books/ \
-H "Content-Type: application/json" \
-d '{
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt",
    "published_date": "1999-10-20"
}'
```

---

## Retrieve a Single Book

### Request

```http
GET /api/books/<id>/
```

Example:

```bash
curl http://localhost:8000/api/books/1/
```

---

## Update a Book

### Request

```http
PUT /api/books/<id>/
```

Example:

```bash
curl -X PUT http://localhost:8000/api/books/1/ \
-H "Content-Type: application/json" \
-d '{
    "title": "Updated Book Title",
    "author": "Updated Author",
    "published_date": "2025-01-01"
}'
```

---

## Delete a Book

### Request

```http
DELETE /api/books/<id>/
```

Example:

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

---

# Local Build and Run Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Ashford-tulgaa/book_catalog_app.git

cd book_catalog_app
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Database Migrations

```bash
python manage.py migrate
```

---

## 5. Start Django Development Server

```bash
python manage.py runserver
```

The API will be available at:

```
http://localhost:8000/api/books/
```

---

# Docker Build and Run

## Build Docker Image

```bash
docker build \
-t book-catalog-api .
```

---

## Run Container

```bash
docker run -p 8000:8000 book-catalog-api
```

The API will be available at:

```
http://localhost:8000
```

---

# CI/CD Pipeline

The project uses GitHub Actions to automate continuous integration and container publishing.

The workflow is triggered when changes are pushed or merged into the `main` branch.

## Pipeline Flow

```
Developer Push
        |
        v
GitHub Actions
        |
        +--> Install Python dependencies
        |
        +--> Run Django migrations
        |
        +--> Execute automated tests
        |
        +--> Build Docker image
        |
        +--> Push image to GHCR
        |
        v
Argo CD Deployment
        |
        v
Kubernetes Cluster
```

## CI Steps

### Dependency Installation

GitHub Actions installs all required Python packages:

```bash
pip install -r requirements.txt
```

### Testing

The pipeline executes Django tests:

```bash
python manage.py test
```

If tests fail, the Docker image is not created.

### Docker Image Build

The workflow builds a production container image:

```bash
docker build -t ghcr.io/ashford-tulgaa/book-catalog-api:latest .
```

### Image Publishing

The image is pushed to GitHub Container Registry:

```
ghcr.io/ashford-tulgaa/book-catalog-api
```

---

# Kubernetes and Helm Setup

## Requirements

Install:

* Docker
* kubectl
* k3d
* Helm

---

# Create Kubernetes Cluster

Create a local Kubernetes cluster using k3d:

```bash
k3d cluster create book-catalog
```

Verify:

```bash
kubectl get nodes
```

---

# Deploy Using Helm

The application is packaged as a Helm chart:

```
book-catalog-api/
├── Chart.yaml
├── values.yaml
└── templates/
```

Install:

```bash
helm install book-catalog-api ./book-catalog-api
```

Check deployment:

```bash
kubectl get pods
```

---

## Upgrade Application

When Helm chart changes are made:

```bash
helm upgrade book-catalog-api ./book-catalog-api
```

---

# Argo CD GitOps Deployment

Argo CD manages Kubernetes deployment automatically.

The Argo CD Application configuration is stored in:

```
argocd/application.yaml
```

It defines:

* Git repository location
* Helm chart path
* Kubernetes destination
* Automatic synchronization policy

Example deployment flow:

```
Git Repository
      |
      v
Argo CD detects change
      |
      v
Helm chart synchronization
      |
      v
Kubernetes deployment updated
```

Argo CD automatically:

* Syncs changes from Git
* Applies Helm updates
* Self-heals manual cluster changes
* Removes resources deleted from Git

---

# Useful Kubernetes Commands

View deployments:

```bash
kubectl get deployments
```

View pods:

```bash
kubectl get pods
```

View services:

```bash
kubectl get services
```

View logs:

```bash
kubectl logs deployment/book-catalog-api
```

Restart deployment:

```bash
kubectl rollout restart deployment book-catalog-api
```

---

# Project Structure

```
book_catalog_app/
|
├── bookcatalog/          # Django project
├── books/                # Book API application
├── book-catalog-api/     # Helm chart
├── argocd/               # Argo CD configuration
├── .github/
│   └── workflows/        # GitHub Actions pipeline
├── Dockerfile
├── requirements.txt
└── manage.py
```

---

# Future Improvements

Possible improvements:

* Use PostgreSQL instead of SQLite
* Add database migrations during deployment
* Use versioned Docker image tags instead of `latest`
* Add monitoring with Prometheus and Grafana
* Deploy to managed Kubernetes infrastructure

# Book Catalog API

A Django REST Framework application that manages a simple book catalog and demonstrates a full DevOps delivery flow using Docker, PostgreSQL, GitHub Actions, Helm, and Argo CD.

## Project overview

This repository provides a lightweight API for storing and managing books. The backend is implemented with Django and Django REST Framework, and the project is structured to support:

- Local development with Docker Compose
- Automated CI validation with GitHub Actions
- Container image publishing to GitHub Container Registry (GHCR)
- Kubernetes deployment via Helm
- GitOps reconciliation through Argo CD

### Core features

- Create a new book
- List all books
- Retrieve a single book by ID
- Update an existing book
- Delete a book

### Data model

The `Book` model contains the following fields:

- `title`
- `author`
- `isbn`
- `published_date`

The `isbn` field is validated to ensure it contains either 10 or 13 numeric digits.

### Repository layout

- `bookcatalog/` — Django project settings and application wiring
- `books/` — models, serializers, views, URL routing, and tests
- `book-catalog-api/` — Helm chart used for Kubernetes deployment
- `argocd/` — Argo CD application manifest
- `.github/workflows/ci.yml` — CI workflow for tests, image build, and Helm image tag update

---

## API usage examples

The API is available under the `/api/` prefix.

### Base URL

Local development:

```text
http://localhost:8000/api/
```

### Endpoints

```http
GET    /api/books/           List all books
POST   /api/books/           Create a book
GET    /api/books/<id>/      Retrieve one book
PUT    /api/books/<id>/      Replace one book
PATCH  /api/books/<id>/      Partially update one book
DELETE /api/books/<id>/      Delete one book
```

### Example request payload

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

### Example `curl` commands

List books:

```bash
curl http://localhost:8000/api/books/
```

Create a book:

```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "isbn": "9780132350884",
    "published_date": "2008-08-01"
  }'
```

Retrieve a specific book:

```bash
curl http://localhost:8000/api/books/1/
```

Delete a specific book:

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

---

## Local build and run instructions

### Prerequisites

- Python 3.14+
- pip
- Docker and Docker Compose
- PostgreSQL database or a compatible local database service

### Option 1: Run with Docker Compose

From the project root:

```bash
docker compose up --build
```

This runs the Django development server and exposes the API on:

```text
http://localhost:8000
```

To stop the containers:

```bash
docker compose down
```

### Option 2: Run directly with Django

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Export the required environment variables:

```bash
export DB_NAME=book_catalog
export DB_USER=bookuser
export DB_PASSWORD=bookpassword
export DB_HOST=localhost
export DB_PORT=5432
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. Start the app:

```bash
python manage.py runserver 0.0.0.0:8000
```

### Run tests

```bash
python manage.py test
```

---

## CI/CD pipeline explanation

The repository uses GitHub Actions for continuous integration and delivery.

### Pipeline flow

The workflow in `.github/workflows/ci.yml` performs the following steps:

1. Checks out the repository code
2. Sets up Python 3.14 on the runner
3. Installs the project dependencies from `requirements.txt`
4. Runs the Django test suite against a PostgreSQL service container
5. If the workflow runs on a push to `main`, logs in to GitHub Container Registry (GHCR)
6. Builds the Docker image using the repository `Dockerfile`
7. Pushes the image to GHCR using a commit SHA as the tag
8. Updates the Helm values file to reference the new image tag
9. Commits that Helm change back to the repository so Argo CD can reconcile the deployment

### Why this matters

This pipeline creates a clean automation path:

- code changes trigger test validation
- passing changes are packaged into a Docker image
- the image is published to a registry
- Helm values are updated to the new tag
- Argo CD applies the new revision to the cluster automatically

---

## Kubernetes and Helm setup instructions

The Helm chart in `book-catalog-api/` is responsible for deploying the application into Kubernetes.

### What the chart deploys

- A Django API `Deployment`
- A Kubernetes `Service`
- An `Ingress` endpoint
- A PostgreSQL dependency from the Bitnami Helm chart
- A migration job that runs `python manage.py migrate` after synchronization

### Helm chart values

Key configuration is stored in `book-catalog-api/values.yaml`.

Important defaults include:

- image repository: `ghcr.io/ashford-tulgaa/book-catalog-api`
- replica count: `2`
- service type: `ClusterIP`
- container port: `8000`
- ingress host: `bookcatalog.local`
- PostgreSQL database name: `book_catalog`

### Install or upgrade with Helm

From the repository root:

```bash
helm dependency build book-catalog-api
helm upgrade --install book-catalog-api ./book-catalog-api
```

### Access the app in Kubernetes

If you are running a local cluster or a dev ingress setup, you can expose the service either through the configured ingress host or via port-forwarding:

```bash
kubectl port-forward svc/book-catalog-api 8000:80
```

Then access the API at:

```text
http://localhost:8000/api/books/
```

### Argo CD GitOps deployment

The repository also contains an Argo CD application manifest in `argocd/application.yaml`.

This manifest tells Argo CD to:

- watch the Git repository on the `main` branch
- read the Helm chart from `book-catalog-api/`
- deploy the chart into the `default` namespace

This gives the project a GitOps-based deployment loop where changes in Git become the source of truth for Kubernetes resources.

---

## Docker image details

The image is built from the `Dockerfile` and starts the Django development server with:

```bash
python manage.py runserver 0.0.0.0:8000
```

This container is intended to run on port `8000`.

## Notes

- The app is configured to use PostgreSQL-backed runtime settings.
- The current setup is well suited for a demo, learning project, or DevOps showcase.
- The Helm configuration expects the PostgreSQL service name to match the chart-managed database service.

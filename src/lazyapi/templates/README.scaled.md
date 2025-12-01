# {project_name}

A feature-based FastAPI project with scalable architecture.

## Structure

```
src/
├── core/           # Business logic, domain models
├── features/       # Feature modules
├── api/            # API routes and endpoints
└── infrastructure/ # External services, database
```

## Setup

```bash
cd {project_name}
source .venv/bin/activate
uvicorn src.main:app --reload
```

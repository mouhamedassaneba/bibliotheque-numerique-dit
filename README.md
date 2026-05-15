# Bibliotheque Numerique DIT

Plateforme de gestion de bibliotheque academique avec systeme de recommandation.

## Services

- Service Livres : http://localhost:5001
- Service Utilisateurs : http://localhost:5002
- Service Emprunts : http://localhost:5003
- Service Recommandation : http://localhost:5004
- Frontend : http://localhost

## Lancement avec Docker Compose

```bash
docker compose up --build
```

## Pipeline DVC

```bash
dvc repro
dvc metrics show
```

## Technologies

- Backend : Flask, FastAPI
- Base de donnees : PostgreSQL
- Conteneurisation : Docker, Docker Compose
- Versioning donnees : DVC
- Frontend : HTML/CSS/JavaScript

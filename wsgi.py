"""
Point d'entree pour l'hebergement en ligne (serveur de production).

Utilise par gunicorn :  gunicorn wsgi:app
Ne pas utiliser pour le mode local hors ligne (utilisez run.py).
"""
from app.main import create_app

app = create_app()

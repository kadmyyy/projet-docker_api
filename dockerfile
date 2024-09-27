# Utiliser une image Python officielle comme image parent
FROM python:3.9-slim

# Installer les dépendances système requises pour psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port 5000 au monde extérieur
EXPOSE 5000

# Démarrer l'application
CMD ["python", "app.py"]

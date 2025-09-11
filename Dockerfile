# image de base
FROM python:3.11-slim

# répertoire
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code de l'application
COPY . .

# Expose port utilisé 
EXPOSE 5000

#  commande pour lancer l'application 
CMD ["python", "app.py"]
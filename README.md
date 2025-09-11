# README

## Supprimer le fond d'une image avec Flask et Rembg

Cette application web permet de supprimer le fond d'une image (JPEG ou PNG) en utilisant [Flask](https://flask.palletsprojects.com/) et la bibliothèque [rembg](https://github.com/danielgatis/rembg).

### Fonctionnalités

- Téléversement d'une image via une interface web moderne (mode sombre/clair)
- Suppression automatique du fond de l'image
- Téléchargement de l'image traitée

---

## Prérequis

- Python 3.11 ou supérieur
- [pip](https://pip.pypa.io/en/stable/)
- (Optionnel) [Docker](https://www.docker.com/) si tu veux utiliser le conteneur

---

## Installation et lancement

### 1. Cloner le dépôt

```sh
git clone <url-du-repo>
cd remove_bg_app
```

### 2. Installer les dépendances Python

```sh
pip install -r requirements.txt
```

### 3. Lancer l'application Flask

```sh
python app.py
```

L'application sera accessible sur [http://localhost:5000](http://localhost:5000).

---

## Utilisation avec Docker

### 1. Construire l'image Docker

```sh
docker build -t remove_bg_app .
```

### 2. Lancer le conteneur

```sh
docker run -p 5000:5000 -v $(pwd)/uploads:/app/uploads -v $(pwd)/output:/app/output remove_bg_app
```

---

## Structure du projet

- `app.py` : Application Flask principale
- `requirements.txt` : Dépendances Python
- `templates/index.html` : Interface utilisateur
- `uploads/` : Images uploadées par l'utilisateur
- `output/` : Images traitées (sans fond)
- `Dockerfile` : Pour l'exécution dans un conteneur Docker

---

## Exemple d'utilisation

1. Ouvre [http://localhost:5000](http://localhost:5000) dans ton navigateur.
2. Téléverse une image (JPEG ou PNG).
3. Clique sur "Télécharger et Supprimer le Fond".
4. Télécharge l'image sans fond générée.

---

## Licence

Projet à usage éducatif.

---

## Auteur

- bbabadara@gmail.com

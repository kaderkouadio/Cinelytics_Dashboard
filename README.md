# Cinema_Insights - Phase 2 : Exploration et Visualisation des Données

Bienvenue dans la **Phase 2** de **Cinema_Insights**, une solution analytique interactive pour explorer et visualiser les données cinématographiques du jeu **MovieLens**. Cette phase se concentre sur l’analyse exploratoire des données (EDA) via Jupyter Notebook et la création d’une application web interactive avec **Streamlit**, connectée à l’API développée en Phase 1. Ce projet illustre des compétences avancées en analyse de données, visualisation, et développement d’interfaces utilisateur.

---

## Aperçu de la Phase 2

**Objectif** : Explorer les données MovieLens via l’API développée en Phase 1 et présenter des insights exploitables à travers une application web interactive pour les cinéphiles, analystes, et studios.

- **Analyse Exploratoire (EDA)** :
  - Utiliser le SDK Python `cinelytics_sdk` pour extraire les données de l’API.
  - Identifier les tendances dans les notes des films, les genres populaires, et les préférences des utilisateurs.
- **Visualisation Interactive** :
  - Créer des graphiques dynamiques avec **Plotly** pour illustrer les insights.
  - Développer une application **Streamlit** avec des tableaux dynamiques et une recherche avancée.
- **Enrichissement des Données** :
  - Intégrer l’API OMDb pour ajouter des affiches et liens IMDb aux films.

**Livrables** :
- Notebooks Jupyter : `Data_Cinelytics.ipynb` (EDA) et `Data_Visualisations.ipynb` (visualisations).
- Application Streamlit : Application multi-pages dans `App_Streamlit` pour une exploration interactive.

**Contexte de la Phase 1** : La Phase 1 a consisté à développer une API RESTful avec **FastAPI**, une base SQLite pour les données MovieLens, et un SDK Python (`cinelytics_sdk`) publié sur PyPI. L’API est hébergée sur Render (`https://cinema-insights.onrender.com`).

---

## Structure du Projet

```
Cinelytics_Dashboard/
├── App_Streamlit/                  # Application Streamlit
│   ├── App.py                 # Point d’entrée de l’application
│   ├── dashboard.py            # Tableau de bord principal
│   ├── page1.py                # Recherche de films (titre, genre, note)
│   ├── page2.py               # Analyse des genres (popularité, notes)
│   ├── page3.py                # Statistiques globales et tendances
│   ├── utils.py                 # Fonctions utilitaires
│   ├── requirements.txt         # Dépendances de l’application
│   ├── Images/                 # Ressources visuelles
│   │   ├── Backend_Developer.png
│   │   ├── Data_Analyst.png
│   │   ├── Phase_1.png
│   │   ├── Phase_2.png
│   │   └── profil.jpg
│   ├── __pycache__/
│       └── utils.cpython-...
├── dataanalysis/                   # Notebooks d’analyse
│   ├── Data_Cinelytics.ipynb   # Analyse exploratoire
│   ├── Data_Visualisations.ipynb # Visualisations
├── data/                          # Données brutes (CSV MovieLens)
├── output/                         # Données enrichies (ex. : links_enriched.parquet)
```

---

## Technologies Utilisées

- **Python** : Langage principal pour l’analyse et la visualisation.
- **Jupyter Notebook** : Environnement interactif pour l’EDA et les visualisations.
- **Streamlit** : Framework pour une application web interactive.
- **Pandas** : Manipulation et analyse des données.
- **Plotly** : Création de graphiques interactifs.
- **cinelytics_sdk** : SDK pour interroger l’API MovieLens.
- **OMDb API** : Enrichissement des données avec affiches et liens IMDb.
- **Requests** : Appels HTTP pour les API externes.
- **Python-dotenv** : Gestion des variables d’environnement.
- **Render** : Hébergement cloud de l’application.
- **Docker** : Conteneurisation pour déploiements locaux.

---

## Détails de la Phase 2

### 1. Analyse Exploratoire des Données (EDA)
- **Outil** : `Data_Cinelytics.ipynb`.
- **Activités** :
  - Extraction des données via `cinelytics_sdk` (ex. : `client.list_movies`, `client.list_ratings`).
  - Analyse des distributions de notes, genres populaires, et corrélations entre utilisateurs et films.
  - Identification des films les mieux notés et des tendances par genre.
- **Résultats** :
  - Statistiques clés : moyenne des notes, genres dominants, films populaires.
  - Insights pour orienter les visualisations dans `Data_Visualisations.ipynb`.

### 2. Visualisation des Données
- **Outil** : `Data_Visualisations.ipynb`.
- **Activités** :
  - Création de graphiques interactifs avec **Plotly** :
    - Histogrammes des distributions de notes.
    - Diagrammes en barres des genres populaires.
    - Nuages de points pour les relations films/tags.
  - Préparation des visualisations pour intégration dans l’application Streamlit.
- **Résultats** :
  - Visualisations dynamiques prêtes à être utilisées dans l’application.

### 3. Application Streamlit
- **Structure** : Application multi-pages dans `App_Streamlit/`.
  - **`App.py`** : Point d’entrée, configure la navigation entre les pages.
  - **`dashboard.py`** : Tableau de bord principal affichant un aperçu des insights.
  - **`page1.py`** : Recherche interactive de films par titre, genre, et note minimale, avec affichage des affiches via OMDb.
  - **`page2.py`** : Analyse des genres (popularité, notes moyennes par genre).
  - **`page3.py`** : Statistiques globales (nombre de films, évaluations, tags) et tendances via l’endpoint `/analytics`.
  - **`utils.py`** : Fonctions utilitaires (ex. : appels API, formatage des données).
- **Enrichissement** : Intégration de l’API OMDb pour récupérer les affiches et liens IMDb, stockés dans `output/links_enriched.parquet`.
- **Interface** : Utilisation des images dans `Images/` pour une UI attrayante (ex. : `profil.jpg`, `Phase_1.png`).
- **Livrable** : Application web accessible localement ou déployée sur Render.

---

## Mise en Place de l’Environnement

### Prérequis
- Python 3.11+
- VSCode (recommandé)
- Git
- Compte GitHub pour le contrôle de version
- Clé API OMDb ([obtenir ici](http://www.omdbapi.com/apikey.aspx))
- Compte Render (pour déploiement cloud, gratuit)

### Étapes d’Installation

1. **Cloner le Répertoire**
   ```bash
   git clone https://github.com/votre-username/cinelytics-dashboard.git
   cd cinelytics-dashboard
   ```

2. **Créer et Activer un Environnement Virtuel**
   ```bash
   python3 -m venv .venv
   .\venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Ouvrir dans VSCode**
   ```bash
   code .
   ```
   Sélectionnez l’interpréteur Python du `.venv` si demandé.

4. **Installer les Dépendances**
   Assurez-vous que `App_Streamlit/requirements.txt` contient :
   ```text
   cinelytics_sdk
   pandas
   plotly
   streamlit
   requests
   python-dotenv
   ```
   Installez :
   ```bash
   pip install -r App_Streamlit/requirements.txt
   ```

5. **Configurer l’API OMDb**
   Créez `App_Streamlit/.env` :
   ```env
   OMDB_API_KEY=votre_clé_ici
   MOVIE_API_BASE_URL=https://cinema-insights.onrender.com
   ```

6. **Vérifier les Notebooks**
   Assurez-vous que `dataanalysis/` contient :
   - `Data_Cinelytics.ipynb`
   - `Data_Visualisations.ipynb`
   Si absents, créez-les :
   ```bash
   mkdir dataanalysis
   touch dataanalysis/Data_Cinelytics.ipynb
   touch dataanalysis/Data_Visualisations.ipynb
   ```

7. **Lancer l’Application Streamlit**
   ```bash
   cd App_Streamlit
   streamlit run App.py
   ```
   Accédez à `http://localhost:8501`.

---

## Utilisation de l’Application

- **Tableau de Bord (`dashboard.py`)** : Aperçu des statistiques clés (nombre de films, notes moyennes).
- **Page 1 (`page1.py`)** : Recherche de films par titre, genre, ou note minimale, avec affichage des détails et affiches.
- **Page 2 (`page2.py`)** : Visualisations des genres populaires et des notes par genre.
- **Page 3 (`page3.py`)** : Statistiques globales et tendances (ex. : films les mieux notés).

**Exemple d’Utilisation du SDK dans un Notebook** :
```python
from cinelytics_sdk import MovieClient, MovieConfig
import pandas as pd

# Configurer le client
config = MovieConfig(movie_base_url="https://cinema-insights.onrender.com")
client = MovieClient(config=config)

# Vérifier la santé de l’API
print(client.health_check())

# Récupérer un film
movie = client.get_movie(1)
print(f"Film : {movie.title}")

# Lister les films en DataFrame
movies_df = client.list_movies(limit=10, output_format="pandas")
print(movies_df)
```

---

## Déploiement

### Cloud (Render)
1. Poussez `App_Streamlit` dans un répertoire GitHub.
2. Créez un service Web sur Render :
   - Langage : `Python 3`
   - Commande de Build : `pip install -r requirements.txt`
   - Commande de Démarrage : `streamlit run App.py --server.port $PORT --server.address 0.0.0.0`
   - Instance Type : `Free`
3. Ajoutez les variables d’environnement :
   ```env
   OMDB_API_KEY=votre_clé_ici
   MOVIE_API_BASE_URL=https://cinema-insights.onrender.com
   ```
4. Déployez et accédez via l’URL fournie (ex. : `https://cinelytics-app.onrender.com`).

### Docker
Créez `App_Streamlit/Dockerfile` :
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit", "run", "App.py", "--server.port", "80", "--server.address", "0.0.0.0"]
```
Construisez et exécutez :
```bash
cd App_Streamlit
docker build -t cinelytics-streamlit .
docker run -d -p 8501:80 --name cinelytics-streamlit-container cinelytics-streamlit
```
Accédez à `http://localhost:8501`.

---

## Réalisations Clés
- **Analyse Exploratoire** : Identification des tendances (notes, genres, préférences) via `Data_Cinelytics.ipynb`.
- **Visualisation Interactive** : Graphiques Plotly dans `Data_Visualisations.ipynb` et intégrés dans Streamlit.
- **Application Utilisateur** : Interface multi-pages avec recherche avancée et enrichissement OMDb.
- **Déploiement** : Application accessible localement ou sur Render, avec conteneurisation Docker.
- **Portfolio Impact** : Projet professionnel démontrant des compétences en analyse et visualisation.

---

## Pourquoi Ce Projet Se Démarque
Cette Phase 2 illustre ma capacité à transformer des données brutes en insights exploitables :
- **Expertise Technique** : Maîtrise de Pandas, Plotly, Streamlit, et intégration d’APIs externes.
- **Compétences Analytiques** : EDA rigoureuse pour identifier des tendances significatives.
- **Orientation Utilisateur** : Interface intuitive pour analystes et cinéphiles.
- **Professionnalisme** : Livrables soignés, prêts à être présentés à des recruteurs.

---

## Améliorations Futures
- **Recommandations** : Intégrer un modèle de machine learning pour des suggestions personnalisées.
- **Filtres Avancés** : Ajouter des options de filtrage par année, tags, ou utilisateurs.
- **Optimisation** : Utiliser un cache (ex. : Redis) pour améliorer les performances.
- **Visualisations** : Implémenter des heatmaps ou analyses temporelles.

---

## Liens Utiles
- 🌍 **API (Phase 1)** : [https://cinema-insights.onrender.com](https://cinema-insights.onrender.com)
- 📦 **PyPI (SDK)** : [https://pypi.org/project/cinelytics_sdk](https://pypi.org/project/cinelytics_sdk)
- 🌐 **Application Streamlit** : [(https://cinelytics-dashboard-by-k-kader.streamlit.app/)](https://cinelytics-dashboard-by-k-kader.streamlit.app/)

---

## Contact
Pour toute question ou collaboration, n’hésitez pas à me contacter :
- **LinkedIn** : [Koukou Kader Kouadio](https://www.linkedin.com/in/koukou-kader-kouadio-2a32371a4/)
- **Email** : [kkaderkouadio@gmail.com](mailto:kkaderkouadio@gmail.com)

---

Merci d’explorer la **Phase 2** de **Cinema_Insights** ! Ce projet reflète ma passion pour l’analyse de données et mon engagement à produire des solutions interactives de qualité professionnelle.
# DataScientest-MLOps-Test
Test d'entretient MLOps pour Data Scientest.

# Structure du projet 
```bash
DataScientest-MLOps-Test/
├── api/
│   ├── main.py         # Code de l'API FastAPI
│   └── model.pkl       # Modèle entraîné
├── notebooks/
│   └── train.ipynb     # Notebook d'entraînement
├── Dockerfile
├── requirements.txt
└── README.md
```


## Démarche du projet MLOps

Ce projet vise à transformer un modèle de Machine Learning en une API web facile à déployer et à utiliser. L'exemple choisi ici est la résolution d'un problème de classification des fleurs Iris en utilisant un modèle de Random Forest. Voici les étapes principales suivies pour rendre le modèle accessible :
​
### 1. Entraînement du modèle

Le modèle de classification (exemple : Random Forest sur le jeu de données Iris) est entraîné dans un notebook Python. Il apprend à prédire la classe d'une fleur à partir de ses caractéristiques.

### 2. Sauvegarde du modèle

Après l'entraînement, le modèle est sauvegardé sous le nom model.pkl grâce à la bibliothèque pickle. Cela permet de le recharger facilement plus tard sans le réentraîner.

### 3. Création de l’API FastAPI

Une application web est développée avec FastAPI. Elle expose un endpoint /predict : ce point d'entrée accepte des données au format JSON, applique le modèle et renvoie la prédiction sous forme de réponse JSON.

### 4. Conteneurisation avec Docker

L'ensemble du projet (API, environnement Python, dépendances, modèle) est intégré dans un conteneur Docker via un fichier Dockerfile. Cela permet un lancement simple et reproductible sur n'importe quelle machine Docker-compatible.

### 5. Documentation et exemples d’utilisation

Le fichier README.md détaille : le problème traité, les grandes étapes du projet, les commandes pour démarrer et utiliser l’application, des exemples de requêtes pour tester l’API (comme avec curl) et les choix techniques réalisés.

# Utilisation rapide 

Cloner ce dépôt.

Construire l’image Docker :
```bash
docker build -t iris-fastapi-app .
```

Lancer le conteneur : 
```bash
docker run -d -p 8000:8000 iris-fastapi-app
```

Tester l'API : 
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```


# Conclusion

Ce projet illustre comment on passe d’un simple modèle d’entraînement à une API web déployable et utilisable partout dans le but de réexploiter les prédictions faites par un modèle en temps réel, dans une appli web par exemple.
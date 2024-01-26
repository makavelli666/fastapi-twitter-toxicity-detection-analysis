
# Projet de Détection de Toxicité sur Twitter

Ce projet utilise FastAPI pour créer une API de traitement de commentaires Twitter, avec la détection de toxicité à l'aide du modèle Detoxify et l'enregistrement des commentaires non toxiques dans une base de données MongoDB.

## Prérequis

- Python 3.7 ou version ultérieure
- Clés d'API Twitter (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
- Serveur MongoDB en cours d'exécution

## Installation

1. Clonez le dépôt :

       git clone https://github.com/votre-utilisateur/projet-detoxification-twitter.git

 Installez les dépendances :

    

     cd projet-detoxification-twitter
     pip install -r requirements.txt

Configurez les clés d'API Twitter dans helpers.py.

Lancez l'application FastAPI :

    uvicorn main:app --reload

Utilisation

 Scrappez les commentaires Twitter :

    python main.py

 Les commentaires sont nettoyés, analysés pour la toxicité et enregistrés dans la base de données MongoDB.

  Pour utiliser l'API FastAPI, accédez à http://localhost:8000/docs dans votre navigateur.

Configuration

Assurez-vous de configurer correctement les paramètres dans helpers.py et d'avoir une base de données MongoDB en cours d'exécution.
Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
Licence

Ce projet est sous licence MIT.


N'oubliez pas d'adapter les sections en fonction des détails spécifiques 

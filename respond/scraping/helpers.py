#helpers.py
import requests
import csv
import tweepy
from bs4 import BeautifulSoup

# Configuration des clés d'API Twitter
CONSUMER_KEY = '...................................................'
CONSUMER_SECRET = '...................................................'
ACCESS_TOKEN = '...................................................'
ACCESS_TOKEN_SECRET = '...................................................'

def get_twitter_api():
    # Récupère l'API Twitter en utilisant les clés d'API
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)
    except tweepy.TweepError as e:
        print(f"Erreur lors de l'obtention de l'API Twitter : {str(e)}")
        return None

def scrape_twitter_comments(api, username, count=10000):
    # Récupère les tweets d'un utilisateur Twitter spécifié
    try:
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
        
        # Crée une liste de commentaires avec le nom d'utilisateur et le texte complet du tweet
        comments_list = [{'Username': tweet.user.screen_name, 'Comment': tweet.full_text} for tweet in tweets]
        return comments_list
    except tweepy.TweepError as e:
        print(f"Erreur lors de la récupération des tweets : {str(e)}")
        return []

def export_to_csv(data_list, filename='scraped_file.csv'):
    # Exporte les données vers un fichier CSV
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data_list[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
    except IOError as e:
        print(f"Erreur lors de l'exportation des données vers un fichier CSV : {str(e)}")

def send_file_to_fastapi(upload_url, file_path):
    # Envoie un fichier CSV à un serveur FastAPI
    try:
        files = {'file': open(file_path, 'rb')}
        response = requests.post(upload_url, files=files)
        
        # Vérifie le code de statut de la rvéponse
        if response.status_code == 200:
            print("Fichier envoyé avec succès au serveur FastAPI.")
        else:
            print(f"Échec de l'envoi du fichier au serveur FastAPI. Code de statut : {response.status_code}")
    except requests.RequestException as e:
        print(f"Erreur lors de l'envoi du fichier au serveur FastAPI : {str(e)}")

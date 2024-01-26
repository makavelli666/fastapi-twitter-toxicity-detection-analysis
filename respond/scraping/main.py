# main.py

from helpers import get_twitter_api, scrape_twitter_comments, export_to_csv, send_file_to_fastapi

if __name__ == "__main__":
    # Exemple d'utilisation du script pour récupérer les commentaires Twitter et les données du site web
    twitter_username = 'TwitterUsername'
    
    # Obtient l'API Twitter
    twitter_api = get_twitter_api()
    
    # Récupère les commentaires Twitter
    twitter_comments = scrape_twitter_comments(twitter_api, twitter_username)
    
    # Exporte les données vers un fichier CSV
    export_to_csv( twitter_comments, 'merged_data.csv')
    
    # Envoie le fichier CSV au serveur FastAPI
    send_file_to_fastapi('http://localhost:8000/uploadfile/', 'C:\\Users\\Desktop\\respond\\scraping\\merged_data.csv')

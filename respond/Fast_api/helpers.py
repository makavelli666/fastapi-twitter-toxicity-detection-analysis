# helpers.py

from fastapi import HTTPException, UploadFile
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient
import pandas as pd
import re
from detoxify import Detoxify

async def create_file_traitement(file: UploadFile, toxicity_model):
    try:
        # Connexion à la base de données MongoDB à l'intérieur de la fonction
        collection = AsyncIOMotorClient("mongodb://localhost:27017")["myDB"]["myColl"]

        #verife que cest un csv file 
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Le fichier doit être au format CSV.")
        
        content = await file.read()
        result = traitement_and_enregistrement_data(content.decode("utf-8"), collection, toxicity_model)

        return {"fichier": file.filename, "data_insere": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")

def traitement_and_enregistrement_data(csv_content, collection, toxicity_model):
    try:
        # Charger le contenu CSV dans un DataFrame Pandas et nettoyer les données
        df = clean_data(csv_content)
        # Appliquer la detoxification des commentaires
        df_non_toxic = detoxify_comments(df, toxicity_model)

        # Insérer les données non toxiques dans la base de données MongoDB
        result = collection.insert_many(df_non_toxic.to_dict(orient='records'))
        return len(result.inserted_ids)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")

def clean_data(csv_content):
    try:
        # Charger le contenu CSV dans un DataFrame Pandas
        df = pd.read_csv(pd.compat.StringIO(csv_content))
        
        # Nettoyer les données en supprimant les valeurs nulles et les duplicatas
        df_cleaned = df.dropna().drop_duplicates()

        # Appliquer la fonction de nettoyage du texte à la colonne 'Comment'
        df_cleaned['Comment'] = df_cleaned['Comment'].apply(clean_text)

        return df_cleaned
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")


def clean_text(text):
    try:
        # Supprimer les caractères non alphanumériques, convertir en minuscules et supprimer les espaces avant et après
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower().strip()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")

def detoxify_comments(data_frame, model_utulise, toxicity_lvl=0.8):
    try:
        # Prédiction de la toxicité pour chaque commentaire
        predictions = data_frame.apply(predict_toxicity, axis=1, toxicity_model=model_utulise)

        # Filtrer les commentaires non trop toxiques
        non_toxic_comments_df = data_frame[predictions < toxicity_lvl]

        return non_toxic_comments_df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")

def predict_toxicity(row, toxicity_model):
    try:
        # Concaténer les données du commentaire pour la prédiction
        content = row['Comment']  # Utilisez la colonne 'Comment' de votre DataFrame
        # Prédiction de la toxicité
        toxicity_results = toxicity_model.predict(content)
        return toxicity_results['toxic']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")


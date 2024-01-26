# app.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from helpers import create_file_traitement
from motor.motor_asyncio import AsyncIOMotorClient
from detoxify import Detoxify

app = FastAPI()

# Endpoint pour télécharger un fichier CSV
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Modèle de toxicité à utiliser
    toxicity_model = Detoxify('original')

    # Appel de la fonction de traitement définie dans helpers.py
    return await create_file_traitement(file, toxicity_model)

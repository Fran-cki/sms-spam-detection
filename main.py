from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

# 1. Charger le modèle exporté
model = joblib.load('detecteur_spam.pkl')

# ========================
# CONFIG APP
# ========================
app = FastAPI()

# Autoriser le frontend React à communiquer avec le backend FastAPI
# origins = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,      # les origines autorisées
    allow_origins=["*"],      # les origines autorisées
    allow_credentials=True,
    allow_methods=["*"],        # autorise toutes les méthodes HTTP
    allow_headers=["*"],        # autorise tous les headers
)

# 2. Définir le format de la donnée d'entrée
class DATA(BaseModel):
    text: str
    seuil: float = 0.85

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de détection de Spam"}

@app.post("/predict")
def predict_spam(data: DATA):
    # Récupérer la probabilité de spam
    # Le modèle attend une liste, on met donc [sms.text]
    proba_spam = model.predict_proba([data.text])[0][1]
    
    # On réutilise ton seuil de 0.85
    seuil = data.seuil
    is_spam = bool(proba_spam >= seuil)
    
    return {
        "message_analyse": data.text,
        "is_spam": is_spam,
        "confiance_spam": round(proba_spam, 4),
        "seuil_utilise": seuil
    }
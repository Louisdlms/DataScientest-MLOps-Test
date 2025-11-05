from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

# Charger le modèle
with open('api/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Définir le modèle de données pour la requête
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Endpoint de prédiction
@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}

from fastapi import FastAPI, HTTPException
import pickle, pandas as pd, os
from config import MODEL_PATH, DATA_PATH
app = FastAPI(title='Service Recommandation')
model = None
data = None
def load_model():
    global model, data
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
        if os.path.exists(DATA_PATH):
            data = pd.read_csv(DATA_PATH)
    except Exception as e:
        print(f'Erreur: {e}')
@app.on_event('startup')
async def startup_event():
    load_model()
@app.get('/health')
async def health():
    return {'status': 'ok', 'service': 'recommandation', 'model_loaded': model is not None}
@app.get('/recommendations/{user_id}')
async def get_recommendations(user_id: int):
    if data is None:
        return {'user_id': user_id, 'recommendations': [], 'message': 'Pas de donnees'}
    user_books = data[data['utilisateur_id'] == user_id]['livre_id'].tolist()
    all_books = data['livre_id'].unique().tolist()
    recommendations = [b for b in all_books if b not in user_books][:5]
    return {'user_id': user_id, 'recommendations': recommendations}
@app.post('/train')
async def train_model():
    load_model()
    return {'message': 'Modele recharge'}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5004)

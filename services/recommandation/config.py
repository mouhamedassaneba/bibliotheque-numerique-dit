import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv('MODEL_PATH', '../../models/model.pkl')
DATA_PATH = os.getenv('DATA_PATH', '../../data/processed/loans_clean.csv')
PORT = int(os.getenv('PORT', 5004))

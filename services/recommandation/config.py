import os
from dotenv import load_dotenv
<<<<<<< HEAD

load_dotenv()

MODEL_PATH = os.getenv('MODEL_PATH', '../../models/model.pkl')
DATA_PATH = os.getenv('DATA_PATH', '../../data/processed/loans_clean.csv')
=======
load_dotenv()
MODEL_PATH = os.getenv('MODEL_PATH', '/app/models/model.pkl')
DATA_PATH = os.getenv('DATA_PATH', '/app/data/processed/loans_clean.csv')
>>>>>>> feature/docker
PORT = int(os.getenv('PORT', 5004))

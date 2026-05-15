import pandas as pd
import pickle
import os
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import numpy as np

os.makedirs('models', exist_ok=True)

df = pd.read_csv('data/processed/loans_clean.csv')
users = df['utilisateur_id'].unique()
books = df['livre_id'].unique()
user_idx = {u: i for i, u in enumerate(users)}
book_idx = {b: i for i, b in enumerate(books)}
rows = [user_idx[u] for u in df['utilisateur_id']]
cols = [book_idx[b] for b in df['livre_id']]
data = [1] * len(df)
matrix = csr_matrix((data, (rows, cols)), shape=(len(users), len(books)))
model = TruncatedSVD(n_components=2)
model.fit(matrix)
with open('models/model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'user_idx': user_idx, 'book_idx': book_idx}, f)
print("Modele entraine et sauvegarde dans models/model.pkl")

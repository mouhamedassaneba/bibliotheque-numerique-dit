import pandas as pd
import pickle
import json
import numpy as np
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix

df = pd.read_csv('data/processed/loans_clean.csv')
with open('models/model.pkl', 'rb') as f:
    saved = pickle.load(f)

model = saved['model']
user_idx = saved['user_idx']
book_idx = saved['book_idx']
rows = [user_idx[u] for u in df['utilisateur_id']]
cols = [book_idx[b] for b in df['livre_id']]
data = [1] * len(df)
matrix = csr_matrix((data, (rows, cols)), shape=(len(user_idx), len(book_idx)))
transformed = model.transform(matrix)
reconstructed = model.inverse_transform(transformed)
original = matrix.toarray()
mse = np.mean((original - reconstructed) ** 2)
rmse = float(np.sqrt(mse))
mae = float(np.mean(np.abs(original - reconstructed)))
metrics = {'rmse': rmse, 'mae': mae}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)
print(f"RMSE: {rmse:.4f}, MAE: {mae:.4f}")

import pandas as pd
import os

os.makedirs('data/processed', exist_ok=True)

df = pd.read_csv('data/raw/loans.csv')
df = df.dropna()
df = df[df['statut'] == 'retourne']
df['utilisateur_id'] = df['utilisateur_id'].astype(int)
df['livre_id'] = df['livre_id'].astype(int)
df.to_csv('data/processed/loans_clean.csv', index=False)
print(f"Donnees nettoyees: {len(df)} lignes")

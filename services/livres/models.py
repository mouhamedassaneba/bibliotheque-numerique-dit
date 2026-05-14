from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Livre(db.Model):
    __tablename__ = 'livres'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    genre = db.Column(db.String(50))
    annee_publication = db.Column(db.Integer)
    nombre_exemplaires = db.Column(db.Integer, default=1)
    disponible = db.Column(db.Boolean, default=True)
    date_ajout = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'isbn': self.isbn,
            'genre': self.genre,
            'annee_publication': self.annee_publication,
            'nombre_exemplaires': self.nombre_exemplaires,
            'disponible': self.disponible,
            'date_ajout': self.date_ajout.isoformat()
        }

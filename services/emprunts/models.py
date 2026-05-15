from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Emprunt(db.Model):
    __tablename__ = 'emprunts'

    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, nullable=False)
    livre_id = db.Column(db.Integer, nullable=False)
    date_emprunt = db.Column(db.DateTime, default=datetime.utcnow)
    date_retour_prevue = db.Column(db.DateTime, nullable=False)
    date_retour_effectif = db.Column(db.DateTime, nullable=True)
    statut = db.Column(db.String(20), default='en_cours')

    def to_dict(self):
        return {
            'id': self.id,
            'utilisateur_id': self.utilisateur_id,
            'livre_id': self.livre_id,
            'date_emprunt': self.date_emprunt.isoformat(),
            'date_retour_prevue': self.date_retour_prevue.isoformat(),
            'date_retour_effectif': self.date_retour_effectif.isoformat() if self.date_retour_effectif else None,
            'statut': self.statut
        }

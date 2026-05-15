from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
<<<<<<< HEAD

db = SQLAlchemy()

class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'

=======
db = SQLAlchemy()
class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'
>>>>>>> feature/docker
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telephone = db.Column(db.String(20))
    type_utilisateur = db.Column(db.String(20), nullable=False, default='Etudiant')
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)
    actif = db.Column(db.Boolean, default=True)
<<<<<<< HEAD

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'telephone': self.telephone,
            'type_utilisateur': self.type_utilisateur,
            'date_inscription': self.date_inscription.isoformat(),
            'actif': self.actif
        }
=======
    def to_dict(self):
        return {'id': self.id, 'nom': self.nom, 'prenom': self.prenom, 'email': self.email, 'telephone': self.telephone, 'type_utilisateur': self.type_utilisateur, 'date_inscription': self.date_inscription.isoformat(), 'actif': self.actif}
>>>>>>> feature/docker

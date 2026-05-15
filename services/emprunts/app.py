from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Emprunt
from config import Config
from datetime import datetime, timedelta
<<<<<<< HEAD

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'emprunts'}), 200

=======
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'emprunts'}), 200
>>>>>>> feature/docker
@app.route('/emprunts', methods=['GET'])
def get_emprunts():
    emprunts = Emprunt.query.all()
    return jsonify([e.to_dict() for e in emprunts]), 200
<<<<<<< HEAD

=======
>>>>>>> feature/docker
@app.route('/emprunts/<int:id>', methods=['GET'])
def get_emprunt(id):
    e = Emprunt.query.get_or_404(id)
    return jsonify(e.to_dict()), 200
<<<<<<< HEAD

=======
>>>>>>> feature/docker
@app.route('/emprunts', methods=['POST'])
def add_emprunt():
    data = request.get_json()
    date_retour = datetime.utcnow() + timedelta(days=14)
    e = Emprunt(utilisateur_id=data['utilisateur_id'], livre_id=data['livre_id'], date_retour_prevue=date_retour)
    db.session.add(e)
    db.session.commit()
    return jsonify(e.to_dict()), 201
<<<<<<< HEAD

=======
>>>>>>> feature/docker
@app.route('/emprunts/<int:id>/retour', methods=['PUT'])
def retour_emprunt(id):
    e = Emprunt.query.get_or_404(id)
    e.date_retour_effectif = datetime.utcnow()
    e.statut = 'retourne'
    db.session.commit()
    return jsonify(e.to_dict()), 200
<<<<<<< HEAD

=======
>>>>>>> feature/docker
@app.route('/emprunts/utilisateur/<int:user_id>', methods=['GET'])
def get_emprunts_utilisateur(user_id):
    emprunts = Emprunt.query.filter_by(utilisateur_id=user_id).all()
    return jsonify([e.to_dict() for e in emprunts]), 200
<<<<<<< HEAD

=======
>>>>>>> feature/docker
@app.route('/emprunts/retards', methods=['GET'])
def get_retards():
    now = datetime.utcnow()
    retards = Emprunt.query.filter(Emprunt.date_retour_prevue < now, Emprunt.statut == 'en_cours').all()
    return jsonify([e.to_dict() for e in retards]), 200
<<<<<<< HEAD

=======
>>>>>>> feature/docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

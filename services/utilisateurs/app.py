from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Utilisateur
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'utilisateurs'}), 200
@app.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    return jsonify([u.to_dict() for u in utilisateurs]), 200
@app.route('/utilisateurs/<int:id>', methods=['GET'])
def get_utilisateur(id):
    u = Utilisateur.query.get_or_404(id)
    return jsonify(u.to_dict()), 200
@app.route('/utilisateurs', methods=['POST'])
def add_utilisateur():
    data = request.get_json()
    u = Utilisateur(nom=data['nom'], prenom=data['prenom'], email=data['email'], telephone=data.get('telephone'), type_utilisateur=data.get('type_utilisateur', 'Etudiant'))
    db.session.add(u)
    db.session.commit()
    return jsonify(u.to_dict()), 201
@app.route('/utilisateurs/<int:id>', methods=['PUT'])
def update_utilisateur(id):
    u = Utilisateur.query.get_or_404(id)
    data = request.get_json()
    u.nom = data.get('nom', u.nom)
    u.prenom = data.get('prenom', u.prenom)
    u.type_utilisateur = data.get('type_utilisateur', u.type_utilisateur)
    db.session.commit()
    return jsonify(u.to_dict()), 200
@app.route('/utilisateurs/<int:id>', methods=['DELETE'])
def delete_utilisateur(id):
    u = Utilisateur.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({'message': 'Utilisateur supprime'}), 200
@app.route('/utilisateurs/type/<string:type_u>', methods=['GET'])
def get_by_type(type_u):
    utilisateurs = Utilisateur.query.filter_by(type_utilisateur=type_u).all()
    return jsonify([u.to_dict() for u in utilisateurs]), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

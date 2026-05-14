from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Livre
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'livres'}), 200

@app.route('/livres', methods=['GET'])
def get_livres():
    livres = Livre.query.all()
    return jsonify([l.to_dict() for l in livres]), 200

@app.route('/livres/<int:id>', methods=['GET'])
def get_livre(id):
    livre = Livre.query.get_or_404(id)
    return jsonify(livre.to_dict()), 200

@app.route('/livres', methods=['POST'])
def add_livre():
    data = request.get_json()
    livre = Livre(titre=data['titre'], auteur=data['auteur'], isbn=data['isbn'], genre=data.get('genre'), annee_publication=data.get('annee_publication'), nombre_exemplaires=data.get('nombre_exemplaires', 1))
    db.session.add(livre)
    db.session.commit()
    return jsonify(livre.to_dict()), 201

@app.route('/livres/<int:id>', methods=['PUT'])
def update_livre(id):
    livre = Livre.query.get_or_404(id)
    data = request.get_json()
    livre.titre = data.get('titre', livre.titre)
    livre.auteur = data.get('auteur', livre.auteur)
    livre.genre = data.get('genre', livre.genre)
    livre.nombre_exemplaires = data.get('nombre_exemplaires', livre.nombre_exemplaires)
    livre.disponible = data.get('disponible', livre.disponible)
    db.session.commit()
    return jsonify(livre.to_dict()), 200

@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    livre = Livre.query.get_or_404(id)
    db.session.delete(livre)
    db.session.commit()
    return jsonify({'message': 'Livre supprime avec succes'}), 200

@app.route('/livres/recherche', methods=['GET'])
def recherche_livre():
    titre = request.args.get('titre')
    auteur = request.args.get('auteur')
    isbn = request.args.get('isbn')
    query = Livre.query
    if titre:
        query = query.filter(Livre.titre.ilike('%' + titre + '%'))
    if auteur:
        query = query.filter(Livre.auteur.ilike('%' + auteur + '%'))
    if isbn:
        query = query.filter(Livre.isbn == isbn)
    livres = query.all()
    return jsonify([l.to_dict() for l in livres]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

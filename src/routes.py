from flask import Blueprint, request, jsonify
from .models import Game
from . import db
from datetime import datetime

games_bp = Blueprint('games', __name__)

# lister les jeux
@games_bp.route('/get_games', methods=['GET'])
def get():
    games = Game.query.all()
    return jsonify([{
        'id': game.id,
        'name': game.name,
        'release_date': game.release_date,
        'studio': game.studio,
        'ratings': game.ratings,
        'platforms': game.platforms
    } for game in games]), 200

# ajouter un jeu
@games_bp.route('/add_game', methods=['POST'])
def add():
    data = request.get_json()
    if not data.get('name'):
        return jsonify({"error": "Le jeu doit avoir un nom !"}), 400
    try:
        release_date = datetime.strptime(data['release_date'], '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Le format de la date de parution est incorrect !"}), 400
    new = Game(
        name=data['name'],
        release_date=release_date,
        studio=data['studio'],
        ratings=data['ratings'],
        platforms=data['platforms']
    )
    db.session.add(new)
    db.session.commit()
    return jsonify({
        'id': new.id,
        'name': new.name,
        'release_date': new.release_date,
        'studio': new.studio,
        'ratings': new.ratings,
        'platforms': new.platforms
    }), 201

# modifier un jeu existant
@games_bp.route('/modif_game/<int:id>', methods=['PUT'])
def update(id):
    game = Game.query.get(id)
    if not game:
        return jsonify({"error": "Jeu inexistant :("}), 404

    data = request.get_json()

    game.name = data.get('name', game.name)
    game.release_date = datetime.strptime(data['release_date'], '%Y-%m-%d') if 'release_date' in data else game.release_date
    game.studio = data.get('studio', game.studio)
    game.ratings = data.get('ratings', game.ratings)
    game.platforms = data.get('platforms', game.platforms)

    db.session.commit()
    return jsonify({
        'id': game.id,
        'name': game.name,
        'release_date': game.release_date,
        'studio': game.studio,
        'ratings': game.ratings,
        'platforms': game.platforms
    }), 200

# supprimer un jeu existant
@games_bp.route('/del_game/<int:id>', methods=['DELETE'])
def delete(id):
    game = Game.query.get(id)
    if not game:
        return jsonify({"error": "Jeu inexistant :("}), 404
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Jeu supprimé !'}), 200

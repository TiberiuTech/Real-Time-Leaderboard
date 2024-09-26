from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from auth import auth_bp
from leaderboard import add_score, get_top_players, get_rank

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Real-Time Leaderboard API")

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/leaderboard/submit', methods=['POST'])
@jwt_required()
def submit_score():
    current_user = get_jwt_identity()
    data = request.get_json()
    score = data.get('score')

    if score is None:
        return jsonify({"msg": "Score is required"}), 400
    
    add_score(current_user, score)
    return jsonify({"msg": "Score submitted successfully"}), 200

@app.route('/leaderboard/top/<int:n>', methods=['GET'])
def top_players(n):
    top_n = get_top_players(n)
    return jsonify(top_n), 200

@app.route('/leaderboard/rank', methods=['GET'])
@jwt_required()
def user_rank():
    current_user = get_jwt_identity()  
    rank = get_rank(current_user)
    return jsonify(rank=rank), 200

if __name__ == '__main__':
    app.run(debug=True)

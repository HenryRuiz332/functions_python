from flask import Flask
from flask import jsonify
from models import db

from config import config
#importamos config, está en la misma carpeta raíz

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

enviroment = config['development'] 
app = create_app(enviroment)




app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)



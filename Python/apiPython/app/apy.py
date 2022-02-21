from flask import Flask
from flask_restful import Resource, Api



import route

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        return {"Hello":name}


api.add_resource(Hello, '/hello/<name>')




def hello(name):
    info = requests.get('http://localhost:5000/hello/'+name)
    return info.text



if __name__ == '__main__':
 app.run(debug=True)


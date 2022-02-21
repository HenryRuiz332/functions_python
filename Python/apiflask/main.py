from flask import Flask
import json
app = Flask(__name__)
## los metodos iran luego de esta linea
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/auth/login",methods=['POST'])
def log_auth():
    values = request.get_json()
    if values['usuario'] == 'admin' and values['clave'] == 'top_secret':
        respuesta = {'error':False,'mensaje':'Auser logged'}
        return json.dumps(respuesta)
    respuesta = {'error':True,'mensaje':'Fail Auth'}
    return json.dumps(values)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about',methods=['GET'])
def about():
    return 'Página Sobre'

debugando = __name__ == '__main__'
app.run(debug=debugando)


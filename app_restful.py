from flask import Flask
from flask_restful import Api
from desenvolvedores import Desenvolvedor, ListaDesenvolvedores
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)
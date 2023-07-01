from flask import Flask, request
from flask_restful import Resource
import json


desenvolvedores = [
    {
        'id' : 0,
        'nome' : 'Gabriel',
        'habilidades' : ['Python', 'Flask']
    },
    {
        'id' : 1,
        'nome' : 'Rafael',
        'habilidades' : ['Python', 'Flask']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID { } não existe'. format(id)
            response = {'status': 'erro', 'mensagem' : mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Proucure o administrador da API'
            response = {'status' : 'erro', 'mensagem' : mensagem}
        
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status' : 'sucesso', 'mensagem' : 'Registro excluído'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)

        return desenvolvedores[posicao]

from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

lista_asteroides = [
    {
        'id':0,
        'nome': 'Ceres',
        'diametroKM':939.4
    },
    {
        'id':1,
        'nome': 'Pallas',
        'diametroKM':511
    },
    {
        'id':2,
        'nome': 'Juno',
        'diametroKm':254
    },
    {
        'id':3,
        'nome': 'Vesta',
        'diametroKM':525.4
    }
]

# Devolve um asteróide pelo ID, também altera e deleta um asteróide
class Asteroides(Resource):
    def get(self, id):
        try:
            response = lista_asteroides[id]
        except IndexError:
            mensagem = 'Asteroide de ID {} nao existe'.format(id)
            response = {'status':'Erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_asteroides[id] = dados
        return dados

    def delete(self, id):
        lista_asteroides.pop(id)
        return {'status':'Sucesso', 'mensagem':'Registro excluido'}

#Lista todos os asteróides e permite registrar um novo
class ListaAsteroides(Resource):
    def get(self):
        return lista_asteroides

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_asteroides)
        dados['id'] = posicao
        lista_asteroides.append(dados)
        return lista_asteroides[posicao]

api.add_resource(Asteroides, '/asteroide/<int:id>/')
api.add_resource(ListaAsteroides, '/asteroide/')

if __name__ == '__main__':
    app.run(debug=True)
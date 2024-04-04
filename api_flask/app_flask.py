from flask import Flask, jsonify, request
import json

app = Flask(__name__)

asteroides = [
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
@app.route('/asteroide/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def asteroide(id):
    if request.method == 'GET':
        try:
            response = asteroides[id]
        except IndexError:
            mensagem = 'Asteroide de ID {} nao existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        asteroides[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        asteroides.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluido'})

#Lista todos os asteróides e permite registrar um novo
@app.route('/asteroide', methods=['POST','GET'])
def lista_asteroides():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(asteroides)
        dados['id'] = posicao
        asteroides.append(dados)
        return jsonify(asteroides[posicao])
    elif request.method == 'GET':
        return jsonify(asteroides)

# Página inicial
@app.route('/')
def Home():
    return '<h1> Olá, sou um Flask API de asteróides!<h1>'    

if __name__=='__main__':
    app.run(debug=True)



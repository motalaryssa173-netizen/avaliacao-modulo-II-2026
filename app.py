from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "ano": 2011
    },
    {
        "id": 2,
        "titulo": "Super Mario Odyssey",
        "genero": "Plataforma",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    },
    {
        "id": 3,
        "titulo": "Rocket League",
        "genero": "Esporte",
        "plataforma": "Multiplataforma",
        "ano": 2015  
    }
]

# Listar os jogos 

@app.route("/api/jogos", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

# Buscar os jogos

@app.route("/api/jogos/<int:id>", methods=["GET"])
def buscar_jogos(id):
    jogo = next((l for l in jogos if l['id'] == id), None)
    if jogo: 
        return jsonify(jogo)
    return jsonify({"erro": "Jogo nao encontrado"}), 404

# Cadastrar um novo jogo

@app.route("/api/jogos", methods=["POST"])
def criar_jogo():
    dados = request.get_json()
    novo_jogo = {
        'id': len(jogos) + 1,
        'titulo': dados['titulo'],
        'genero': dados['genero'],
        'plataforma': dados['plataforma'],
        'ano': dados['ano']
    }
    jogos.append(novo_jogo)
    return jsonify(novo_jogo), 201

#Atualizar um jogo

@app.route("/api/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id):
    jogo = next((l for l in jogos if l['id'] == id), None) 
    if not jogo:
        return jsonify({"erro" : "Jogo não encontrado."}), 404

    dados = request.get_json()
    jogo["titulo"] = dados.get("titulo", jogo["titulo"])
    jogo["genero"] = dados.get("genero", jogo["genero"])
    jogo["plataforma"] = dados.get("plataforma", jogo["plataforma"])
    jogo["ano"] = dados.get("ano", jogo["ano"])

    return jsonify(jogos)

# Deletar jogo

@app.route("/api/jogos/<int:id>", methods=["DELETE"])
def excluir_jogo(id):
    global jogos
    jogo = next((j for j in jogos if j['id'] == id), None)
    if not jogo:
        return jsonify ({"erro": "Jogo não encontrado."}), 404

    jogos = [j for j in jogos if j ["id"] != id]
    return jsonify({"mensagem": "Jogo excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
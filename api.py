from flask import Flask, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user="root",
    password="87015119k",
    database="db_apiLivros"
)
cursor = mydb.cursor()

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'HP, E a Pedra Filosofal.',
        'autor': 'J.K Rolling'
    },
    {
        'id': 2,
        'titulo': 'HP, E a Camara Secreta.',
        'autor': 'J.K Rolling'
    }
]

for livro in livros:
    query = "INSERT INTO livros (id, titulo, autor) VALUES (%s, %s, %s)"
    values = (livro['id'], livro['titulo'], livro['autor'])
    cursor.execute(query, values)
    mydb.commit()

cursor.execute("SELECT * FROM livros")
existing_ids = [row[0] for row in cursor.fetchall()]

livros = []
for livro in livros:
    if livro['id'] not in existing_ids:
        query = "INSERT INTO livros (id, titulo, autor) VALUES (%s, %s, %s)"
        values = (livro['id'], livro['titulo'], livro['autor'])
        cursor.execute(query, values)
        mydb.commit()
    livros.append(livro)
"""Consulta generica"""


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


"""Consulta por id"""


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


"""Editar"""


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    query = "UPDATE livros SET titulo = %s, autor = %s WHERE id = %s"
    values = (livro_alterado['titulo'], livro_alterado['autor'], id)
    cursor.execute(query, values)
    mydb.commit()


"""Criar"""


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    query = "INSERT INTO livros (id, titulo, autor) VALUES (%s, %s, %s)"
    values = (novo_livro['id'], novo_livro['titulo'], novo_livro['autor'])
    cursor.execute(query, values)
    livros.append(novo_livro)
    mydb.commit()
    return jsonify(livros)


"""Excluir"""


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    query = "DELETE FROM livros WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    mydb.commit()
    return jsonify(livros,  {'message': 'Livro excluído com sucesso'})


app.run(port=8080, host='localhost', debug=True)

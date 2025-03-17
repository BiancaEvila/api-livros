from flask import Flask, request, jsonify

import sqlite3

app = Flask(__name__)


@app.route("/")
def exiba_mensagem():
    return "<h1>API Livros Vai Na Web</h1>"

def init_db():
    # Conecte o sqlite3 no arquivo database.db com a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                imagem_url TEXT NOT NULL
            )
    """)
        
init_db()

@app.route("/doar", methods =["POST"])

def doar():
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("image_url")

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
            INSERT INTO LIVROS(titulo, categoria, autor, imagem_url)
            VALUES ("{titulo}", "{categoria}", "{autor}", "{imagem_url}")
    """)
        
    return jsonify({"mensagem:""Livro cadastrado com sucesso"}), 201


#Se o app.py for o arquivo principal da API:
# Execute o app.run com o modo debug ativado
if __name__ == "__main__":
    app.run(debug=True)
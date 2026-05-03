from flask import Flask, jsonify, request
from models.Avicultor import Avicultor
import sqlite3

DATABASE_NAME = "avicola.db"

app = Flask(__name__)


@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200


@app.get("/avicultores")
def getAvicultores():
    avicultores = []

    # DB
    conn = None
    try:
        # 1 - Abrir a conexão
        conn = sqlite3.connect(DATABASE_NAME)

        # 2 - Recuperar o cursor
        cursor = conn.cursor()

        # 3 - Preparar a consultar: query | statement
        cursor.execute("select * from tb_avicultores")

        # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
        rows = cursor.fetchall()
        avicultores = []
        for row in rows:
            id = row[0]
            nome = row[1]
            nascimento = row[2]
            cpf = row[3]
            caf = row[4]
            avicultor = Avicultor(id, nome, nascimento, cpf, caf)
            avicultores.append(avicultor.toDict())
        # 4.2 - Confirmar a operação

    except sqlite3.Error as e:
        print(e)
    finally:
        # 5 - Fechar a conexão
        if conn:
            conn.close()

    return avicultores, 200


@app.post("/avicultores")
def postAvicultores():

    avicultorJson = request.get_json()

    # DB
    conn = None
    try:
        # 1 - Abrir a conexão
        conn = sqlite3.connect(DATABASE_NAME)

        # 2 - Recuperar o cursor
        cursor = conn.cursor()

        # 3 - Preparar a consultar: query | statement
        cursor.execute("INSERT INTO tb_avicultores (name, nascimento, cpf, caf) VALUES(?,?,?,?)", ("João","2000-01-01","12345678974","11122233344"))

        # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
        rows.cursor.fetchall()
        avicultores = []
        for row in rows:
            id = row[0]
            nome = row[1]
            nascimento[2]
            cpf[3]
            caf[4]
            avicultor = Avicultor(id, nome, nascimento, cpf, caf)
            avicultores.append(avicultor.toDict())
        # 4.2 - Confirmar a operação

    except sqlite3.Error as e:
        print(e)
    finally:
        # 5 - Fechar a conexão
        if conn:
            conn.close()


@app.put("/avicultores")
def putAvicultores():
    pass


@app.delete("/avicultores")
def deleteAvicultores():
    pass

if __name__ == "__main__":
    app.run(debug=True)

# /avicultores - nome, cpf, caf, nascimento
# /avicolas
# /aviarios ou /galpoes

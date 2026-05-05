from flask import jsonify, request
import sqlite3
import json
import os

from models.Avicultor import Avicultor
from helpers.application import app
from models.database import get_conn


@app.get("/avicultores")
def getAvicultores():
    avicultores = []
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_avicultores")
        rows = cursor.fetchall()
        for row in rows:
            avicultor = Avicultor(row[0], row[1], row[2], row[3], row[4])
            avicultores.append(avicultor.toDict())
    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
    return jsonify(avicultores), 200

@app.post("/avicultores")
def postAvicultores():
    avicultorJson = request.get_json()
    conn = None 
    try:
        conn = get_conn() 
        cursor = conn.cursor()
        query = "INSERT INTO tb_avicultores (name, nascimento, cpf, caf) VALUES(?,?,?,?)"
        params = (avicultorJson['nome'], avicultorJson['nascimento'], avicultorJson['cpf'], avicultorJson['caf'])
        cursor.execute(query, params)
        conn.commit()

        novo_id = cursor.lastrowid
        avicultorJson['id'] = novo_id
        return jsonify(avicultorJson), 201 

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.put("/avicultores/<int:id>")
def putAvicultores(id):
    avicultorJson = request.get_json()
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        # Query para atualizar os dados baseada no ID da URL
        query = "UPDATE tb_avicultores SET name = ?, nascimento = ?, cpf = ?, caf = ? WHERE id = ?"
        params = (avicultorJson['nome'], avicultorJson['nascimento'], avicultorJson['cpf'], avicultorJson['caf'], id)
        
        cursor.execute(query, params)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Avicultor não encontrado"}), 404

        avicultorJson['id'] = id
        return jsonify(avicultorJson), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.delete("/avicultores/<int:id>")
def deleteAvicultores(id):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        query = "DELETE FROM tb_avicultores WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Avicultor não encontrado"}), 404

        return jsonify({"message": "Avicultor removido com sucesso", "id": id}), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)
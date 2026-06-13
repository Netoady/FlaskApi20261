from flask import Blueprint
import sqlite3
from flask import request, jsonify
from marshmallow import ValidationError

from models.Avicula import Avicula, AviculaSchema
from services.AviculaService import AviculaService
from helpers.database import get_conn
from helpers.logger import logger

avicula_bp = Blueprint('avicula', __name__, url_prefix='aviculas')

@avicula_bp.get("/")
def getAviculas():
    aviculas = []
    conn = None

    
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_aviculas")
        rows = cursor.fetchall()
        for row in rows:
            avicula = Avicula(row[0], row[1], row[2], row[3])
            aviculas.append(avicula.toDict())
    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
    return jsonify(aviculas), 200

@avicula_bp.post("/")
def postAviculas():
    aviculaJson = request.get_json()
    conn = None 
    try:

        AviculaSchema = AviculaSchema()
        aviculaData = aviculaSchema.load(aviculaJson)

        #Abrir a conexão
        conn = get_conn() 
        
        #Recuperar o cursor
        cursor = conn.cursor()

        query = "INSERT INTO tb_aviculas (name, cnpj, endereco) VALUES(?,?,?)"
        params = (avicultorJson['nome'], avicultorJson['cnpj'], avicultorJson['endereco'])
        cursor.execute(query, params)
        conn.commit()

        novo_id = cursor.lastrowid
        aviculaJson['id'] = novo_id
        return jsonify(aviculaJson), 201 

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@avicula_bp.put("/<int:id>")
def putAviculas(id):
    aviculaJson = request.get_json()
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        # Query para atualizar os dados baseada no ID da URL
        query = "UPDATE tb_aviculas SET name = ?, cnpj = ?, endereco = ?"
        params = (aviculaJson['nome'], aviculaJson['cnpj'], aviculaJson['endereco'], id)
        
        cursor.execute(query, params)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Avicula não encontrado"}), 404

        avicultorJson['id'] = id
        return jsonify(aviculaJson), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@avicula_bp.delete("/<int:id>")
def deleteAviculas(id):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        query = "DELETE FROM tb_aviculas WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Avicula não encontrado"}), 404

        return jsonify({"message": "Avicula removido com sucesso", "id": id}), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
from flask import Blueprint
import sqlite3
from flask import request, jsonify
from marshmallow import ValidationError

from models.Aviario import Aviario, AviarioSchema
from services.AviarioService import AviarioService
from helpers.database import get_conn
from helpers.logger import logger

aviario_bp = Blueprint('aviario', __name__, url_prefix='aviarios')

@aviario_bp.get("/")
def getAviarios():
    aviarios = []
    conn = None

    
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_aviarios")
        rows = cursor.fetchall()
        for row in rows:
            aviario = Aviario(row[0], row[1], row[2])
            aviarios.append(aviario.toDict())
    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
    return jsonify(aviarios), 200

@aviario_bp.post("/")
def postAviarios():
    aviarioJson = request.get_json()
    conn = None 
    try:

        AviarioSchema = AviarioSchema()
        aviarioData = aviarioSchema.load(aviarioJson) # Caso falte campo, o erro é gerado aqui

        #Abrir a conexão
        conn = get_conn() 
        
        #Recuperar o cursor
        cursor = conn.cursor()

        query = "INSERT INTO tb_aviarios (name, capacidade) VALUES(?,?)"
        params = (aviarioJson['nome'], aviarioJson['capacidade'])

        cursor.execute(query, params)
        conn.commit()

        novo_id = cursor.lastrowid
        aviarioJson['id'] = novo_id
        return jsonify(aviarioJson), 201 

    except sqlite3.Error as e: # Aqui é pra capturar erros de validação do banco
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@aviario_bp.put("/<int:id>")
def putAviarios(id):
    aviarioJson = request.get_json()
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        # Query para atualizar os dados baseada no ID da URL
        query = "UPDATE tb_aviarios SET name = ?, capacidade = ?, WHERE id = ?"
        params = (aviarioJson['nome'], aviarioJson['capacidade'], id)
        
        cursor.execute(query, params)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Aviario não encontrado"}), 404

        avicultorJson['id'] = id
        return jsonify(aviarioJson), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@aviario_bp.delete("/<int:id>")
def deleteAviarios(id):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        query = "DELETE FROM tb_aviarios WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Aviario não encontrado"}), 404

        return jsonify({"message": "Aviario removido com sucesso", "id": id}), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
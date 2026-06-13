from flask import Blueprint
import sqlite3
from flask import request, jsonify
from marshmallow import ValidationError

from models.Galpao import Galpao, GalpaoSchema
from services.GalpaoService import GalpaoService
from helpers.database import get_conn
from helpers.logger import logger

galpao_bp = Blueprint('galpao', __name__, url_prefix='galpao')

@app.get("/")
def getGalpoes():
    galpoes = []
    conn = None

    
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_galpoes")
        rows = cursor.fetchall()
        for row in rows:
            galpao = Galpao(row[0], row[1], row[2])
            galpoes.append(galpao.toDict())
    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
    return jsonify(galpoes), 200

@app.post("/")
def postGalpoes():
    galpaoJson = request.get_json()
    conn = None 
    try:

        GalpaoSchema = GalpaoSchema()
        galpaoData = galpaoSchema.load(galpaoJson)

        #Abrir a conexão
        conn = get_conn() 
        
        #Recuperar o cursor
        cursor = conn.cursor()

        query = "INSERT INTO tb_galpoes (identificador, area_m2) VALUES(?,?)"
        params = (galpaoJson['identificador'], galpaoJson['area_m2'])
        cursor.execute(query, params)
        conn.commit()

        novo_id = cursor.lastrowid
        galpaoJson['id'] = novo_id
        return jsonify(galpaoJson), 201 

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.put("/<int:id>")
def putGalpoes(id):
    galpaoJson = request.get_json()
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        # Query para atualizar os dados baseada no ID da URL
        query = "UPDATE tb_galpoes SET identificador = ?, area_m2 = ?"
        params = (galpaoJson['identificador'], galpaoJson['area_m2'], id)
        
        cursor.execute(query, params)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Galpao não encontrado"}), 404

        galpaoJson['id'] = id
        return jsonify(galpaoJson), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.delete("/<int:id>")
def deleteGalpoes(id):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        query = "DELETE FROM tb_galpoes WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Galpao não encontrado"}), 404

        return jsonify({"message": "Galpao removido com sucesso", "id": id}), 200

    except sqlite3.Error as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
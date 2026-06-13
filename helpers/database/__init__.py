import sqlite3
from flask import g 
from helpers.application import app
from helpers.enviroment import enviroment


DATABASE_NAME = enviroment.get("DATABASE_NAME")

def get_conn():
    conn = getattr(g, '_database', None) 
    # Se eu pego database com G e não encontro nada, jogo o None / getattr é invenção do Python que tenta extrair valores de uma coleção
    if conn is None:
        conn = g._database = sqlite3.connect(DATABASE_NAME)
    return conn

@app.teardown_appcontext
def close_connection(exception):
    print(" -------- Tou finalizando a requisição!!!")
    conn = getattr(g,'_database', None)
    if conn is not None:
        conn.close()


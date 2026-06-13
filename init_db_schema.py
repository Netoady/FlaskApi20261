import psycopg2
from helpers.logger import logger

DATABASE_NAME = "avicola"
DATABASE_USER = "postgres"
DATABASE_PASS = "123456"
DATABASE_PORT = "5435"
DATABASE_HOST = "localhost"

conn = None
try:
    # 1 - Abrir a conexão
    conn = psycopg2.connect(database=DATABASE_NAME,
                            user=DATABASE_USER,
                            password=DATABASE_PASS,
                            host=DATABASE_HOST, port=DATABASE_PORT)
    logger.info("Conectou ao banco de dados")
    # 2 - Recuperar o cursor
    cursor = conn.cursor()

    # 3 - Preparar a consultar: query | statement
    with open('schema.sql', mode='r') as file:
        cursor.execute(file.read())
    logger.info("Criou as tabelas")

    # 4.1 - Iterar nos resultados: resultset.
    # 4.2 - Confirmar operação.
    conn.commit()
except psycopg2.Error as e:
    logger.error(e)
finally:
    # 5 - Fechar a conexão
    if conn:
        conn.close()
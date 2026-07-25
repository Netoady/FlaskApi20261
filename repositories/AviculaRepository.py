from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Avicula.
'''


class AviculaRepository():
    def getAll(self, filtros=None):
        conn = get_conn()
        cursor = conn.cursor()
        query = "SELECT * FROM tb_aviculas"
        values = []
        
        if filtros:
            conditions = [f"{campo} = %s" for campo in filtros]
            values = list(filtros.values())
            query += " WHERE " + " " + " AND ".join(conditions)
        
        cursor.execute(query, values)
        return cursor.fetchall()

    def getByIdAvicula(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        # Ajustado de ? para %s
        cursor.execute("SELECT * FROM tb_aviculas WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, cnpj, endereco):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "INSERT INTO tb_aviculas(nome, cnpj, endereco) VALUES(%s, %s, %s)",
            (nome, cnpj, endereco)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome, cnpj, endereco):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "UPDATE tb_aviculas SET nome=%s, cnpj=%s, endereco=%s WHERE id=%s",
            (nome, cnpj, endereco, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute("DELETE FROM tb_aviculas WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
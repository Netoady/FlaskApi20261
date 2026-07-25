from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Aviario.
'''


class AviarioRepository():
    def getAll(self, filtros=None):
        conn = get_conn()
        cursor = conn.cursor()
        query = "SELECT * FROM tb_aviarios"
        values = []
        
        if filtros:
            conditions = [f"{campo} = %s" for campo in filtros]
            values = list(filtros.values())
            query += " WHERE " + " " + " AND ".join(conditions)
        
        cursor.execute(query, values)
        return cursor.fetchall()

    def getByIdAviario(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        # Ajustado de ? para %s
        cursor.execute("SELECT * FROM tb_aviarios WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "INSERT INTO tb_aviarios(nome, capacidade) VALUES(%s, %s)",
            (nome, capacidade)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "UPDATE tb_aviarios SET nome=%s, capacidade=%s WHERE id=%s",
            (nome, capacidade, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute("DELETE FROM tb_aviarios WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
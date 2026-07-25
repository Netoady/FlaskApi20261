from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Galpao.
'''


class GalpaoRepository():
    def getAll(self, filtros=None):
        conn = get_conn()
        cursor = conn.cursor()
        query = "SELECT * FROM tb_galpoes"
        values = []
        
        if filtros:
            conditions = [f"{campo} = %s" for campo in filtros]
            values = list(filtros.values())
            query += " WHERE " + " " + " AND ".join(conditions)
        
        cursor.execute(query, values)
        return cursor.fetchall()

    def getByIdGalpao(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        # Ajustado de ? para %s
        cursor.execute("SELECT * FROM tb_galpoes WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, identificador, area_m2):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "INSERT INTO tb_galpoes(identificador, area_m2) VALUES(%s, %s)",
            (identificador, area_m2)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, identificador, area_m2):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "UPDATE tb_galpoes SET identificador=%s, area_m2=%s WHERE id=%s",
            (identificador, area_m2, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute("DELETE FROM tb_galpoes WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
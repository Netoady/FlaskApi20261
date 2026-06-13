from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Galpao.
'''


class GalpaoRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_galpoes")
        return cursor.fetchall()

    def getByIdGalpao(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM tb_galpoes WHERE id=?", (id,))
        return cursor.fetchone()

    def insert(self, identificador, area_m2):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tb_galpoes(identificador, area_m2) VALUES(?, ?)",
            (identificador, area_m2)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, identificador, area_m2):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tb_galpoes SET identificador=?, area_m2=? WHERE id=?",
            (identificador, area_m2, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_galpoes WHERE id=?", (id,))
        conn.commit()
        return cursor.rowcount
from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Aviario.
'''


class AviarioRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_aviarios")
        return cursor.fetchall()

    def getByIdAviario(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM tb_aviarios WHERE id=?", (id,))
        return cursor.fetchone()

    def insert(self, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tb_aviarios(nome, capacidade) VALUES(?, ?)",
            (nome, capacidade)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tb_aviarios SET nome=?, capacidade=? WHERE id=?",
            (nome, capacidade, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_aviarios WHERE id=?", (id,))
        conn.commit()
        return cursor.rowcount
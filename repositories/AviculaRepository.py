from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Avicula.
'''


class AviculaRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_aviculas")
        return cursor.fetchall()

    def getByIdAvicula(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        cursor.execute("SELECT * FROM tb_aviculas WHERE id=?", (id,))
        return cursor.fetchone()

    def insert(self, nome, cnpj, endereco):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tb_aviculas(nome, cnpj, endereco) VALUES(?, ?, ?)",
            (nome, cnpj, endereco)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome, cnpj, endereco):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tb_aviculas SET nome=?, cnpj=?, endereco=? WHERE id=?",
            (nome, cnpj, endereco, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_aviculas WHERE id=?", (id,))
        conn.commit()
        return cursor.rowcount
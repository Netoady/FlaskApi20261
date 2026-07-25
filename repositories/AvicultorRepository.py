from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Avicultor.
'''


class AvicultorRepository():
    def getAll(self, filtros=None):
        conn = get_conn()
        cursor = conn.cursor()
        query = "SELECT * FROM tb_avicultores"
        values = []
        
        if filtros:
            conditions = [f"{campo} = %s" for campo in filtros]
            values = list(filtros.values())
            query += " WHERE " + " " + " AND ".join(conditions)
        
        cursor.execute(query, values)
        return cursor.fetchall()

    def getByIdAvicultor(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement.")
        # Ajustado de ? para %s
        cursor.execute("SELECT * FROM tb_avicultores WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, nascimento, cpf, caf):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "INSERT INTO tb_avicultores(nome, nascimento, cpf, caf) VALUES(%s, %s, %s, %s)",
            (nome, nascimento, cpf, caf)
        )
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome, nascimento, cpf, caf):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute(
            "UPDATE tb_avicultores SET nome=%s, nascimento=%s, cpf=%s, caf=%s WHERE id=%s",
            (nome, nascimento, cpf, caf, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        # Ajustado de ? para %s
        cursor.execute("DELETE FROM tb_avicultores WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
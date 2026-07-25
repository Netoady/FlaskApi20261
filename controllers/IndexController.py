from flask_restful import Resource
import psycopg2

from helpers.database import get_conn


class IndexController(Resource):
    def get(self):
        return {"versao": "1.0.1"}, 200


class HealthController(Resource):
    def get(self):
        try:
            conn = get_conn()
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
                return {"status": "healthy", "message": "Database connection verified."}
        except psycopg2.OperationalError as e:
            return {"status": "unhealthy", "message": f"Connection failed: {e}"}
        except Exception as e:
            return {"status": "unhealthy", "message": f"Unexpected error: {e}"}
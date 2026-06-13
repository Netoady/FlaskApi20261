from flask import jsonify
from helpers.application import app
from controllers.AvicultorController import avicultor_bp

app.register_blueprint(avicultor_bp)

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200

if __name__ == "__main__":
    # Mudamos explicitamente para a porta 5001 e ativamos o modo debug
    app.run(debug=True, port=5001)

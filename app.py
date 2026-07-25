from helpers.application import app, api
from controllers.AvicultorController import AvicultoresController, AvicultorController
from controllers.IndexController import IndexController, HealthController

api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')

api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

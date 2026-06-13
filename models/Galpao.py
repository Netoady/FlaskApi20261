class Galpao:
    def __init__(self, id, identificador, area_m2):
        self.id = id
        self.identificador = identificador
        self.area_m2 = area_m2

    def toDict(self):
        return {"id": self.id, "identificador": self.identificador, "area_m2": self.area_m2}

class GalpaoSchema(Schema):
    identificador = fields.Str(required=True, error_messages={
                    "required": "Adicione um identificador."
    })
    area_m2 = fields.Int(required=True, error_messages={"required": "Informe a area do galpao: "})



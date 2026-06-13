class Avicula:
    def __init__(self, id, nome, cnpj, endereco):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco

    def toDict(self):
        return {"nome": self.nome, "cnpj": self.cnpj, "endereco": self.endereco}

class AviculaSchema(Schema):
    nome = fields.Str(required=True, error_messages={
                    "required": "Adicione um nome."
    })
    cnpj = fields.Str(required=True, validate=validate.Length(max=14, error="Tamanho do CNPJ inválido."), error_messages=
                    {"required": "Adicione um CNPJ.", "invalid": })
    endereco = fields.Str(required=True, error_messages={
                    "required": "Adicione um endereco: "
    })


import mongoengine as me


def connect_mongo():
    me.connect(
        db="educore",
        host="mongodb://172.20.0.10:27017/educore"
    )

    print("Conectado ao MongoDB com sucesso!")
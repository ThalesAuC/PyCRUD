from .dbconnect import get_database
db = get_database()
colecao = db["pacientes"]

def criar_paciente(cpf:str, nome:str, idade:int, contato:str):
    paciente = {"cpf":cpf, "nome":nome, "idade":idade, "telefone":contato}
    return colecao.insert_one(paciente).inserted_id

def encontrar_paciente(cpf:str):
    return colecao.find_one({"cpf":cpf})
#TESTAR

def listar_pacientes():
    return list(colecao.find())

def atualizar_paciente(cpf:str, nome:str, idade:int, contato:str):
    return colecao.update_one({"cpf":cpf},
    {"$set":{"nome":nome,
    "idade":idade,
    "telefone":contato}
    })

def deletar_paciente(cpf:str):
    return colecao.delete_one({"cpf":cpf})
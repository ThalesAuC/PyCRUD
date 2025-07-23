import os
import json
import pyfiglet
from rich.console import Console
from rich.panel import Panel
f = pyfiglet.figlet_format("PyCrud", font="slant")
print(f)
console = Console()
console.print(Panel("1- Novo Cadastro"))
console.print(Panel("2- Buscar Cadastro"))
response = input(int());

match response:
    case 1: #cadastrar novo usuário
    userid # ler a ultima id e aplicar a logica de +1 encima do ultimo cadastrado
    nome = input("insira um nome para cadastro: ")
    idade = int(input("insira idade: "))
    email = input("insira o e-mail: ")


    user = { #objeto usuário
        "id":userid,
        "nome":nome,
        "email":email,
    }

print(json.dumps(user, indent=4, ensure_ascii=False))

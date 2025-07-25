import json
import os
#Create, parte onde o usuário insere os dados
userid # ler a ultima id e aplicar a logica de +1 encima do ultimo cadastrado
cpf = input("Insira o CPF: ")
nome = input("insira um nome: ")
idade = int(input("insira idade: "))
email = input("insira o e-mail: ")


user = { #objeto usuário
  "id":userid,
  "cpf":cpf,
  "nome":nome,
  "email":email,
    }
print(json.dumps(user, indent=4, ensure_ascii=False))


#print(nome,idade,email,sep="\n");

#print(user);
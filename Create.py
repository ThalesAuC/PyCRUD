import json
#Create, parte onde o usuário insere os dados
nome = input("insira um nome para cadastro: ");
idade = int(input("insira idade: "));
email = input("insira o e-mail: ");

user = {
  "nome":nome,
  "idade":idade,
  "email":email,
}

print(json.dumps(user, indent=4, ensure_ascii=False));

#print(nome,idade,email,sep="\n");

#print(user);
<pre>
      _____                      __  _______      __             ____   ___
     / ___/____ ___  ____ ______/ /_/ ____(_)____/ /_  ____ _   / __ \ <  /
     \__ \/ __ `__ \/ __ `/ ___/ __/ /_  / / ___/ __ \/ __ `/  / / / / / / 
    ___/ / / / / / / /_/ / /  / /_/ __/ / / /__/ / / / /_/ /  / /_/ / / /  
   /____/_/ /_/ /_/\__,_/_/   \__/_/   /_/\___/_/ /_/\__,_/   \____(_)_/  </pre>

# Sistema C.R.U.D. para teste de conceito:
 - criado em Python, implementado mongoDB para o banco de dados, implementação em docker para deploy rapido.

 1- Para rodar o programa use `git clone https://github.com/ThalesAuC/PyCRUD` </br>
 2- Com o docker instalado abra a pasta pycrud </br>
 3- Depois para iniciar o banco de dados use: `docker-compose up -d mongodb` </br>
 4- Depois rode: `docker-compose up -d --build smartficha`  </br>
 5- Para abrir o terminal do container rode: `docker exec -it smartficha_0.1 bash` ou `docker exec -it smartficha_0.1 sh` </br>
 6- Por fim use o comando para inciar o sistema `python main.py` </br>

![Imagem do Programa rodando em linha de comando pelo windows terminal](mainscreen.png) 

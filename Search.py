import os
import json
import pyfiglet
from rich.console import Console
from rich.panel import Panel
f = pyfiglet.figlet_format("Buscar Cadastro", font="slant")
print(f)
console = Console()
console.print(Panel("1- Visualizar Informações"))
console.print(Panel("2- Editar Informações"))
console.print(Panel("3- Apagar Cadastro"))
console.print(Panel("4- Retornar ao menu"))
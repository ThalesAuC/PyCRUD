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
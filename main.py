import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from FuncList import pausa, criar_cadastro, lista_cadastro, atualizar_cadastro, deletar_cadastro
console = Console()
header = pyfiglet.figlet_format("SmartFicha 0.1", font="slant")

def head():
    print(header)

def menu():
    console.print("Sistema para Cadastro de Pacientes, Selecione uma opção para prosseguir: ")
    console.print("[1] Novo Cadastro")
    console.print("[2] Listar Cadastros")
    console.print("[3] Alterar Cadastros") 
    console.print("[4] Remover Cadastro")
    console.print("[0] SAIR", style="red")

    escolha = int(input("Escolha uma Opção: "))
    return escolha

def clearterm():
    os.system('cls' if os.name == 'nt' else 'clear')
   
if __name__ =="__main__":
    while True:
        clearterm()
        head()
        escolha = menu()

        match escolha:
            case 0:
                console.print("Fechando Sistema...")
                clearterm()
                exit()
            
            case 1:
                criar_cadastro()
                clearterm()
            
            case 2:
                lista_cadastro()
            
            case 3:
                atualizar_cadastro()
                clearterm
            
            case 4:
                deletar_cadastro()
            
            case _:
                console.print("ERRO: NENHUMA OPÇÃO CORRESPONDENTE")
                pausa()
                clearterm()
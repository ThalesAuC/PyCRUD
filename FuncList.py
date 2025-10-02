import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from db.crud import criar_paciente, encontrar_paciente, listar_pacientes, atualizar_paciente, deletar_paciente

console = Console()
#funcs auxiliares -------------------------------------------
def clearterm():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("PRESSIONE ENTER PARA CONTINUAR...")

def tabela_list(titulo:str, info: list[dict]):
    panel = Table(title=titulo)
    panel.add_column("cpf")
    panel.add_column("nome")
    panel.add_column("idade")
    panel.add_column("telefone")
    for u in info:
        panel.add_row(u["cpf"], u["nome"], str(u["idade"]),u["telefone"])
    return console.print(panel)

def cadastro_unico(titulo:str, info: dict):
    panel = Table(title=titulo)
    panel.add_column("cpf")
    panel.add_column("nome")
    panel.add_column("idade")
    panel.add_column("telefone")
    panel.add_row(info["cpf"], info["nome"], str(info["idade"]),info["telefone"])
    return console.print(panel)

#-------------------------------------------------------------------

def criar_cadastro ():
    console.print("Insira as Informações solicitadas sobre o paciente: ")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    contato = input("telefone: ")
    criar_paciente(cpf, nome, idade, contato)
    console.print("✅ Cadastro de Paciente Salvo com Sucesso! ")
    pausa()

def lista_cadastro():
    pacientes = listar_pacientes()
    if not pacientes:
        console.print("❌ NENHUM PACIENTE CADASTRADO!", style="red")
        return 0
    else:
        tabela_list("Pacientes", pacientes)
    pausa()

def localizar_cadastro():
    cpf = input("Digite o CPF do Cadastro a ser localizado: ")
    paciente = encontrar_paciente(cpf)
    if not paciente:
        console.print("❌ NENHUM CADASTRO LOCALIZADO", style="red")
        pausa()
        return 0
    else:
        cadastro_unico("Cadastro Localizado", paciente)
    pausa()

def atualizar_cadastro():
    console.print("Insira as Informações para Atualizar ")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    contato = input("telefone: ")
    atualizar_paciente(cpf, nome, idade, contato)
    console.print("✅ Cadastro Atualizado com Sucesso!", style="green")
    pausa()
#todo: confirmação de que o cadastro naquele cpf foi localizado e recusa caso não encontrar nada


def deletar_cadastro():
    cpf = input("Digite o CPF do Cadastro a ser Apagado: ")
    paciente = encontrar_paciente(cpf)
    if not paciente:
        console.print("❌ NENHUM CADASTRO LOCALIZADO", style="red")
        pausa()
        return 0
    else:
        cadastro_unico("Cadastro Localizado", paciente)
        console.print("CONTINUAR A REMOÇÃO DO CADASTRO? ", style="red")
        status = int(input("[1]SIM ou [2]NÃO: "))
        match status:
            case 1:
                deletar_paciente(cpf)
                console.print("❌ CADASTRO REMOVIDO! ", style="red")
                pausa()
            case 2:
                console.print("OPERAÇÃO CANCELADA!")
                pausa()
    
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from db.crud import criar_paciente, listar_pacientes, atualizar_paciente, deletar_paciente 

console = Console()

def pausa():
    input("PRESSIONE ENTER PARA VOLTAR AO MENU...")


def criar_cadastro ():
    print("Insira as Informações solicitadas sobre o paciente: ")
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
        pausa()
        return 0
    else:
        panel = Table(title="PACIENTES")
        panel.add_column("cpf")
        panel.add_column("nome")
        panel.add_column("idade")
        panel.add_column("telefone")
    
    for u in pacientes:
        panel.add_row(u["cpf"], u["nome"], str(u["idade"]),u["telefone"])
        
    console.print(panel)
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

def deletar_cadastro():
        cpf = input("Digite o CPF do Cadastro a ser Apagado: ")
        deletar_paciente(cpf)
        console.print("🗑️ Cadastro Apagado com sucesso! ", style="red")
        pausa()

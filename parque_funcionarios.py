import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "parque_aquatico"
)
cursor = conexao_banco.cursor()

def cadastrar():

    id = int(input("digite o id do funcionarios: "))
    read = f'SELECT * FROM funcionarios WHERE id_funcionarios = {id}'
    cursor.execute(read)
    dados = cursor.fetchall()

    if len(dados) >  0:
        print("ja cadastrado")
    else:
        nome = input("digite o nome do funcionario: ").capitalize()
        cargo = input("digite o cargo do funcionario: ").capitalize()
        salario = float(input("digite o salario do funcionario: "))
        fone = int(input("digite o telefone do funcionario: "))
        cpf = int(input("digite o cpf do funcionario: "))
        cargaH = int(input("digite a carga horaria do funcionario: "))
    
        comando_sql = f'INSERT INTO funcionarios (id_funcionarios, nome_funcionarios, cargo_funcionarios, salario_funcionarios, telefone_funcionarios, cpf_funcionarios, cargaH_funcionarios) VALUES ({id},"{nome}", "{cargo}", {salario}, {fone}, {cpf}, {cargaH})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    

def alterar():
    id = int(input("digite o ID do funcionarios: "))
    novo_cargo = input("digite o novo cargo do funcionario: ")
    comando_sql = f'UPDATE funcionarios SET cargo = "{novo_cargo}" WHERE id_funcionarios = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def excluir():
    id = int(input("digite o ID do funcionario que deseja excluir: "))
    comando_sql = f'DELETE FROM funcionarios WHERE id_funcionarios = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def pesquisar():
    escolha = input('Escolha:\nN- nome \nT - Todos\n:').upper()
    if escolha == 'N':
        nome = input('Digite o nome: ')
        comando = f'SELECT * FROM funcionarios WHERE nome_funcionarios like "%{nome}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Nome não encontrado!')
        
    
    elif escolha == "T":
        comando = f'SELECT * FROM funcionarios '
        cursor.execute(comando)
        dados = cursor.fetchall()
    
def menu():
    while True:
        op = input("digite \nC-cadastrar \nA-alterar \nE-excluir \nP-pesquisar \nS-sair \n: ").upper()

        if op =="C":
            cadastrar()

        elif op =="A":
            alterar()

        elif op =="E":
            excluir()
        
        elif op =="P":
            pesquisar()

        elif op =="S":
            break

        else:
            print("insira uma alternativa valida: ")

menu()
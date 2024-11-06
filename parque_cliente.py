import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "parque_aquatico"
)
cursor = conexao_banco.cursor()

def cadastrar():

    id = int(input("digite o id do clientes: "))
    read = f'SELECT * FROM clientes WHERE id_clientes = {id}'
    cursor.execute(read)
    dados = cursor.fetchall()

    if len(dados) >  0:
        print("ja cadastrado")
    else:
        nome = input("digite o nome do cliente: ").capitalize()
        idade = int(input("digite a idade do cliente: "))
        rg = int(input("digite o RG do cliente: "))
        id_ingresso = id
    
        comando_sql = f'INSERT INTO clientes (id_clientes, nome_clientes, idade_clientes, rg_clientes,id_ingresso) VALUES ({id},"{nome}", {idade}, {rg}, {id_ingresso})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    

def alterar():
    id = int(input("digite o ID do clientes: "))
    novo_ingresso = input("digite a nova validade do ingresso do cliente: ")
    comando_sql = f'UPDATE clientes SET cargo = "{novo_ingresso}" WHERE id_clientes = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def excluir():
    id = int(input("digite o ID do cliente que deseja excluir: "))
    comando_sql = f'DELETE FROM clientes WHERE id_clientes = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def pesquisar():
    escolha = input('Escolha:\nN- nome \nT - Todos\n:').upper()
    if escolha == 'N':
        nome = input('Digite o nome: ')
        comando = f'SELECT * FROM clientes WHERE nome_clientes like "%{nome}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Nome não encontrado!')
        
    
    elif escolha == "T":
        comando = f'SELECT * FROM clientes '
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
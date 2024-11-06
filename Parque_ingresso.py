import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "parque_aquatico"
)
cursor = conexao_banco.cursor()

def cadastrar():

    id = int(input("digite o id do ingresso: "))
    read = f'SELECT * FROM ingresso WHERE id_ingresso = {id}'
    cursor.execute(read)
    dados = cursor.fetchall()

    if len(dados) >  0:
        print("ja cadastrado")
    else:
        tipo = input("digite o tipo do ingresso(Padrão, VIP ou Meia): ").capitalize()
        preco = float(input("digite o preço do ingresso: "))
        validade = input("digite a validade do ingresso: ")
    
        comando_sql = f'INSERT INTO ingresso (id_ingresso, tipo_ingresso, preco_ingresso, validade_ingresso) VALUES ({id},"{tipo}", {preco}, "{validade}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    

def alterar():
    id = int(input("digite o ID do ingresso: "))
    nova_validade = input("digite a nova validade do ingresso: ")
    comando_sql = f'UPDATE ingresso SET validade = "{nova_validade}" WHERE id_ingresso = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def excluir():
    id = int(input("digite o ID do ingresso que deseja excluir: "))
    comando_sql = f'DELETE FROM ingresso WHERE id_ingresso = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def pesquisar():
    escolha = input('Escolha:\nT - Tipo\nTo - Todos\n:').upper()
    if escolha == 'T':
        tipo = input('Digite o tipo(padrão, VIP ou Meia): ')
        comando = f'SELECT * FROM ingresso WHERE tipo_ingresso like "%{tipo}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Nome não encontrado!')
        else:
            for i in dados:
                print(f'ID:{i[0]}   TIPO: {i[1]} PREÇO: {i[2]} VALIDADE: {i[3]}' )
    
    elif escolha == "To":
        comando = f'SELECT * FROM ingresso '
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
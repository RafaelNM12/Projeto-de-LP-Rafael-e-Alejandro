import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "parque_aquatico"
)
cursor = conexao_banco.cursor()

def cadastrar():

    id = int(input("digite o id do brinquedos: "))
    read = f'SELECT * FROM brinquedos WHERE id_brinquedos = {id}'
    cursor.execute(read)
    dados = cursor.fetchall()

    if len(dados) >  0:
        print("ja cadastrado")
    else:
        nome = input("digite o nome do brinquedo: ").capitalize()
        manu = input("digite se a manutenção esta em andamento ou se está finalizado: ").capitalize()
        status = input("digite o brinquedo esta apto ou não: ").capitalize()
    
        comando_sql = f'INSERT INTO brinquedos (id_brinquedos, nome_brinquedos, manutenção_brinquedos, status_brinquedos) VALUES ({id},"{nome}", "{manu}", "{status}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    

def alterar():
    id = int(input("digite o ID do brinquedo: "))
    nova_manu = input("digite se a manutenção esta em andamento ou se está finalizado: ").capitalize()
    novo_status = input("digite os novos status do brinquedo: ")
    comando_sql = f'UPDATE brinquedos SET manutenção_brinquedos = "{nova_manu}", status = "{novo_status}" WHERE id_brinquedos = {id}'
    
    cursor.execute(comando_sql)
    conexao_banco.commit()


def excluir():
    id = int(input("digite o ID do brinquedo que deseja excluir: "))
    comando_sql = f'DELETE FROM brinquedos WHERE id_brinquedos = {id}'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def pesquisar():
    escolha = input('Escolha:\nN- nome \nT - Todos\n:').upper()
    if escolha == 'N':
        nome = input('Digite o nome do brinquedo: ')
        comando = f'SELECT * FROM brinquedos WHERE nome_brinquedos like "%{nome}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()
        print(dados)

        if len(dados) <= 0:
            print('brinquedo não encontrado!')
        
    
    elif escolha == "T":
        comando = f'SELECT * FROM brinquedos '
        cursor.execute(comando)
        dados = cursor.fetchall()
        print(dados)
    
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
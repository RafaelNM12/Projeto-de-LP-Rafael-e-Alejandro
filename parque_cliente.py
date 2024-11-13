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
    read = f'SELECT * FROM clientes WHERE id_clientes = {id};'
    cursor.execute(read)
    dados = cursor.fetchall()

    if len(dados) >  0:
        print("ja cadastrado")
    else:
        nome = input("digite o nome do cliente: ").capitalize()
        idade = int(input("digite a idade do cliente: "))
        rg = int(input("digite o RG do cliente: "))
        ingresso = input("digite o tipo do ingresso \nP-Padrão(R$50,00), \nV-VIP(R$75,00) \n: ").upper()
        ing_qunt = int(input("quantos ingressos você quer comprar: "))
        if ingresso =="P":
            valor = 50*ing_qunt
        elif ingresso =="V":
            valor = 75*ing_qunt
    
        comando_sql = f'INSERT INTO clientes (id_clientes, nome_clientes, idade_clientes, rg_clientes, ingreso_tipo, ingresso_quant, ingresso_valor) VALUES ({id},"{nome}", {idade}, {rg}, "{ingresso}", {ing_qunt}, {valor});'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    

def alterar():
    id = int(input("digite o ID do clientes: "))
    novo_tipo = input("digite o novo ingresso do cliente\nV-VIP \nP-padrão \n:  ").upper()
    nova_quant = int(input("digite a nova quantidade de ingresso que deseja pegar: "))
    if novo_tipo =="P":
        valor = 50*nova_quant

    elif novo_tipo =="V":
        valor = 75*nova_quant

    comando_sql = f'UPDATE clientes SET ingreso_tipo = "{novo_tipo}", ingresso_quant = {nova_quant}, ingresso_valor = {valor} WHERE id_clientes = {id};'
    cursor.execute(comando_sql)
    conexao_banco.commit()

def excluir():
    id = int(input("digite o ID do cliente que deseja excluir: "))
    comando_sql = f'DELETE FROM clientes WHERE id_clientes = {id};'

    cursor.execute(comando_sql)
    conexao_banco.commit()


def pesquisar():
    escolha = input('Escolha:\nV- VIP \nP - Padrão\nT- Todos\n : ').upper()
    if escolha == 'V':
        comando = f'SELECT * FROM clientes WHERE ingreso_tipo like "%{escolha}%";'
        cursor.execute(comando)
        dados = cursor.fetchall()
        print(dados)
        
        if len(dados) <= 0:
            print('Não encontrado!')

    elif escolha == "P":
        comando = f'SELECT * FROM clientes WHERE ingreso_tipo like "%{escolha}%";'
        cursor.execute(comando)
        dados = cursor.fetchall()
        print(dados)

        if len(dados) <= 0:
            print('Não encontrado!')  
    
    elif escolha == "T":
        comando = f'SELECT * FROM clientes;'
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
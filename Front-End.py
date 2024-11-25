from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "parque_aquatico"
)
cursor = conexao_banco.cursor()


root = Tk() #Criar o TK (Cria a janela)
root.title("Águas Rasas") 
root.config(bg="#021C2F")

#---------------------------------------------DEFS---------------------------------------------------#

def cadastro():
    frm.pack_forget()
    framecadastrar.pack(expand=True)

def volta_cadastro():
    framecadastrar.pack_forget()
    frm.pack(expand=True)

def funcionario():
    framecadastrar.pack_forget()
    framefunc.pack(expand=True)

def volta_cadastro_funcionario():
    framefunc.pack_forget()
    framecadastrar.pack(expand=True)

def visitantes():
    framecadastrar.pack_forget()
    framevisitante.pack(expand=True)

def volta_cadastro_Clientes():
    framevisitante.pack_forget()
    framecadastrar.pack(expand=True)

def brinquedos():
    framecadastrar.pack_forget()
    framebrinq.pack(expand=True)

def volta_cadastro_Brinquedos():
    framebrinq.pack_forget()
    framecadastrar.pack(expand=True)


#--------------------------------pesquisar--------------------------------#
def Pesquisar():
    frm.pack_forget()
    framepesquisar.pack(expand=True)

def volta_pesquisa():
    framepesquisar.pack_forget()
    frm.pack(expand=True)

def funcionarioP():
    framepesquisar.pack_forget()
    framePfunc.pack(expand=True)

def volta_pesquisa_funcionario():
    framePfunc.pack_forget()
    framepesquisar.pack(expand=True)

def visitanteP():
    framepesquisar.pack_forget()
    framePvisitante.pack(expand=True)

def volta_pesquisa_cliente():
    framePvisitante.pack_forget()
    framepesquisar.pack(expand=True)

def brinquedosP():
    framepesquisar.pack_forget()
    framePbrinq.pack(expand=True)

def volta_pesquisa_brinquedos():
    framePbrinq.pack_forget()
    framepesquisar.pack(expand=True)

#----------------------------Alterar---------------------------------------

def alterar():
    frm.pack_forget()
    framealterar.pack(expand=True)

def volta_alterar():
    framealterar.pack_forget()
    frm.pack(expand=True)

def funcionarioA():
    framealterar.pack_forget()
    frameAfunc.pack(expand=True)

def volta_alterar_funcionario():
    frameAfunc.pack_forget()
    framealterar.pack(expand=True)

def visitanteA():
    framealterar.pack_forget()
    frameAvisitante.pack(expand=True)

def volta_alterar_cliente():
    frameAvisitante.pack_forget()
    framealterar.pack(expand=True)

def brinquedosA():
    framealterar.pack_forget()
    frameAbrinq.pack(expand=True)

def volta_alterar_brinquedos():
    frameAbrinq.pack_forget()
    framealterar.pack(expand=True)

#----------------EXCLUIR---------------

def Excluir():
    frm.pack_forget()
    frameexcluir.pack(expand=True)

def volta_excluir():
    frameexcluir.pack_forget()
    frm.pack(expand=True)

def funcionarioE():
    frameexcluir.pack_forget()
    frameEfunc.pack(expand=True)

def volta_excluir_funcionario():
    frameEfunc.pack_forget()
    frameexcluir.pack(expand=True)

def visitanteE():
    frameexcluir.pack_forget()
    frameEvisitante.pack(expand=True)

def volta_excluir_cliente():
    frameEvisitante.pack_forget()
    frameexcluir.pack(expand=True)

def brinquedosE():
    frameexcluir.pack_forget()
    frameEbrinq.pack(expand=True)

def volta_excluir_brinquedos():
    frameEbrinq.pack_forget()
    frameexcluir.pack(expand=True)

#-------------------------------------------------------------------------------------------------#

imagem = Image.open("./Assets/Logo.jpg")
imagem = ImageTk.PhotoImage(file="./Assets/Logo.jpg")
img = Label(root, image=imagem, bg="#021C2F")
img.Imagem = imagem
img.pack()

#-------------------------------------------------------------------------------------------------#

""" root.attributes('-fullscreen', True) """

#-------------------------------------------------------------------------------------------------#
frm = Frame(root, pady=100)
frm.config(bg="#021C2F")

menu = Label(frm, text="------------ MENU ------------", bg="#021C2F", fg="#FFFFFF", font=("Arial", 12)).grid(column=0, row=0)
esc1 = Button(frm, text="Cadastrar", command=cadastro, width= 10).grid(column=0, row=1)
esc2 = Button(frm, text="Pesquisar", command=Pesquisar, width= 10).grid(column=0, row=2)
esc3 = Button(frm, text="Alterar", command=alterar, width= 10).grid(column=0, row=3)
esc4 = Button(frm, text="Excluir", command=Excluir, width= 10).grid(column=0, row=4)
frm.pack()
     
#---------------------------------------- CRIAR PAGINAS -------------------------------------------------#
#----------------CADASTRAR-------------------------
framecadastrar = Frame(root, bg="#021C2F")

framefunc = Frame(root, bg="#021C2F")

framevisitante = Frame(root, bg="#021C2F")

framebrinq = Frame(root, bg="#021C2F")
#----------------------PESQUISAR---------------------
framepesquisar = Frame(root, bg="#021C2F")

framePfunc = Frame(root, bg="#021C2F")

framePvisitante = Frame(root, bg="#021C2F")

framePbrinq = Frame(root, bg="#021C2F")
#-----------------ALTERAR-------------
framealterar =Frame(root, bg="#021C2F")

frameAfunc = Frame(root, bg="#021C2F")

frameAvisitante = Frame(root, bg="#021C2F")

frameAbrinq = Frame(root, bg="#021C2F")
#-------------EXCLUIR---------------
frameexcluir =Frame(root, bg="#021C2F")

frameEfunc = Frame(root, bg="#021C2F")

frameEvisitante = Frame(root, bg="#021C2F")

frameEbrinq = Frame(root, bg="#021C2F")

#------------------------------------------ CADASTRAR ------------------------------------------------------#

Label(framecadastrar, text="Opções de cadastro",  bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0)
func = Button(framecadastrar, text="Funcionário", command=funcionario, width=10).grid(column=0, row=4, padx=(0, 120), pady=30)
cliente = Button(framecadastrar, text="Visitante", command=visitantes, width=10).grid(column=0, row=4, padx=(120, 0), pady=10)
brinq = Button(framecadastrar, text="Brinquedos", command=brinquedos, width=10).grid(column=0, row=5)

Button(framecadastrar, text="Volte para a tela inicial", command=volta_cadastro).grid(column=0, row=7)


#------------------------------------------ fUNCIONÁRIO ------------------------------------------------------#

Label(framefunc, text="ID: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
Id = Entry(framefunc, width=45, font=(("Arial", 12)))
Id.grid(column=0, row=0, padx=(100, 0))

Label(framefunc, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=2, padx=(0, 400))
nome = Entry(framefunc, width=45, font=(("Arial", 12)))
nome.grid(column=0, row=2, padx=(100, 0))

Label(framefunc, text="Cargo: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=6, padx=(0, 400))
cargo = Entry(framefunc, width=45, font=(("Arial", 12)))
cargo.grid(column=0, row=6, padx=(100, 0))

Label(framefunc, text="Salario: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=8, padx=(0, 400))
salario = Entry(framefunc, width=45, font=(("Arial", 12)))
salario.grid(column=0, row=8, padx=(100, 0))

Label(framefunc, text="Telefone: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=10, padx=(0, 400))
telefone = Entry(framefunc, width=45, font=(("Arial", 12)))
telefone.grid(column=0, row=10, padx=(100, 0))

Label(framefunc, text="CPF: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=4, padx=(0, 400))
cpf = Entry(framefunc, width=45, font=(("Arial", 12)))
cpf.grid(column=0, row=4, padx =(100, 0))

Label(framefunc, text="Carga-Horária: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=12, padx=(0, 450))
CargaH = Entry(framefunc, width=45, font=(("Arial", 12)))
CargaH.grid(column=0, row=12, padx=(100, 0))

Button(framefunc, text="Volte para a tela de cadastro", command=volta_cadastro_funcionario).grid(column=0, row=16)
#--------------------Armazenamento dos Funcionarios-----------------------------------------------------------#
def armazenar():

    id_funcionarios = Id.get()
    
    nome_funcionarios = nome.get()
    
    cargo_funcionarios = cargo.get()

    salario_funcionarios = salario.get()

    telefone_funcionarios = telefone.get()

    cpf_funcionarios = cpf.get()
    
    cargaH_funcionarios = CargaH.get()

    cursor.execute(f"INSERT INTO funcionarios (id_funcionarios, nome_funcionarios, cargo_funcionarios, salario_funcionarios, telefone_funcionarios, cpf_funcionarios, cargaH_funcionarios) VALUES ({id_funcionarios},'{nome_funcionarios}','{cargo_funcionarios}',{salario_funcionarios},{telefone_funcionarios},{cpf_funcionarios},{cargaH_funcionarios})")

    conexao_banco.commit()

    messagebox.showinfo("resultado","------TUDO CADASTRADO COM SUCESSO-------" )

RegistrarButton = Button(framefunc, text="Registrar Funcionario", width=35, command=armazenar).grid(column=0, row=14)


#--------------------------------------Clientes-----------------------------------------------------------------#

Label(framevisitante, text="ID: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
Ida = Entry(framevisitante, width=45, font=(("Arial", 12)))
Ida.grid(column=0, row=0, padx=(100, 0))

Label(framevisitante, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=2, padx=(0, 400))
nomeC = Entry(framevisitante, width=45, font=(("Arial", 12)))
nomeC.grid(column=0, row=2, padx=(100, 0))

Label(framevisitante, text="Idade: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=4, padx=(0, 400))
idade = Entry(framevisitante, width=45, font=(("Arial", 12)))
idade.grid(column=0, row=4, padx=(100, 0))

Label(framevisitante, text="RG: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=6, padx=(0, 400))
rg = Entry(framevisitante, width=45, font=(("Arial", 12)))
rg.grid(column=0, row=6, padx=(100, 0))

Label(framevisitante, text="Tipo do ingresso: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=8, padx=(0, 450))
ingressoT = Entry(framevisitante, width=45, font=(("Arial", 12)))
ingressoT.grid(column=0, row=8, padx=(100, 0))

Label(framevisitante, text="Quantidade de ingresso: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=10, padx=(0, 450))
ingressoQ = Entry(framevisitante, width=45, font=(("Arial", 12)))
ingressoQ.grid(column=0, row=10, padx=(100, 0))

Button(framevisitante, text="Volte para a tela de cadastro", command=volta_cadastro_Clientes).grid(column=0, row=14)
#-----------------------------Armazenamento dos clientes ---------------------------------------------------------#

def armazenarC():

    valor = 0 

    Id_cliente = Ida.get()

    nome_cliente = nomeC.get()

    idade_cliente = idade.get()

    rg_cliente = rg.get()

    ingreso_tipo = ingressoT.get()

    ingresso_quant = int(ingressoQ.get())

    if ingreso_tipo == "P" or ingreso_tipo == "p" :
        valor = 50 * ingresso_quant

    elif ingreso_tipo == "V" or ingreso_tipo == "v" :
        valor = 75 * ingresso_quant

    cursor.execute(f"INSERT INTO clientes (id_clientes, nome_clientes, idade_clientes, rg_clientes, ingreso_tipo, ingresso_quant, ingresso_valor) VALUES ({Id_cliente}, '{nome_cliente}', {idade_cliente}, {rg_cliente}, '{ingreso_tipo}', {ingresso_quant}, {valor})")

    conexao_banco.commit()

    messagebox.showinfo("resultado","------TUDO CADASTRADO COM SUCESSO-------" )


RegistrarButton = Button(framevisitante, text="Registrar Cliente", width=35, command=armazenarC).grid(column=0, row=12)

#-----------------------------------------------------Brinquedos--------------------------------------------------------#

Label(framebrinq, text="ID: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
IdB = Entry(framebrinq, width=45, font=(("Arial", 12)))
IdB.grid(column=0, row=0, padx=(100, 0))

Label(framebrinq, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=2, padx=(0, 400))
nomeB = Entry(framebrinq, width=45, font=(("Arial", 12)))
nomeB.grid(column=0, row=2, padx=(100, 0))

Label(framebrinq, text="Manutenção: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=4, padx=(0, 400))
manutencao = Entry(framebrinq, width=45, font=(("Arial", 12)))
manutencao.grid(column=0, row=4, padx=(100, 0))

Label(framebrinq, text="status: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=6, padx=(0, 400))
status = Entry(framebrinq, width=45, font=(("Arial", 12)))
status.grid(column=0, row=6, padx=(100, 0))

Button(framebrinq, text="Volte para a tela de cadastro", command=volta_cadastro_Brinquedos).grid(column=0, row=10)
#-------------------------------------Armazenamento dos Brinquedos----------------------------------------------------#

def armazenarB():

    id_brinq = IdB.get()
    
    nome_brinq = nomeB.get()
    
    manuc = manutencao.get()

    stat = status.get()

    cursor.execute(f"INSERT INTO brinquedos (id_brinquedos, nome_brinquedos, manutenção_brinquedos, status_brinquedos) VALUES ({id_brinq}, '{nome_brinq}', '{manuc}', '{stat}')")

    conexao_banco.commit()

    messagebox.showinfo("resultado","------TUDO CADASTRADO COM SUCESSO-------" )

RegistrarButton = Button(framebrinq, text="Registrar Brinquedo", width=35, command=armazenarB).grid(column=0, row=8)

#-------------------------------------Pesquisar---------------------------------------------------------------#

Label(framepesquisar, text="Opções de pesquisa",  bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0)
funcP = Button(framepesquisar, text="Funcionário", command=funcionarioP, width=10).grid(column=0, row=4, padx=(0, 120), pady=30)
clienteP = Button(framepesquisar, text="Visitante", command=visitanteP, width=10).grid(column=0, row=4, padx=(120, 0), pady=10)
brinqP = Button(framepesquisar, text="Brinquedos", command=brinquedosP, width=10).grid(column=0, row=5)

Button(framepesquisar, text="Volte para a tela inicial", command=volta_pesquisa).grid(column=0, row=7)

#---------------------------Funcionario----------------------------------------------------------------#

Label(framePfunc, text="ID: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
IdF = Entry(framePfunc, width=45, font=(("Arial", 12)))
IdF.grid(column=0, row=0, padx=(100, 0))


Button(framePfunc, text="Volte para a tela de pesquisa", command=volta_pesquisa_funcionario).grid(column=0, row=4)

#----------------------Função de pesquisa do funcionario------------------------------------------------#

def pesquisaF_id():
    idP_funcionario = IdF.get()

    cursor.execute(f"SELECT * FROM funcionarios WHERE id_funcionarios = {idP_funcionario}")
    dados = cursor.fetchall()
    
    if len(dados) <= 0:
            messagebox.showinfo('Nome não encontrado!', "isso não esta no banco")
    else:
        for i in dados:
            messagebox.showinfo("Resultado", f'ID: {i[0]}, Nome: {i[1]}, Cargo: {i[2]}, Salario: {i[3]}, Telefone: {i[4]}, CPF: {i[5]}, Carga Horaria: {i[6]}')


pesquisaButton = Button(framePfunc, text="Pesquisar Funcionario", width=35, command=pesquisaF_id).grid(column=0, row=2)

#--------------------cliente------------------------------------------------#

Label(framePvisitante, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
nomeCP = Entry(framePvisitante, width=45, font=(("Arial", 12)))
nomeCP.grid(column=0, row=0, padx=(100, 0))

Button(framePvisitante, text="Volte para a tela de pesquisa", command=volta_pesquisa_cliente).grid(column=0, row=4)

#----------------------Função de pesquisa do cliente-------------------------#

def pesquisaC_nome():
    nome_clienteP = nomeCP.get()

    cursor.execute(f"SELECT * FROM clientes WHERE nome_clientes like '%{nome_clienteP}%' ")
    dados = cursor.fetchall()

    if len(dados) <= 0:
            messagebox.showinfo('Nome não encontrado!', "isso não esta no banco")
    else:
        for i in dados:
            messagebox.showinfo("Resultado", f'ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]}, RG: {i[3]}, TIPO do INGRESSO: {i[4]}, Quantidade de Ingressos: {i[5]}, Valor Total: {i[6]}')

pesquisaButton = Button(framePvisitante, text="Pesquisar cliente", width=35, command=pesquisaC_nome).grid(column=0, row=2)

#------------------------------Brinquedos--------------------------------#

Label(framePbrinq, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
nomeBP = Entry(framePbrinq, width=45, font=(("Arial", 12)))
nomeBP.grid(column=0, row=0, padx=(100, 0))

Button(framePbrinq, text="Volte para a tela de pesquisa", command=volta_pesquisa_brinquedos).grid(column=0, row=4)

#-----------------------------Função de pesquisa do Brinquedos--------------------------------------------

def pesquisaB_nome():
    nome_brinqP = nomeBP.get()

    cursor.execute(f"SELECT * FROM brinquedos WHERE nome_brinquedos like '%{nome_brinqP}%' ")
    dados = cursor.fetchall()

    if len(dados) <= 0:
            messagebox.showinfo('Nome não encontrado!', "isso não esta no banco")
    else:
        for i in dados:
            messagebox.showinfo("Resultado", f'ID: {i[0]}, Nome: {i[1]}, Manuteção: {i[2]}, Status: {i[3]} ')

pesquisaButton = Button(framePbrinq, text="Pesquisar brinquedo", width=35, command=pesquisaB_nome).grid(column=0, row=2)


#-----------------------ALTERAR----------------------------------------------------

Label(framealterar, text="tabelas que podem ser alteradas",  bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0)
funcA = Button(framealterar, text="Funcionário", command=funcionarioA, width=10).grid(column=0, row=4, padx=(0, 120), pady=30)
clienteA = Button(framealterar, text="Visitante", command=visitanteA, width=10).grid(column=0, row=4, padx=(120, 0), pady=10)
brinqA = Button(framealterar, text="Brinquedos", command=brinquedosA, width=10).grid(column=0, row=5)


Button(framealterar, text="Volte para a tela inicial", command=volta_alterar).grid(column=0, row=7)

#----------------------alterar funcionario-------------------------------

Label(frameAfunc, text="Digite o ID do funcionario que deseja alterar: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdAF = Entry(frameAfunc, width=45, font=(("Arial", 12)))
IdAF.grid(column=0, row=0, padx=(100, 0))

Label(frameAfunc, text="Cargo: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=6, padx=(0, 400))
cargoAF = Entry(frameAfunc, width=45, font=(("Arial", 12)))
cargoAF.grid(column=0, row=6, padx=(100, 0))

Label(frameAfunc, text="Salario: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=8, padx=(0, 400))
salarioAF = Entry(frameAfunc, width=45, font=(("Arial", 12)))
salarioAF.grid(column=0, row=8, padx=(100, 0))

Label(frameAfunc, text="Carga-Horária: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=14, padx=(0, 450))
CargaHAF = Entry(frameAfunc, width=45, font=(("Arial", 12)))
CargaHAF.grid(column=0, row=14, padx=(100, 0))

Button(frameAfunc, text="Volte para a tela de alterar", command=volta_alterar_funcionario).grid(column=0, row=18)

#------------------------------função de alterar o funcionario----------------------------------------------

def alterarF():

    Id_funcionariosA = IdAF.get()

    cargo_funcionariosA = cargoAF.get()

    salario_funcionariosA = salarioAF.get()

    cargaH_funcionariosA = CargaHAF.get()

    cursor.execute(f"UPDATE funcionarios SET cargo_funcionarios = '{cargo_funcionariosA}', salario_funcionarios = {salario_funcionariosA},cargaH_funcionarios = {cargaH_funcionariosA} WHERE id_funcionarios = {Id_funcionariosA} ")

    conexao_banco.commit()

    messagebox.showinfo("resultado", "ALTERAÇÃO COMPLETADA" )

RegistrarButton = Button(frameAfunc, text="alterar dados do funcionario", width=35, command=alterarF).grid(column=0, row=16)

#----------------------------clientes-----------------------------------------------------------

Label(frameAvisitante, text="Digite o ID do clientes que deseja alterar: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdCA = Entry(frameAvisitante, width=45, font=(("Arial", 12)))
IdCA.grid(column=0, row=0, padx=(100, 0))

Label(frameAvisitante, text="Tipo do ingresso: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=8, padx=(0, 500))
ingressoTA = Entry(frameAvisitante, width=45, font=(("Arial", 12)))
ingressoTA.grid(column=0, row=2, padx=(100, 0))

Label(frameAvisitante, text="Quantidade de ingresso: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=10, padx=(0, 500))
ingressoQA = Entry(frameAvisitante, width=45, font=(("Arial", 12)))
ingressoQA.grid(column=0, row=4, padx=(100, 0))

Button(frameAvisitante, text="Volte para a tela de alterar", command=volta_alterar_cliente).grid(column=0, row=18)

#------------------------------função de alterar o cliente----------------------------------------------

def alterarC():

    valorA = 0 

    id_clientesA = IdCA.get()

    ingreso_tipoA = ingressoTA.get()

    ingresso_quantA = int(ingressoQA.get())

    if ingreso_tipoA == "P" or ingreso_tipoA == "p" :
        valorA = 50 * ingresso_quantA

    elif ingreso_tipoA == "V" or ingreso_tipoA == "v" :
        valorA = 75 * ingresso_quantA

    cursor.execute(f'UPDATE clientes SET ingreso_tipo = "{ingreso_tipoA}", ingresso_quant = {ingresso_quantA}, ingresso_valor = {valorA} WHERE id_clientes = {id_clientesA}') 

    messagebox.showinfo("resultado", "ALTERAÇÃO COMPLETADA" )

    conexao_banco.commit()

RegistrarButton = Button(frameAvisitante, text="alterar dados do Cliente", width=35, command=alterarC).grid(column=0, row=8)

#------------------------------------Brinquedos------------------------------------------------------

Label(frameAbrinq, text="Digite o ID do Brinquedo que deseja alterar: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdBA = Entry(frameAbrinq, width=45, font=(("Arial", 12)))
IdBA.grid(column=0, row=0, padx=(100, 0))

Label(frameAbrinq, text="Manutenção: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=4, padx=(0, 450))
manutencaoA = Entry(frameAbrinq, width=45, font=(("Arial", 12)))
manutencaoA.grid(column=0, row=4, padx=(100, 0))

Label(frameAbrinq, text="status: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=6, padx=(0, 400))
statusA = Entry(frameAbrinq, width=45, font=(("Arial", 12)))
statusA.grid(column=0, row=6, padx=(100, 0))

Button(frameAbrinq, text="Volte para a tela de alterar", command=volta_alterar_brinquedos).grid(column=0, row=10)

#--------------------------------------função de alterar o Brinquedos----------------------------------------------

def alterarB():

    id_brinq = IdBA.get()

    manuAB = manutencaoA.get()                                                   

    statusAB = statusA.get()

    cursor.execute(f'UPDATE brinquedos SET manutenção_brinquedos = "{manuAB}", status_brinquedos = "{statusAB}" WHERE id_brinquedos = {id_brinq} ')
    
    messagebox.showinfo("resultado", "ALTERAÇÃO COMPLETADA" )

    conexao_banco.commit()

Button(frameAbrinq, text='alterar dados do brinquedo', width=35 , command=alterarB).grid(column=0, row=8)

#---------------------------------Excluir-------------------------------------------------

Label(frameexcluir, text="tabelas que podem ser excluidas",  bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0)
funcE = Button(frameexcluir, text="Funcionário", command=funcionarioE, width=10).grid(column=0, row=4, padx=(0, 120), pady=30)
clienteE = Button(frameexcluir, text="Visitante", command=visitanteE, width=10).grid(column=0, row=4, padx=(120, 0), pady=10)
brinqE = Button(frameexcluir, text="Brinquedos", command=brinquedosE, width=10).grid(column=0, row=5)


Button(frameexcluir, text="Volte para a tela inicial", command=volta_excluir).grid(column=0, row=7)
#------------------------------excluir funcionario----------------------------------

Label(frameEfunc, text="Digite o ID do funcinario que deseja excluir: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdFE = Entry(frameEfunc, width=45, font=(("Arial", 12)))
IdFE.grid(column=0, row=2, padx=(100, 0))

Button(frameEfunc, text="Volte para a tela de excluir", command=volta_excluir_funcionario).grid(column=0, row=6)

#-----------------------------função de excluir--------------------------------

def excluirF():
    id_funcionarioE = IdFE.get()

    cursor.execute(f"DELETE FROM funcionarios WHERE id_funcionarios = {id_funcionarioE}")

    conexao_banco.commit()

    messagebox.showinfo("resultado", "FUNCIONARIO EXCLUIDO" )

Button(frameEfunc, text="excluir funcionario", width=35 , command=excluirF).grid(column=0, row=4)

#----------------------------excluir clientes---------------------------------

Label(frameEvisitante, text="Digite o ID do cliente que deseja excluir: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdCE = Entry(frameEvisitante, width=45, font=(("Arial", 12)))
IdCE.grid(column=0, row=2, padx=(100, 0))

Button(frameEvisitante, text="Volte para a tela de excluir", command=volta_excluir_cliente).grid(column=0, row=6)

#------------------função excluir--------------------------------------------------

def excluirC():
    id_clientesE = IdCE.get()

    cursor.execute(f"DELETE FROM clientes WHERE id_clientes = {id_clientesE}")

    conexao_banco.commit()

    messagebox.showinfo("resultado", "CLIENTE EXCLUIDO" )

Button(frameEvisitante, text="excluir clientes", width=35, command=excluirC).grid(column=0, row=4)

#-------------------excluir brinquedos---------------------------------------------

Label(frameEbrinq, text="Digite o ID do brinquedo que deseja excluir: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 700))
IdBE = Entry(frameEbrinq, width=45, font=(("Arial", 12)))
IdBE.grid(column=0, row=2, padx=(100, 0))

Button(frameEbrinq, text="Volte para a tela de excluir", command=volta_excluir_brinquedos).grid(column=0, row=6)

#---------------------função excluir-----------------------------------------------

def excluirB():
    id_brinquedosE = IdBE.get()

    cursor.execute(f"DELETE FROM brinquedos WHERE id_brinquedos = {id_brinquedosE} ")

    conexao_banco.commit()

    messagebox.showinfo("resultado", "BRINQUEDO EXCLUIDO" )

Button(frameEbrinq, text="excluir brinquedos", width=35, command=excluirB).grid(column=0, row=4)



root.mainloop()
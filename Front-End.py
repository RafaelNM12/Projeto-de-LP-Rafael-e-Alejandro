from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "1234",
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

def visitantes():
    framecadastrar.pack_forget()
    framevisitante.pack(expand=True)



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
esc2 = Button(frm, text="Pesquisar", command=root.option_add, width= 10).grid(column=0, row=2)
esc3 = Button(frm, text="Alterar", command=root.option_add, width= 10).grid(column=0, row=3)
esc4 = Button(frm, text="Excluir", command=root.option_add, width= 10).grid(column=0, row=4)
frm.pack()
     
#---------------------------------------- CRIAR PAGINAS -------------------------------------------------#

framecadastrar = Frame(root, bg="#021C2F")

framefunc = Frame(root, bg="#021C2F")

framevisitante = Frame(root, bg="#021C2F")

#------------------------------------------ CADASTRAR ------------------------------------------------------#

Label(framecadastrar, text="Opções de cadastro",  bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0)
func = Button(framecadastrar, text="Funcionário", command=funcionario, width=10).grid(column=0, row=4, padx=(0, 120), pady=30)
cliente = Button(framecadastrar, text="Visitante", command=visitantes, width=10).grid(column=0, row=4, padx=(120, 0), pady=10)


Button(framecadastrar, text="Volte para a tela inicial", command=volta_cadastro).grid(column=0, row=5)


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


RegistrarButton = Button(framefunc, text="Registrar A", width=35, command=armazenar).grid(column=0, row=14)

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

#-----------------------------Armazenamento dos clientes ---------------------------------------------------------#

def armazenarC():

    valor = 0 

    Id_cliente = Ida.get()

    nome_cliente = nomeC.get()

    idade_cliente = idade.get()

    rg_cliente = rg.get()

    ingreso_tipo = ingressoT.get()

    ingresso_quant = ingressoQ.get()

    if ingreso_tipo =="P" or ingreso_tipo =="p":
        valor = 50 * ingresso_quant

    elif ingreso_tipo =="V" or ingreso_tipo == "v":
        valor = 75 * ingresso_quant
    
    cursor.execute(f"INSERT INTO funcionarios (id_clientes, nome_clientes, idade_clientes, rg_clientes, ingreso_tipo, ingresso_quant, ingresso_valor) VALUES ({Id_cliente}, '{nome_cliente}', {idade_cliente}, {rg_cliente}, '{ingreso_tipo}', {ingresso_quant}, {valor}")

    conexao_banco.commit()

RegistrarButton = Button(framevisitante, text="Registrar C", width=35, command=armazenarC).grid(column=0, row=14)

root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
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

root.attributes('-fullscreen', True)

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

Label(framefunc, text="Nome: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=0, padx=(0, 400))
nome = Entry(framefunc, width=45, font=(("Arial", 12))).grid(column=0, row=0, padx=(100, 0))

Label(framefunc, text="CPF: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=2, padx=(0, 400))
cpf = Entry(framefunc, width=45, font=(("Arial", 12))).grid(column=0, row=2, padx =(100, 0))

Label(framefunc, text="Email: ", bg="#021C2F", fg="#FFFFFF", font="Arial").grid(column=0, row=4, padx=(0, 400))
Id = Entry(framefunc, width=45, font=(("Arial", 12))).grid(column=0, row=4, padx=(100, 0))

root.mainloop()

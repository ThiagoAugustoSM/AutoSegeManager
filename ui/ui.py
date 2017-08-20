import sys
sys.path.append('../data')
from tkinter import *
from jsonFunc import jsonFunc
from guiStatus import notificacao

class GUI():

	def __init__(self, root):
		self.janela = root
		self.menubar = Menu(self.janela)
		self.json = jsonFunc()
		self.iniciando_menu()
		self.state = 0
		self.createAllFrames()
		borda1 = Label()
		#self.menubar["bg"] = ""
		self.janela.iconbitmap('../img/SEGEicon2.ico')
		self.janela.title("Auto Sege Manager")
		self.janela.geometry("800x600+300+100")
		self.janela["bg"] = "#778899"
		self.janela.config(menu=self.menubar)

	def createAllFrames(self):
		json = jsonFunc()
		self.FrameAddAluno = Frame(self.janela, bg="#778899")
		self.margem1 = Label(self.FrameAddAluno, width = 10,bg = "#778899").grid(row = 0, column = 0, rowspan =4)
		self.margem2 = Label(self.FrameAddAluno,height = 4, bg = "#778899").grid(row = 0, column = 0, columnspan =4)
		self.labelNome = Label(self.FrameAddAluno, text = "Nome do Aluno: ", width = 15, height = 5, bg = "#778899", anchor = E).grid(row = 1, column = 1)
		self.labelcpf = Label(self.FrameAddAluno, text = "CPF: ", width = 15, height =5,  bg = "#778899", anchor = E).grid(row = 2, column = 1)
		self.labeldata = Label(self.FrameAddAluno, text = "Data de nascimento: ", width = 15, height = 5, bg = "#778899").grid(row = 3, column = 1 )
		self.labelturma = Label(self.FrameAddAluno, text = "Turma: ", width = 15, height =5,  bg = "#778899", anchor = E).grid(row = 4, column = 1 )
		self.entryNome = Entry(self.FrameAddAluno).grid(row = 1, column = 2)
		self.entryCPF = Entry(self.FrameAddAluno).grid(row = 2, column = 2)
		self.entryData = Entry(self.FrameAddAluno).grid(row = 3, column = 2)
		self.entryTurma = Entry(self.FrameAddAluno).grid(row = 4, column = 2)
		self.btSalvar = Button(self.FrameAddAluno, text = ("Adicionar Aluno"), 
		                    width  = 20, height = 3 , bg = "#778899", 
		                    activebackground = "#DCDCDC", 
		                    command =lambda: self.json.adicionarAluno(entryNome.get(), entryData.get())).grid(row = 5, column = 1, columnspan = 2)


		self.FrameSearchAluno = Frame(self.janela, bg="#778899")   
		margem1 = Label(self.FrameSearchAluno, width = 10,bg = "#778899")
		margem2 = Label(self.FrameSearchAluno,height = 4, bg = "#778899")

		escolha = IntVar()
		explicacao = Label(self.FrameSearchAluno,text = "Escolha a forma de pesquisa", bg = "#778899", height = 3)
		escolhanome = Radiobutton(self.FrameSearchAluno, text="Nome", variable = escolha,  value = 1, bg = "#778899",activebackground = "#DCDCDC",   height = 3)
		self.escolhacpf = Radiobutton(self.FrameSearchAluno, text="CPF", variable = escolha,  value = 2, bg = "#778899",activebackground = "#DCDCDC",   height = 3)
		escolhaid = Radiobutton(self.FrameSearchAluno, text="ID", variable = escolha,  value = 3, bg = "#778899", activebackground = "#DCDCDC",   height = 3)
		aux = Label(self.FrameSearchAluno, height = 2,bg = "#778899")
		self.stringNomeEntrada = StringVar()
		self.entradaNome = Entry(self.FrameSearchAluno)
		self.dadosAluno = Label(self.FrameSearchAluno, font= ("Arial", 20), textvariable = self.stringNomeEntrada, bg = "#778899", width = 15, height = 3).grid(row = 3, column = 3)
		btpesquisar= Button(self.FrameSearchAluno, text = ("Pesquisar Aluno"),
						 width  = 20, height = 3 , bg = "#778899",
						  activebackground = "#DCDCDC",
						  command = lambda: self.refreshFrameSearchAluno())

		margem1.grid(row = 0, column = 0, rowspan =4)
		margem2.grid(row = 0, column = 0, columnspan =4)
		explicacao.grid(row = 1, column = 1)
		escolhanome.grid(row = 2, column = 1)
		self.escolhacpf.grid(row = 3, column = 1)
		escolhaid.grid(row = 4, column = 1 )
		aux.grid(row = 5, column =1)
		self.entradaNome.grid(row = 6, column = 1)
		aux.grid(row = 7, column =1)
		btpesquisar.grid(row = 8, column = 1, columnspan = 2)

	def refreshFrameSearchAluno(self):
		recebidos = self.json.pesquisarAluno(self.entradaNome.get())
		self.stringNomeEntrada.set(str(recebidos[0]) + '\n' + recebidos[1] + '\n' + recebidos[2])
		print(self.json.pesquisarAluno(self.entradaNome.get()))
		self.dadosAluno.config(text='Button Pressed')
		#self.stringNomeEntrada.set() = str((self.json.pesquisarAluno(self.entradaNome.get())[0]))
		print(self.stringNomeEntrada)
		self.janela.update()

	def addFrameAddAluno(self):

		if(self.state != 1):
			self.killFrames()
			self.FrameAddAluno.grid()
			self.state = 1

	def killFrames(self):
		self.state = 0
		self.FrameAddAluno.grid_forget()
		self.FrameSearchAluno.grid_forget()

	def addFrameSearchAluno(self):
	    
		if(self.state != 2):
			self.killFrames()
			self.FrameSearchAluno.grid()
			#self.state = 2

	def iniciando_menu(self):
		alunomenu = Menu(self.menubar, tearoff=0)
		alunomenu.add_command(label="Adicionar", command = self.addFrameAddAluno)

		alunomenu.add_command(label="Pesquisar", command= self.addFrameSearchAluno)
		#alunomenu.add_command(label="Save", command="donothing")
		#alunomenu.add_command(label="Close", command="donothing")

		alunomenu.add_separator()

		alunomenu.add_command(label="Sair", command=self.janela.quit)
		self.menubar.add_cascade(label="Alunos", menu=alunomenu)

		instrutormenu = Menu(self.menubar, tearoff=0)

		instrutormenu.add_command(label="Adicionar", command="donothing")
		instrutormenu.add_command(label="Pesquisar", command="donothing")

		self.menubar.add_cascade(label="Instrutores", menu=instrutormenu)

		calendario = Menu(self.menubar, tearoff=0)
		calendario.add_command(label="Notificações", command= notificacao)
		calendario.add_command(label="Sobre...", command="donothing")

		self.menubar.add_cascade(label="Calendário", menu=calendario)

		ajudamenu = Menu(self.menubar, tearoff=0)
		ajudamenu.add_command(label="Tutorial", command="donothing")
		ajudamenu.add_command(label="Sobre...", command="donothing")
		self.menubar.add_cascade(label="Ajuda", menu=ajudamenu)

root = Tk()
window = GUI(root)
root.mainloop()

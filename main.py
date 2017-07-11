import json
import time
from datetime import datetime
from usuarios import Aluno, Instrutor
from jsonFunc import jsonFunc

aluno = Aluno('Thiago', '12/03/98')
instrutor = Instrutor('Raquel', '21/06/1985')

state = 0 #variavel para o controle da maquina de estados

#Funcao dias entre duas datas
def days_between(d1):
    dataAtual = datetime.now()
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    print(d1.year)
    print (abs((dataAtual - d1).days))

days_between("12/3/1998")

while True:
    state = int(input("Digite o valor do estado:"))
    if(state == 0):
        nome = input("digite um nome")
        data = input("digite uma data")
        state = jsonFunc.adicionarAluno(nome, data)
    elif(state == 1):
        state = adicionarInstrutor()
    elif(state == 2):
        pass
    elif(state == 3):
        pass
    elif(state == 4):
        nome = input("digete o nome:")
        state = jsonFunc.pesquisarAluno(nome)
    elif(state == 5):
        nome = input("digete o nome:")
        state = jsonFunc.pesquisarInstrutor(nome)
    elif(state == 6):
        state = todosAlunos()
    elif(state == 7):
        state = todosInstrutores()
    elif(state == 8):
        break

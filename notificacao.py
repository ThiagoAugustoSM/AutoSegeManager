from datetime import datetime
from jsonFunc import jsonFunc

class Notificacao():

    def __init__():
        pass

    def days_between(dataAniversario):
        dataAtual = datetime.now()
        data = dataAniversario.split('/')
        data[2] = str(dataAtual.year)
        dataAniversario = data[0] + '/' + data[1] + '/' + data[2]
        dataAniversario = datetime.strptime(dataAniversario, "%d/%m/%Y")
        return -(dataAtual - dataAniversario).days

    def printDiasAniversario(nome, num):
        if(num < 0):
            print("Já se passaram ", -num, " dias para o aniversário de " + nome)
        if(num == 0):
            print("O aniversário de " + nome + " é hoje!")
        if(num > 0):
            print("Faltam ", num, " dias para o aniversário de " + nome)

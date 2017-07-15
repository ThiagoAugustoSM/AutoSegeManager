from datetime import datetime

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

    def printDiasAniversario(nome, num, dataAniversario):
        if(num < 0):
            print("Já se passaram", -num ," dias para o aniversário de ", nome,
                    "\nData Aniversário:", dataAniversario, "de", nome)
        elif(num == 0):
            print("O aniversário de", nome, " é hoje!")
        elif(num > 0):
            print("Faltam" , num ," dias para o aniversário de", nome,
                    "\nData Aniversário:", dataAniversario, "de", nome)

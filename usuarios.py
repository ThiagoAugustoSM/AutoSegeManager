class Aluno:

    def __init__(self, nome, dataNascimento):
        self.nome = nome
        self.dataNascimento = dataNascimento

    def mudarNomeAluno(self, novoNome):
        self.nome = novoNome

    def mostrarNomeAluno(self):
        print(self.nome)

    def validaData():
        data = ""
        while len(data.split('/')) != 3:
            data = (input("Digite a data de nascimento no formato DD/MM/AAAA: "))
        print("Formato Válido, obrigado pelos dados!")
        return data

class Instrutor:

    def __init__(self, nome, dataNascimento):
        self.nome = nome
        self.dataNascimento = dataNascimento

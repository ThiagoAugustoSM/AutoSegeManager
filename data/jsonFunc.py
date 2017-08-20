import json
from notificacao import Notificacao

class jsonFunc():

    def __init__(self):
        self.path = '../data/jsonData/alunos.json' 
        pass

    def adicionarAluno(self, nome, dataNascimento):
        # Reading data back
        with open(self.path, 'r') as f:
            data = json.load(f)
            data['alunos'].append({'nome': str(nome),
                                'id': str(len(data['alunos']) + 1),
                                'dataNascimento': str(dataNascimento)
                                })
            for alunos in data['alunos']:
                print('Nome: ' + alunos['nome'])
                print('ID: ' + alunos['id'])
                print('Data de Nascimento: ' + alunos['dataNascimento'])
                print(Notificacao.days_between(alunos['dataNascimento']))
                print('')
        # Writing JSON data
        with open(self.path, 'w') as f:
             json.dump(data, f, indent=4)
        return 4

    def adicionarInstrutor(self, nome, dataNascimento):
        # Reading data back
        with open(self.path, 'r') as f:
            data = json.load(f)
            data['alunos'].append({'nome': str(nome),
                                'id': str(len(data['alunos']) + 1),
                                'dataNascimento': str(dataNascimento)
                                })
            for alunos in data['alunos']:
                print('Nome: ' + alunos['nome'])
                print('ID: ' + alunos['id'])
                print('Data de Nascimento: ' + alunos['dataNascimento'])
                print(Notificacao.days_between(alunos['dataNascimento']))
                print('')
        # Writing JSON data
        with open(self.path, 'w') as f:
             json.dump(data, f, indent=4)
        return 4

    def pesquisarAluno(self, nome):

        with open(self.path, 'r') as f:
            data = json.load(f)
            for aluno in data['alunos']:
                #print(aluno['nome'])
                if(aluno['nome'] == nome):
                    print('Nome: ' + aluno['nome'])
                    print('ID: ' + aluno['id'])
                    print('Data de Nascimento: ' + aluno['dataNascimento'])
                    print('')
                    return [aluno['nome'], aluno['id'], aluno['dataNascimento']]
        return 8

    def notificacaoAluno(self, quantidadeDias):

        with open(self.path, 'r') as f:
            data = json.load(f)
            for aluno in data['alunos']:
              	if(-quantidadeDias <= Notificacao.days_between(aluno['dataNascimento']) <= quantidadeDias):
                    print(aluno['nome'])
                    Notificacao.printDiasAniversario(aluno['nome'], Notificacao.days_between(aluno['dataNascimento']), aluno['dataNascimento'])
        return 8

    def retornoNotificacaoAluno(self, quantidadeDias):
        listaAlunos = []
        with open(self.path, 'r') as f:
            data = json.load(f)
            for aluno in data['alunos']:
              	if(-quantidadeDias <= Notificacao.days_between(aluno['dataNascimento']) <= quantidadeDias):
                    print(aluno['nome'])
                    listaAlunos.append(Notificacao.retornaDiasAniversario(aluno['nome'], Notificacao.days_between(aluno['dataNascimento']), aluno['dataNascimento']))
        return listaAlunos

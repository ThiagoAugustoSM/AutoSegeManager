import json
from notificacao import Notificacao

class jsonFunc():

    def __init__(self):
        pass

    def adicionarAluno(nome, dataNascimento):
        # Reading data back
        with open('jsonData/alunos.json', 'r') as f:
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
        with open('jsonData/alunos.json', 'w') as f:
             json.dump(data, f, indent=4)
        return 4

    def adicionarInstrutor(nome, dataNascimento):
        # Reading data back
        with open('jsonData/funcionarios.json', 'r') as f:
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
        with open('jsonData/alunos.json', 'w') as f:
             json.dump(data, f, indent=4)
        return 4

    def pesquisarAluno(nome):

        with open('jsonData/alunos.json', 'r') as f:
            data = json.load(f)
            for aluno in data['alunos']:
                print(aluno['nome'])
                if(aluno['nome'] == nome):
                    print('Nome: ' + aluno['nome'])
                    print('ID: ' + aluno['id'])
                    print('Data de Nascimento: ' + aluno['dataNascimento'])
                    print('')
                    break
        return 8

    def notificacaoAluno(quantidadeDias):

        with open('jsonData/alunos.json', 'r') as f:
            data = json.load(f)
            for aluno in data['alunos']:
              	if(-quantidadeDias <= Notificacao.days_between(aluno['dataNascimento']) <= quantidadeDias):
                    print(aluno['nome'])
                    Notificacao.printDiasAniversario(aluno['nome'], Notificacao.days_between(aluno['dataNascimento']), aluno['dataNascimento'])
        return 8

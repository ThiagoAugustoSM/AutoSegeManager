import json

class jsonFunc():

    def __init__(self):
        pass

    def adicionarAluno(nome, dataNascimento):
        # Reading data back
        with open('jsonData/alunos.json', 'r') as f:
             data = json.load(f)
             data['alunos'].append({'nome': nome,
                                    'id': str(len(data['alunos']) + 1),
                                    'dataNascimento': dataNascimento
                                    })
             for p in data['alunos']:
                print('Nome: ' + p['nome'])
                print('ID: ' + p['id'])
                print('Data de Nascimento: ' + p['dataNascimento'])
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

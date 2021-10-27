from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Lins', idade=46)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    # pessoa = Pessoas.query.filter_by(nome='James')
    # for p in pessoa:
    #     print(p)

    pessoa = Pessoas.query.filter_by(nome='James').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lins').first()
    # pessoa.idade = 30
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
from infeng import Engine

def asking(value):
    while True:
        i = input(value.description).lower()
        if i == 'sim':
            value.value = True
            return
        elif i == 'nao':
            value.value = False
            return
        else:
            print('Resposta inválida. Tente novamente.')


eng = Engine('knowledge_base.json', asking)

print('Bem vindo ao bot de recomendação de filmes!')
print('Você deverá responder as perguntas com um sim (caso afirmativo) ou nao (caso falso)')
print('Iniciando avaliação...')



while True:
    if(eng.evaluate('Lista1') == True):
        print('Comedia 1, 2 e 3')
        break
    else:
        print('Esses filmes não são para você!')
        break

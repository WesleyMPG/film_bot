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

print('---------------------------------------------------------------------')
print('Bem vindo ao bot de recomendação de filmes!')
print('---------------------------------------------------------------------')
print('VOCÊ DEVERÁ RESPONDER sim (caso afirmativo) ou nao (caso falso)')
print('---------------------------------------------------------------------')
print('Iniciando avaliação...')
print('---------------------------------------------------------------------')


while True:
    if(eng.evaluate('Lista1') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l100')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L01')
        break
    elif(eng.evaluate('Lista2') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l200')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L02')
        break
    elif(eng.evaluate('Lista3') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l300')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L03')
        break
    elif(eng.evaluate('Lista4') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l400')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L04')
        break
    elif(eng.evaluate('Lista5') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l500')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L05')
        break
    elif(eng.evaluate('Lista6') == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l600')
        print('---------------------------------------------------------------------')
        print('CÓDIGO DA OPERAÇÃO: L06')
        break
    else:
        print('Esses filmes não são para você!')
        break

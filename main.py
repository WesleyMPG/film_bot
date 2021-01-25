import re
from infeng import Engine

def asking(value):
    while True:
        i = input(value.description+' ').lower()
        if i == 'sim':
            value.value = True
            break
        elif i == 'nao':
            value.value = False
            break
        else:
            print('Resposta inválida. Tente novamente.')
    while True:
        c = input(f'Quão certo você está disso (%)? ').lower()
        found = re.match(r'^\d{1,2}([\.,]\d+)?$|^100$', c)
        if found is not None:
            if ',' in c:
                c = c.replace(',', '.')
            value.confidence = float(c)
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


def main():
    result, confidence = eng.evaluate('Lista1')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l100')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L01')
        return
    result, confidence = eng.evaluate('Lista2')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l200')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L02')
        return
    result, confidence = eng.evaluate('Lista3')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l300')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L03')
        return
    result, confidence = eng.evaluate('Lista4')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l400')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L04')
        return
    result, confidence = eng.evaluate('Lista5')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l500')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L05')
        return
    result, confidence = eng.evaluate('Lista6')
    if(result == True):
        print('---------------------------------------------------------------------')
        print('PREPARAMOS UMA LISTA COM FILMES SELECIONADOS PARA VOCÊ ASSISTIR HOJE!')
        print('ACESSE ESSE LINK E CONFIRA --> https://cutt.ly/recomendacao_de_filmes_0l600')
        print('---------------------------------------------------------------------')
        print(f'\nNível de confiaça: {confidence}\n')
        print('CÓDIGO DA OPERAÇÃO: L06')
        return
    print('Esses filmes não são para você!')


main()

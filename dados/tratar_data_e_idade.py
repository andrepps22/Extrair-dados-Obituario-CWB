############################# IMPORTS ##########################################
import locale
from datetime import datetime
################################################################################


def formatar_data(date: str):
    '''
        Recebe uma data por ex: 'sexta-feira, 9 de outubro de 2022' e retorna 09-10-2022
    '''
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    data = date
    data_nova = data.split()
    if data_nova[3] == "marco":
        data_nova.remove('marco')
        data_nova.insert(3, 'março')

    data_tratada = datetime.strptime(
        f'{data_nova[1]}-{data_nova[3]}-{data_nova[5]}', '%d-%B-%Y')

    return data_tratada.date()


def formatar_idade(idade: str):
    '''
        Recebe a idade passada por ex: '25 anos(s) e retora somente o numero inteiro(int)
    '''
    idade_separada = idade.split()
    for idade_tratada in idade_separada:
        if idade_tratada.isnumeric():

            return int((idade_tratada))


if __name__ == '__main__':
    print(formatar_data('q 13 de marco de 2022'))

############################# IMPORTS ##########################################
from .tratar_data_e_idade import formatar_data, formatar_idade
from BD.banco_de_dados import Falecidos, session
from datetime import datetime
from sqlalchemy.future import select
################################################################################

# VARIAVEIS
data_now = datetime.now()
lista_dados = []
temp = {}


def inserir_dados():
    '''
        Ler o arquivo 'Falecidos.txt' e joga os dados para o banco de dados.
    '''
    cont = 0
    # vai ler arquivo que está com texto puro e transforma em varios dicionarios que vão ser armazenados em uma lista
    with open('falecidos.txt', 'r') as file:
        arquivo = file.readlines()
        for index, linha in enumerate(arquivo):
            if linha.__contains__(':\n'):
                temp[linha.replace(':\n', '')] = arquivo[index +
                                                         1].replace('\n', '').rstrip()
            if linha == 'Funeraria:\n':
                lista_dados.append(temp.copy())
                temp.clear()

    # pega todos os dados da lista_dados que contem varios dicionarios e insere em variaveis
    for dados in lista_dados:
        nome = dados['Nome']
        data_do_falecimento = formatar_data(dados['Data do Falecimento'])
        idade = formatar_idade(dados['Idade'])
        profissao = dados['Profissao']
        nome_do_pai = dados['Nome do Pai']
        nome_da_mae = dados['Nome da Mae']

        # Checa se o Falecido possui conjuge caso não tenha insere um campo vazio no banco
        if 'Conjuge' in dados:
            conjuge = dados['Conjuge']
        else:
            conjuge = ''

        numero_da_FAF = dados['Numero da FAF']
        local_do_falecimento = dados['Local do Falecimento']
        local_do_velorio = dados['Local do Velorio']
        local_do_sepultamento = dados['Local do Sepultamento']
        data_do_sepultamento = formatar_data(dados['Data do Falecimento'])
        funeraria = dados['Funeraria']

        query = session.execute(
            select(Falecidos).where(
                Falecidos.nome == nome,
                Falecidos.idade == idade,
                Falecidos.nome_da_mae == nome_da_mae
            ))
        result = query.scalars().all()

        # Se o resultado da buscar trouxer valores(True) não insere nenhum dados pois está repitido, caso não traga nenhum resultado(False) insere os dados na instancia do banco.
        if result:
            continue
        else:
            # Instacia que vai fazer a inserção dos dados no banco de dados
            falecidos = Falecidos(data_insercao=data_now, nome=nome, data_do_falecimento=data_do_falecimento, idade=idade, profissao=profissao, nome_do_pai=nome_do_pai,
                                  nome_da_mae=nome_da_mae, conjuge=conjuge, numero_da_FAF=numero_da_FAF, local_do_falecimento=local_do_falecimento, local_do_velorio=local_do_velorio,
                                  local_do_sepultamento=local_do_sepultamento, data_do_sepultamento=data_do_sepultamento, funeraria=funeraria)

            session.add(falecidos)
            session.commit()
            cont += 1

    session.close()  # Encerrando a sessão

    print(f'Foram inseridos {cont} registros')


if __name__ == '__main__':
    inserir_dados()

import requests
import unidecode
from bs4 import BeautifulSoup as bs


def buscar_dados():
    """
        faz o scrap da pagina de obituarios da prefeitura e criar o arquivo falecidos.txt
    """
    pagina = 'https://obituarios.curitiba.pr.gov.br/publico/falecimentos.aspx'

    pag = requests.get(pagina)
    soup = bs(pag.text, 'html.parser')
    texto = ''

    # Faz a busca somente das TAG 'td' que estão dentro da TAG HTML TABLE/TR
    for palavra in soup.find_all('td'):
        p = palavra.get_text()  # Retira todas as TAGS HTML e retorna texto puro tratado

        # Retira acentos caracteres especias
        unicode_string = unidecode.unidecode(p)

        texto += unicode_string + '\n'  # Junto todo o texto tratado em uma variavel

    # Criar o arquivo txt dos dados colhidos
    with open('falecidos.txt', 'w+') as file:
        file.write(str(texto))

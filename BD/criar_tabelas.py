# Criando a tabela no banco de dados
# OBS: SOMENTE SE A TABELA NÃO EXISTE CASO EXISTA IGNORAR ESTE ARQUIVO.

from BD.banco_de_dados import Base, session, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session.close()

from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from logins import login, senha

engine = create_engine(
    f'mysql+pymysql://{login}:{senha}@localhost:3306/falecidos')

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

session = Session()

Base = declarative_base()


class Falecidos(Base):
    __tablename__ = 'falecidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_insercao = Column(String(250))
    nome = Column(String(250))
    data_do_falecimento = Column(Date)
    idade = Column(Integer)
    profissao = Column(String(250))
    nome_do_pai = Column(String(250))
    nome_da_mae = Column(String(250))
    conjuge = Column(String(250))
    numero_da_FAF = Column(String(250))
    local_do_falecimento = Column(String(250))
    local_do_velorio = Column(String(250))
    local_do_sepultamento = Column(String(250))
    data_do_sepultamento = Column(Date)
    funeraria = Column(String(250))

    def __repr__(self) -> str:
        return f'{self.nome}'

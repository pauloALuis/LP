"""
Paulo Luis 17359
pg1.py
30/08/2021
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from flask import Flask, render_template

#1.a)
engine = create_engine('sqlite:///colegas.sqlite3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

#1.b)
class Contato(Base):
    __tablename__ = 'contato'

    id = Column(Integer, primary_key=True)
    nome = Column('nome', String(32))
    telefone = Column('telefone', String(32))
    email = Column('email', String(32))

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Mensagem(Base):
    __tablename__ = 'mensagem'

    id = Column(Integer, primary_key=True)
    destinatario = Column('destinatario', ForeignKey("contato.id"), nullable=False)
    texto = Column('texto', String(140))

    def __init__(self, destinatario, texto):
        self.destinatario = destinatario
        self.texto = texto

Base.metadata.create_all(engine)
session = Session()

#1.c)
"""
*******************************************************************************
**************************** Inserção de dados ********************************
*******************************************************************************
"""
def inserir_contatos():
    Contatos =   [Contato('Maria', '912345678', 'maria@gmail.com'), 
                Contato('Pedro', '919999999', 'pedro@hotmail.com'), 
                Contato("Bernardo", '916587688', "bernardo.martinho.marques@gmail.com")]
    session.add_all(Contatos)
    session.commit()
#inserir_contatos()

def insert_mensagens():
    Mensagens =   [Mensagem(1, "Olá"), Mensagem(2, "Olá, tudo bem?"), Mensagem(1, "Oi oi"), Mensagem(1, "Como estás?"), ]
    session.add_all(Mensagens)
    session.commit()
#insert_mensagens()


"""
*******************************************************************************
**************************** Consultas de dados *******************************
*******************************************************************************
"""
def consultar_all_contatos():
    dados = session.query(Contato).all()
    for linha in dados:
        print(f'Id: {linha.id} - Nome: {linha.nome} - Telefone: {linha.telefone} - Email: {linha.email}')
#consultar_all_contatos()

def consultar_all_mensagens():
    dados = session.query(Mensagem).all()
    for linha in dados:
        print(f'Id: {linha.id} - Texto: {linha.texto}')
consultar_all_mensagens()


def consultar_mensagens_from_desteny():
    dados = session.query(Mensagem).all()
    for linha in dados:
        telefone = session.query(Contato).filter(Contato.id == linha.destinatario).one().telefone
        nome = session.query(Contato).filter(Contato.id == linha.destinatario).one().nome
        print(f'Id: {linha.id} - Destinatario: {nome} - Nº: {telefone} - Texto: {linha.texto}')
#consultar_mensagens_from_desteny()

def consultar_mensagens_from_desteny2(id : int = 1):
    dados = session.query(
        Contato, Mensagem).filter(Contato.id == Mensagem.destinatario,).filter(Contato.id == id).all()
    print("Mensagens para ", dados[0][0].nome, " com o número de telefone ", dados[0][0].telefone, ":")
    i = 0
    for linha in dados:
        i += 1
        print("Mensgaem ", str(i),": ", linha[1].texto)
#consultar_mensagens_from_desteny2()

#1.d)
def consultar_contato_filter(number: str = '916587688'):
    dados = session.query(Contato).filter(Contato.telefone == number).all()
    for linha in dados:
        print(f'Id: {linha.id} - Nome: {linha.nome} - Telefone: {linha.telefone} - Email: {linha.email}')
#consultar_contato_filter()

def update_contato(id: int):
    print('Nome ANTES da alteração:', session.query(Contato).filter(Contato.id == id).one().nome)
    session.query(Contato).filter(Contato.id == 1).update({'nome': 'Roberto', 'email': 'roberto@gmail.com'})
    session.commit()
    print('Nome DEPOIS da alteração:', session.query(Contato).filter(Contato.id == 1).one().nome)
#update_contato(1)

session.close()

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')
app.run()
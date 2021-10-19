from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluno.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Disciplina(db.Model):
   id = db.Column('disciplina_id', db.Integer, primary_key = True)
   disciplina = db.Column(db.String(100))
   semestre = db.Column(db.String(50))
   ects = db.Column(db.String(200)) 
   nota = db.Column(db.String(10))

   def __init__(self, disciplina, semestre, ects, nota):
      self.disciplina = disciplina
      self.semestre = semestre
      self.ects = ects
      self.nota = nota

def insert_disciplinas():
    disciplinas =   [Disciplina('LP', '1º', 6, 20), Disciplina('EDA', '2º', 6, 19.5)]
    db.session.add_all(disciplinas)
    db.session.commit()

def delete_disciplina(id: int):
   disciplina = db.session.query(Disciplina).filter(Disciplina.id == id).first()
   db.session.delete(disciplina)
   db.session.commit()

x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
sin = np.sin(x)

@app.route('/')
def home():
   images = ["imagem1.jpg", "imagem2.jpg", "imagem3.jpg"]
   return render_template('home.html', disciplinas = Disciplina.query.all(), images = images)

@app.route('/other')
def other():
   return render_template('other.html')
   
if __name__ == '__main__':
   db.create_all()
   images = []
   app.run(port=18373, debug = True)



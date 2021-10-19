"""
Paulo Luis 17359
questao4.py
31/08/2021
"""

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"

marcas = [["1", "Mercedes", 10000], ["2", "Audi", 9000], ["3", "BMW" , 8000], ["4", "Opel", 7000]]

@app.route('/')
def home():
    """
    função que trata do encaminhamento do URL principal
    redireciona par a pagina marca.html que está na pasta templates
    """
    return render_template('marca.html', len = len(marcas), marca = marcas[0])

@app.route('/<int:id>')
def marca(id):
    """
    função que trata do encaminhamento do URL /<id>
    redireciona par a pagina marca.html que está na pasta templates com o id dinâmico
    @param id : id da marca de automoveis
    """
    id=id
    return render_template('marca.html', len = len(marcas), marca = marcas[int(id)])

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    """
    função que trata do encaminhamento do URL /lista
    redireciona par a pagina lista.html que está na pasta templates
    esta pagina contem a lista de marcas de automoveis
    """
    return render_template('lista.html',len = len(marcas), marcas = marcas)
   
if __name__ == '__main__':
   app.run(port=18373, debug = True) # corre a aplicação


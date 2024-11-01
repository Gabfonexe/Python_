from flask import Flask, render_template

# Sempre usar na primeira vez que usar o Flask, esse comando - set FLASK_APP=app.py / Isso configura a variavel de ambiente

# set FLASK_ENV=development = Define o modo de operação para desenvolvimento, com isso é possível notar a mudança do app de forma síncrona

# Sempre que for utilizar o render_template, basta colocar o nome da pasta como "templates", que ele irá reconhecer automaticamente

# Definir o nome do app // instanciando
app = Flask(__name__)

# Criar a rota
@app.route('/') #Rota principal normalmente é a /
def principal():
  nome = "Fulano"
  idade = 25
  return render_template("index.html", nome=nome, idade=idade) # Ao retornar a var nome e idade, consigo acessar ela no arquivo html do parâmetro

@app.route('/sobre')
def sobre():
  return render_template("sobre.html")




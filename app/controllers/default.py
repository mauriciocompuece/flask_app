from flask import render_template #rece arquivo html e renderiza
from app import app, db
from app.models.tables import User, Test
#from app.models.forms import LoginForm
print("default")

@app.route("/index")
@app.route("/")
def index():
    print("renderizou########")
    return render_template('index.html')

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',form=form)
#@app.route("/add/<info>")
@app.route("/add")
def add():
    i=Test("teste_user")
    db.session.add(i)
    db.session.commit()
    ##print(i,"Iiiiiiiiiiii")
    ##return i

@app.route("/select/<info>")
@app.route("/select", defaults={"info: None"})
def select(info):
    s= User.query.filter_by(username='mauricio.cardoso').first()
    print("selecionar")
    return s

@app.route("/delete/<info>")
@app.route("/delete", defaults={"info: None"})
def delete(info):
    d=Test("teste_user")
    db.session.delete(i)
    db.session.commit()
    print("deletou")
    return d

@app.route('/cadastro')
def cadastro():    
    return render_template('cadastro.html')



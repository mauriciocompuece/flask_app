from flask import render_template, request, redirect  #rece arquivo html e renderiza
from app import app, db
from app.models.tables import User, Test
#from app.models.forms import LoginForm
print("default")


@app.route("/frist")
def frist():
    print("inicio########")
    return render_template('inicio.html')

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
    i=Test(name)
    db.session.add(i)
    db.session.commit()

@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        name = request.form['name']
        test = Test(name=name)
        db.session.add(test)
        db.session.commit()
        return redirect('/data')

@app.route('/del', methods=['GET','POST'])
def deletepag():
    if request.method == 'GET':
        return render_template('delete.html')
 
    if request.method == 'POST':
        name = request.form['name']
        test = Test.query.filter_by(name=name).first()
        db.session.delete(test)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveList():
    test = Test.query.all()
    print("foi data")
    return render_template('datalist.html',test = test)

@app.route("/select/<info>")
@app.route("/select", defaults={"info: None"})
def select(info):
    s= User.query.filter_by(username='mauricio.cardoso').first()
    print("selecionar")
    return s

@app.route("/delete/<info>")
@app.route("/delete", defaults={"info: None"})
def delete(info):
    d=Test("teste_user2")
    db.session.delete(i)
    db.session.commit()
    print("deletou")
    return d

@app.route('/cadastro')
def cadastro():    
    return render_template('cadastro.html')


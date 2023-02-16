from flask import Flask
from flask_sqlalchemy import SQLAlchemy ##biblioteca sql flask
##from flask_script import Manager
##from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' ##configuração do flask
db = SQLAlchemy(app) ## instanciando database
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

print ( "entrou em uniti_app")
from app.models import tables 
from app.controllers import default
#from app.models import tables
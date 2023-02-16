from app import db
print("entrou em tables")

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column (db.String)
    email = db.Column(db.String)
    teste = db.Column (db.String)

    def __init__(self, username, password,name, email,teste):
       self.username = username
       self.password = password
       self.name = name
       self.email = email
       self.teste = teste
    
    def __repr__(self):
        return "<User %r>" % self.username  

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String)
    

    def __init__(self,name):
       self.name = name
      
    
    def __repr__(self):
        return "<Test %r>" % self.name


   

###class User (db.Model):  ##tabela de usuario 
   ### __tablename__== users

   ### id = db.Column(db.Integer, primary_key=True)
   ### username = db.Column (db.String, unique = true)
   ### password = db.Column(db.String)
   ### name = db.Column (db.String)
   ### email = db.Column(db.String)

   ### def __init__(self, username, password,name, email):
   ###     self.username = username
   ###     self.password = password
      ##  self.name = name
    ###    self.email = email
    
   ## def __repr__(self):
    #    return "<User %r>" % self.username  

#class Post (db.Model):
   # __tablename__ = "posts"
#
   # id = db.Column(db.Integer, primary_key=True)
   # content = db.Column(db.Text)
   # user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    
   # user =db.relationship('User', foreign_keys = user_id)

    #def __init__ ( self , content , user_id):
       # self.content = content
        #self.user_id = user_id
   # def __repr__(self):
        return "<Post %r>" % self.id 
    
    
##class  Follow (db.Model):
    ## __tablename__ = "follow"

   ## id = db.Column(db.Integer, primary_key=True)
   ## user_id =db.Column(db.Integer, db.ForeignKey('users_id'))
  ##  follower_id = db.relationship('User', foreign_keys = follower_id)
    ##user =db.relationship('User', foreign_keys = user_id)
   ## def __init__ ( self , user_id , follower):
      ##  self.user_id = user_id
      ##  self.follower_id= follower_id
   ## def __repr__(self):
      ##  return "<Follow %r>" % self.user_id 
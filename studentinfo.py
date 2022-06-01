from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost:3306/empdb'%quote("Admin@123")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empdb.db'
db = SQLAlchemy(app)

class Student(db.Model):
    sid = db.Column(db.Integer, primary_key = True)
    name = db.Column( db.String(100), nullable =Flask)
    cls = db.Column(db.Integer, nullable = False)
    div = db.Column(db.String(100), nullable = False)


    def __str__(self):
        return f'id : {self.sid}, name: {self.name}, cls : {self.cls}, div : {self.div}'


    def __repr__(self):
        return str(self)

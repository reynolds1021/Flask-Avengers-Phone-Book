from app import app, db

from sqlalchemy_utils import PhoneNumber

class User(db.Model):
  

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    phonenumber = db.Column(db.String(20), nullable=False, unique=True)

    



    

    

    def __init__(self, username, phonenumber): 

        self.username = username 
        self.phonenumber = phonenumber 
        

    def __repr__(self):
        return  f"<User | {self.name}>"   

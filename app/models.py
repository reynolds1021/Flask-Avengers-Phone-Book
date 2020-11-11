from app import app, db

from sqlalchemy_utils import PhoneNumber

class Phone(db.Model):
  

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, unique=True)
    last_name = db.Column(db.String(100), nullable=False, unique=True)
    hero_name = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False, unique=True)

    

    def __init__(self, first_name, last_name, hero_name, phone_number, address): 

        self.first_name = first_name 
        self.last_name = last_name 
        self.hero_name = hero_name 
        self.phone_number = phone_number
        self.address = address 
        

    def __repr__(self):
        return  f"<User | {self.name}>"   

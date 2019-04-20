from . import db
from app.models.user import user


class Pet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    raza = db.Column(db.String(20))
    
    #id_user = db.column(db.Integer,db.ForeignKey(user.id),nullable = False)
    
    
    def json(self):
        d={}
        d['id']= self.id
        d['name']= self.name
        d['raza'] = self.raza
        return d

    def getAllPets(self):
        return Pet.query.all()
from . import db,dbEngine
from app.models.user import user
from app.models.pet import Pet
class Pet_x_User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    pets = db.relationship(Pet,backref = 'Pet_x_User',lazy =True)
    users = db.relationship(user,backref = 'Pet_x_User',lazy =True)
    id_pet  = db.Column(db.Integer,db.ForeignKey(Pet.id),nullable=False)
    id_user = db.Column(db.Integer,db.ForeignKey(user.id),nullable=False)
    
    def json(self):
        d={}
        d['id']= self.id
        d['id_pet']= self.id_pet
        d['id_user'] = self.id_user
        return d
    
    @classmethod
    def getAll(self):
        return db.session.query(Pet_x_User,user,Pet).join(user,Pet).all()
    


    

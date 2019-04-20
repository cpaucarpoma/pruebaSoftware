#from app.db import getSessionServer
from . import db



#db = getSessionServer()
class user(db.Model):
    id=db.Column(db.Integer, primary_key =True)
    firstName= db.Column(db.String(50))
    lastName= db.Column(db.String(50)) 
    
    email= db.Column(db.String(100))
    gender= db.Column(db.String(10))
    status = db.Column(db.Integer) 
    dateOfBirth = db.Column(db.String(100))
    adress= db.Column(db.String(20))    
    _type = db.Column(db.Integer)
    
    _default_fields = [
        "firstName",
        "lastName",
        "email",
        "gender",
        "status",
        "dateOfBirth",
        "adress"
    ]
    
    def json(self):
        d = {}
        d['id'] = self.id
        d['firstName']= self.firstName
        d['lastName'] = self.lastName
        d['email'] = self.email
        d['gender'] = self.gender
        d['status'] = self.status
        d['dateOfBirth'] = self.dateOfBirth
        d['adress'] = self.adress
        d['_type'] = self._type
        return d

    def insert(self,newUser):
        db.session.add(newUser)
        db.session.commit()
        return

    @classmethod
    def getOneUser(self,idU):
        return user.query.filter_by(id = idU).first()
    
    @classmethod
    def getAllUser(self):
        return user.query.all()
#db.create_all()
#db.session.commit()
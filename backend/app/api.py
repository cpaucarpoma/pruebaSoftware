from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
from app.db import getSessionServer


from app.models import db
from app.models.user import user
from app.models.pet import Pet
from app.models.pet_x_user import Pet_x_User


migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
#db.session.close()

from app.resource.user import *
from app.resource.basic import Hello
from app.resource.pet import PetListarSRC
from app.resource.pet_x_userSRC import listarPet_x_UserSRC

#from app.resource.listUser import listuser

api.add_resource(agregarUsuarioSRC,'/api/user')
api.add_resource(listarUser,'/api/users/<idU>')
api.add_resource(listarUser,'/api/users',endpoint="ListUser")
api.add_resource(Hello,'/api/hello',endpoint="holaMundo")
api.add_resource(PetListarSRC,'/api/pets')
api.add_resource(listarPet_x_UserSRC,'/api/pet-x-user')
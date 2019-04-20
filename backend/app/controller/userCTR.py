from app.models.user import user
#from app.api import db

def agregarUsuarioCTR(datos):
    newUser= user(firstName = datos['firstName'],
    lastName=datos['lastName'],
    email=datos['email'],
    gender=datos['gender'],
    status=datos['status'],
    dateOfBirth=datos['dateOfBirth'],
    _type= datos['_type'],
    adress=datos['adress']
    )
    user().insert(newUser)

    rpta = newUser.json()
    rpta['codigo'] = 500
    rpta['mensaje'] = 'ok'
    rpta['dato'] = "confirmado"
    return rpta

def oneUser(idU):
    u = user().getOneUser(idU)
    rpta = u.json()
    rpta['codigo'] = 500
    rpta['mensaje'] = 'ok'  
    return rpta

def allUser():
    lista = user().getAllUser()
    res = []
    for u in lista:
        res.append(u.json())
    rpta={}
    rpta['items']=res
    rpta['totalCount']= len(res)
    return rpta
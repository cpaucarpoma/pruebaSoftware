from app.models.pet_x_user import Pet_x_User

def listar():
    lista = Pet_x_User().getAll()
    res = []
    for rela,user,pet in lista:
        aux = rela.json()
        aux['pet'] = pet.json()
        aux['user'] = user.json()
        res.append(aux)
    
    rpta={}
    rpta['items']=res
    rpta['count'] = len(res)
    return rpta
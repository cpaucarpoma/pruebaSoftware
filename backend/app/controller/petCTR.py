from app.models.pet import Pet

def listarPets():
        
        lista = Pet().getAllPets()
        #lista = Pet.query.all()
        res = []
        for p in lista:
            aux=p.json()
            res.append(aux)
        
        rpta={}
        rpta['items']=res
        rpta['totalCount'] = len(res)
        return rpta
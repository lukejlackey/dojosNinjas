from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    
    def __init__(self, data, display=False) -> None:
        if display:
            self.name = data
        else:
            for key in data.keys():
                setattr(self,key,data[key])

    
    @classmethod
    def showAll(cls):
        query = 'SELECT * FROM dojos;'
        rslt = [cls(dojo) for dojo in connectToMySQL(DATABASE).query_db(query)]
        return rslt

    @classmethod
    def showDojo(cls, id, add_ninjas=False):
        query = 'SELECT * FROM dojos '
        if add_ninjas:
            query += 'JOIN ninjas ON dojos.id = ninjas.dojo_id '
        query += f'WHERE dojos.id = {id};'
        rslt = connectToMySQL(DATABASE).query_db(query)
        if rslt:
            dojo = cls(rslt[0]['name'], display=True)
            ninjas = [Ninja(ninja, display=True).__dict__ for ninja in rslt if add_ninjas]
            return [dojo, ninjas]
        else:
            return None

    @classmethod
    def addNewDojo(cls, name):
        query = 'INSERT INTO dojos( name ) '
        query += 'VALUES( %(name)s );'
        rslt = connectToMySQL(DATABASE).query_db(query, name)
        return rslt
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    
    def __init__(self, data, display=False) -> None:
        if display:
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.age = data['age']
        else:
            for key in data.keys():
                setattr(self,key,data[key])
    
    @classmethod
    def showAll(cls):
        query = 'SELECT * FROM ninjas;'
        rslt = [cls(ninja) for ninja in connectToMySQL(DATABASE).query_db(query)]
        return rslt
    
    @classmethod
    def addNewNinja(cls, data):
        query = 'INSERT INTO ninjas( first_name, last_name, age, dojo_id ) '
        query += 'VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        rslt = connectToMySQL(DATABASE).query_db(query, data)
        return rslt
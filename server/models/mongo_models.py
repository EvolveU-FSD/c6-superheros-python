from bson.objectid import ObjectId
from pymodm.connection import connect
from pymodm import MongoModel, fields
from pymongo import IndexModel, ASCENDING
# Connect to MongoDB and call the connection "my-app".
connect("mongodb://localhost:27017/superheroes")

class Superhero(MongoModel):
    name = fields.CharField(required = True)
    alterego = fields.CharField(blank=True)
    sidekick = fields.CharField(blank=True)
    nickname = fields.CharField(blank=True)
    _cls = fields.CharField()

    class Meta:
        final = True
        indexes = [
            IndexModel(
                [("name",ASCENDING)],
                unique = True
            )
        ]
    @staticmethod
    def hello():
        print('hello')
    @classmethod
    def goodbye(cls):
        print('goodbye')
    @classmethod
    def find_all(cls):
        superheros = cls.objects.values().all()
        superheros_list = []
        for superhero in superheros:
            print(superhero)
            superhero['id'] = superhero['_id']
            del superhero['_id']
            superheros_list.append(superhero)
        return superheros_list
    @classmethod
    def create(cls, superhero_to_create): 
        if 'nickname' not in superhero_to_create:
            superhero_to_create['nickname']=None
        if 'alterego' not in superhero_to_create:
            superhero_to_create['alterego']=None
        if 'sidekick' not in superhero_to_create:
            superhero_to_create['sidekick']=None
        args = (superhero_to_create['name'],superhero_to_create['nickname'],
            superhero_to_create['alterego'],superhero_to_create['sidekick'])
        new_superhero = cls(*args,_cls="Superhero") 
        new_superhero.save()

    @classmethod
    def update_superhero(cls, id, superhero_to_update):         
        cls.objects.raw({"_id":ObjectId(id)}).update({"$set": superhero_to_update})
    @classmethod
    def delete_superhero(cls, id):
        superhero = cls.objects.get({"_id":ObjectId(id)})
        superhero.delete()

    @classmethod
    def find_by_id(cls,id):
        print(id)
        return cls.objects.values().get({"_id":ObjectId(id)})


class User(MongoModel):
    username = fields.CharField(required=True)
    password = fields.CharField(required=True)
    class Meta:
        indexes = [
            IndexModel(
                [("username",ASCENDING)],
                unique = True
            )
        ]


if __name__ == '__main__':
    Superhero.create({"name":"Spiderman","alterego":"Peter Parker"})
    # all_superheros = Superhero.find_all()

    # print(list(all_superheros))
    # Superhero.delete_superhero('60e87e713c532c42c7ad442b')
    
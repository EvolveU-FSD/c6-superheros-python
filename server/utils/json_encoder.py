import json
from bson import ObjectId
class JsonEncoder(json.JSONEncoder):

    def default(self,obj):
        if isinstance(obj,ObjectId):
            return str(obj)
        return super().default(self,obj)


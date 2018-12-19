from flask_restful import Resource, reqparse
from model.item import ItemModel

class Article(Resource):
    
    def get(self, item_name, id):
        result = ItemModel.find_by_item(item_name)
        print(result[0])
        print(result[0].__dict__)
        if id <= len(result):
            result = [x.__dict__ for x in result if x.id == id][0]       
            keys = ['title', 'item', 'source', 'date', 'content']
            result = {key : result[key]  for key in keys}
            return {'content' :result} 
        



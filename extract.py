import json
import pymongo

class NewsExtractor():
    collection = "articles_collection"
    # search_query = ""
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://micca55:wIE079CMw8fT0FNo@cluster0-sweiq.mongodb.net/test?retryWrites=true&w=majority")
        db = client.nyt_db
        self.collection = db.articles_collection



    def search(self, query):
        result = []    
        newsList = self.collection.find()
        for item in newsList:
            if query in item["headline"] or query in item["text"]:
                result.append(item)
        # result = self.collection.find({"text":query})
     
        return result
    
    

search_query = input()
extractor = NewsExtractor()
docs = extractor.search(search_query)
for x in docs:
    print(x)

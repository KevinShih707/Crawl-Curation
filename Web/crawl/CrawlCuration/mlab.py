import pymongo
from pymongo import MongoClient
# import csv
# import codecs
# import os
# from mongoengine import connect, Document, StringField,DateTimeField

MONGO_HOST = "mongodb://104820022:104820022@ds034677.mlab.com:34677/python"


DOCUMENT_NAME = "python"
'''
def mongoengine():
    # get the mlab URI from environment variables
    uri = os.getenv("mongodb://104820022:104820022@ds034677.mlab.com:34677/python")

    # connect to our database at MLAB
    connect(db='python',username='104820022',password='104820022',host=uri)
'''


def connect_mongo(collection_input):
    try:
        client = MongoClient(MONGO_HOST)
        db = client[DOCUMENT_NAME]
        return db[collection_input]
    except Exception as e:
        print('Got an error!')
        print(e)

def DB_Size():
    try:
        client = MongoClient(MONGO_HOST)
        db = client[DOCUMENT_NAME]
        return db.stats()
    except Exception as e:
        print('Got an error!')
        print(e)

def getAllDoc(collection_input):
    try:
        collection = connect_mongo(collection_input)
        return collection.find({})
    except Exception as e:
        print('Got an error!')
        print(e)

def getNewsContent(collection_input):
    try:
        collection = connect_mongo(collection_input)
        return collection.find({},{'_id':0,'content':1,'by':1})
    except Exception as e:
        print('Got an error!')
        print(e)


def getNewsInStringList(collection_input, col="content"):
    """
    抓下資料庫的文章(內文)
    :param collection_input:mongoDB上面的collection
    :param col:預設為content
    :return:文章內容(List of Strings)
    """
    news = getNewsContent(collection_input)
    list = [m[col] for m in news]
    return list


def getAllText(collection_input):
    try:
        collection = connect_mongo(collection_input)
        return collection.find({},{'_id':0,'text':1,'by':1})
    except Exception as e:
        print('Got an error!')
        print(e)

def getTextById(collection_input, Pageid):
    try:
        collection = connect_mongo(collection_input)
        return collection.find({'id':{'$regex':Pageid}},{'_id':0,'text':1,'by':1})
    except Exception as e:
        print('Got an error!')
        print(e)

def getVocabularyByTheme(title):
# input: 主題字串 ex."deault"
# output: cursor

    try:
        client = MongoClient(MONGO_HOST)
        db = client.python
        collection = db["theme"]
        return collection.find({"title":title},{"vocabulary":1})
    except Exception as e:
        print('Got an error on getVocabularyByTheme')
        print(e)

'''
def read_csv():
    reader = open(FILENAME, 'r', encoding='utf8')
    return csv.DictReader(reader, COLUMNS)
'''
def DeleteById(collection_input,id):
    try:
        collection = connect_mongo(collection_input)
        deletepage = '^'+id
        collection.remove({'id':{'$regex':deletepage}})
    except Exception as e:
        print('Got an error!')
        print(e)

def save_to_mongo(collection_input, input_data, id):
    collection = connect_mongo(collection_input)
    # data = read_csv()

    try:
        #collection.drop()
        DeleteById(collection_input,id)
        collection.insert_many(input_data)
        # result = collection.insert_many(data)
        # print('%d rows are saved to "%s" collection in "%s" document successfully!' % (len(result.inserted_ids), COLLECTION_NAME, DOCUMENT_NAME))
    except Exception as e:
        print('Got an error!')
        print(e)

'''
def findbyid():
    myClient = MongoClient("mongodb://104820022:104820022@ds034677.mlab.com:34677/python")
    myDB = myClient.python
    myCollection = myDB.post
    cursor = myCollection.find({'id':{'$regex':'^124616330906800'}},{'_id':0,'text':1,'by':1})
    for document in cursor:
        print(document['text'])
'''


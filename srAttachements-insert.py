__author__ = 'asifj'
import requests
from pymongo import MongoClient
import json
import csv
import traceback
import logging
from tabulate import tabulate
from bson.json_util import dumps

client = MongoClient('10.219.48.134', 27017)
#client = MongoClient('192.168.56.101', 27017)
db = client['ImportedEvents_NOV18']
collection = db['srAttachements']
collection_new = db['srAttachements-new1']
document_no = 0
#2506813,
documents = collection.find(no_cursor_timeout=True)[2506814:]
inserts = 0
updates = 0
for document in documents:
    for key, value in document.iteritems():
        document[key] = str(value).strip()
    key = {'caseId': document['SRID']}
    doc = collection_new.find_one({'caseId': document['SRID']})
    del document['_id']
    if not doc:
        inserts += 1
        doc_to_ins = key
        doc_to_ins['attachment'] = []
        for key, value in document.iteritems():
            document[key] = str(value).strip()
        doc_to_ins['attachment'].append(document)
        collection_new.insert(doc_to_ins)
    else:
        updates += 1
        doc['attachment'].append(document)
        collection_new.update(key, doc, upsert=True);
    print "Inserts: "+str(inserts)
    print "Updates: "+str(updates)
    print "Total: "+str(inserts+updates)

__author__ = 'asifj'
import logging
from kafka import KafkaConsumer
from pymongo import MongoClient
import re
import json
import traceback
import sys

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
)

def drop_database():
    client = MongoClient('192.168.56.101', 27017)
    client.drop_database("test")

def upsert_record(coll, doc):
    client = MongoClient('192.168.56.101', 27017)
    db = client['test']
    collection = db[coll]
    #post_id = collection.insert_one(doc).inserted_id
    key = {'caseId': doc[coll]['caseId']}
    doc = doc[coll]
    post_id = collection.update(key, doc, upsert=True);
    return post_id

# To consume messages
consumer = KafkaConsumer('SAPEvent', bootstrap_servers=['172.22.147.242:9092'], auto_commit_enable=False, auto_offset_reset="smallest")
# group_id='CLIEvent-grp',
#consumer.configure(bootstrap_servers=['172.22.147.242:9092', '172.22.147.232:9092', '172.22.147.243:9092'], auto_commit_enable=False, auto_offset_reset="smallest")
drop_database()
message_no = 1
for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                     message.offset, message.key,
    #                                     message.value))
    topic = message.topic
    partition = message.partition
    offset = message.offset
    key = message.key
    message = message.value
    if not message is None:
        try:
            document = json.loads(message)
            print document.keys()
            print message_no
            collection = document.keys()[0]
            #print document
            print upsert_record(collection, document)
        except Exception, err:
            print "CustomException"
            #print(message)
            print(traceback.format_exc())
    message_no += 1
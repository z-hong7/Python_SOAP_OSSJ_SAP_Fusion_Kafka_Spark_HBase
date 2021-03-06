#### For all old messages and new messages
__author__ = 'asifj'

import logging
from kafka import KafkaConsumer
import json
import traceback
from bson.json_util import dumps


logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
)

# To consume messages
consumer = KafkaConsumer("SAPEvent", bootstrap_servers=['172.22.147.242:9092', '172.22.147.232:9092', '172.22.147.243:9092'], auto_commit_enable=False, auto_offset_reset="smallest")
# group_id='CLIEvent-grp',
#consumer.configure(bootstrap_servers=['172.22.147.242:9092', '172.22.147.232:9092', '172.22.147.243:9092'], auto_commit_enable=False, auto_offset_reset="smallest")
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
    #print "Topic: "+str(topic)+", Partition: "+str(partition)+", Offset: "+str(offset)
    message = message.value
    print "================================================================================================================="
    if not message is None:
        try:
            document = json.loads(message)
            #print "Event Type: "+str(document.keys())
            #print "Message No: "+str(message_no)
            collection = document.keys()[0]
            #print "Collection Name: "+str(collection)
            #print "Debug Document ID: "+str(upsert_document_debug(collection, document[collection]))
            if collection == "customerMaster":
                print "customerMaster"
            elif collection == "srAttachements":
                print dumps(document, sort_keys=True)
        except Exception, err:
            print "CustomException"
            print "Kafka Message: "+str(message)
            print(traceback.format_exc())
    print "================================================================================================================="
    print "\n"
    message_no += 1
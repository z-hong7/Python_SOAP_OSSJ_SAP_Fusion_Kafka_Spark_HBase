__author__ = 'asifj'
from tabulate import tabulate
from kafka import SimpleProducer, KafkaClient
import logging
import requests
import json
import datetime
import traceback
import time
from utils import Utils

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.DEBUG
)

sr = {"srDetails" : { "srCategory4" : "", "srCategory2" : "", "srCategory3" : "", "srCategory1" : "Mis-Ship", "previousTeam" : "", "zzQ10" : "", "sirtBundle" : "", "endDate" : "20151108", "knowledgeArticle" : "", "outageInfoAvailable" : "", "sku" : "", "customerCaseNumber" : "", "yearRoundSupport" : "", "totalOutageTime" : "00000000", "zzQ3" : "", "zzQ2" : "", "zzQ1" : "", "outageImpactKey" : "", "zzQ7" : "", "zzQ6" : "", "zzQ5" : "", "zzQ4" : "", "ccList" : "", "zzQ9" : "", "zzQ8" : "", "processType" : "ZADM", "ccEngineer" : "TEST@JUNIPER.ENT", "numberOfUsersAffected" : "", "contractId" : "", "criticalOutage" : "", "previousOwnerSkill" : "", "followupMethodKey" : "ESEC", "specialRelease" : "", "release" : "LCNAT 1.0", "startDate" : "20151108", "warrantyEndDate" : "20151108", "escalation" : "", "jsaAdvisoryBoard" : "", "viaDescription" : "Telephone call", "employeeId" : "PULKITA", "severityKey" : "00", "secVulnerability" : "", "version" : "R1", "outageDescription" : "", "statusKey" : "E0004", "theaterDescription" : "AMER", "contractStatus" : "", "productSeries" : "CGNAT Logging (LCNAT)", "escalationkey" : "0", "reason" : "", "serviceProduct" : "", "processTypeDescription" : "Admin Service Request", "country" : "US", "courtesykey" : "", "betaType" : "", "entitlementChecked" : "", "smeContact" : "", "software" : "New Software", "reporterDetails" : "", "technicalCategory4" : "", "technicalCategory1" : "", "technicalCategory3" : "", "technicalCategory2" : "", "caseId" : "9999-9999-P-9989", "temperature" : "", "platform" : "LCNAT", "entitledSerialNumber" : "", "priority" : "P2 - High", "viaKey" : "202", "srReqDate" : [  { "dateStamp" : "20151026055317", "duration" : "", "dateType" : "First Responsible group assignment", "timeUnit" : "" },  { "dateStamp" : "20151026055455", "duration" : "", "dateType" : "Last Modified by SAP User", "timeUnit" : "" },  { "dateStamp" : "20151026055317", "duration" : "", "dateType" : "ACCARE First Assigned", "timeUnit" : "" },  { "dateStamp" : "20151026065317", "duration" : "", "dateType" : "First Response By", "timeUnit" : "" },  { "dateStamp" : "20151015062324", "duration" : "", "dateType" : "Requested Delivery Date Proposal", "timeUnit" : "" },  { "dateStamp" : "20151012062324", "duration" : "", "dateType" : "Create Date", "timeUnit" : "" } ], "outageKey" : "", "priorityKey" : "2", "theaterKey" : "2", "escalationLevelDescription" : "", "outageTypeKey" : "", "entitlementServiceLevel" : "", "cve" : "", "urgencyKey" : "uk", "courtesyDescription" : "", "top5" : "", "ouatgeCauseDescription" : "", "criticalIssue" : "", "jtac" : "", "followupMethod" : "Email Secure Web Link", "routerName" : "ASD", "severity" : "", "outsourcer" : "", "numberOfSystemsAffected" : "", "outageTypeDescription" : "", "build" : "", "cvss" : "", "productId" : "", "status" : "Dispatch", "externallyReported" : "", "description" : "Hi ,My mobile is not working, so please contact me on the mentioned number.Pulkit Sir,Will be going to Vodafone office for this, therefore will not be coming today.RegardABCnmsd", "raFa" : "", "entitlementSource" : "ENTITLEMENT CHECK NOT DONE", "outageCauseKey" : "", "employeeEmail" : "nikhilg1@kpit.com", "partnerFunction" : [  { "partnerName" : "JUNIPER NETWORKS", "partnerId" : "100000151", "partnerFunctionName" : "Sold-To Party", "partnerFunctionKey" : "00000001" },  { "partnerName" : "Juan-Antonio Bernal Van der Ven", "partnerId" : "0000001211", "partnerFunctionName" : "Employee Responsible", "partnerFunctionKey" : "00000014" },  { "partnerName" : "JNPRACEMEA Ccare-ADV-EMEA", "partnerId" : "0089514385", "partnerFunctionName" : "Responsible Group", "partnerFunctionKey" : "00000099" },  { "partnerName" : "Goverthanan S", "partnerId" : "0000014748", "partnerFunctionName" : "Reporter (Person)", "partnerFunctionKey" : "00000151" },  { "partnerName" : "Goverthanan S", "partnerId" : "0000014748", "partnerFunctionName" : "Created By", "partnerFunctionKey" : "ZCRBY" },  { "partnerName" : "Goverthanan S", "partnerId" : "0000014748", "partnerFunctionName" : "Modified By", "partnerFunctionKey" : "ZMODBY" } ], "escalationLevelKey" : "0", "overideOutage" : "", "serialNumber" : "", "outageImpactDescription" : "", "urgency" : "U"}}

kblinks = {"srKbLink": { "caseId": "2015-1004-T-0021", "link": [ { "kbId": "PRSEARCH1", "internalId": "0000002551", "dataSource": "PRSEARCH", "status": "", "description": "test1 description for kblink1", "kbDate": 20151005105602, "srVisibility": "PUBLIC", "sourceVisibility": "", "url": "www.prsearch1.net/test1/" } ] }}

data= {"srDetails": {"betaType": "PythonTesting", "build": "PythonTesting", "caseId": "9999-9999-P-9988", "ccEngineer": "PythonTesting", "ccList": "PythonTesting", "contractId": "PythonTesting", "contractStatus": "PythonTesting", "country": "PythonTesting", "courtesyDescription": "PythonTesting", "courtesykey": "PythonTesting", "criticalIssue": "PythonTesting", "criticalOutage": "PythonTesting", "customerCaseNumber": "PythonTesting", "cve": "PythonTesting", "cvss": "PythonTesting", "description": "PythonTesting", "employeeEmail": "PythonTesting", "employeeId": "PythonTesting", "endDate": "PythonTesting", "entitledSerialNumber": "PythonTesting", "entitlementChecked": "PythonTesting", "entitlementServiceLevel": "PythonTesting", "entitlementSource": "PythonTesting", "escalation": "PythonTesting", "escalationLevelDescription": "PythonTesting", "escalationLevelKey": "PythonTesting", "escalationkey": "PythonTesting", "externallyReported": "PythonTesting", "followupMethod": "PythonTesting", "followupMethodKey": "PythonTesting", "internalUse": "PythonTesting", "jsaAdvisoryBoard": "PythonTesting", "jtac": "PythonTesting", "knowledgeArticle": "PythonTesting", "numberOfSystemsAffected": "PythonTesting", "numberOfUsersAffected": "PythonTesting", "ouatgeCauseDescription": "PythonTesting", "outageCauseKey": "PythonTesting", "outageDescription": "PythonTesting", "outageImpactDescription": "PythonTesting", "outageImpactKey": "PythonTesting", "outageInfoAvailable": "PythonTesting", "outageKey": "PythonTesting", "outageTypeDescription": "PythonTesting", "outageTypeKey": "PythonTesting", "outsourcer": "PythonTesting", "overideOutage": "PythonTesting", "partnerFunction": [{"partnerFunctionKey": "00000001", "partnerFunctionName": "Sold-To Party", "partnerId": "100000151", "partnerName": "CENTURYLINK, INC"}, {"partnerFunctionName":"Employee Responsible","partnerFunctionKey":"00000014","partnerId":"0000018961","partnerName":"Vidhya Sadasivam"}], "platform": "PythonTesting", "previousOwnerSkill": "PythonTesting", "previousTeam": "PythonTesting", "priority": "PythonTesting", "priorityKey": "PythonTesting", "processType": "PythonTesting", "processTypeDescription": "PythonTesting", "productId": "PythonTesting", "productSeries": "PythonTesting", "raFa": "PythonTesting", "reason": "PythonTesting", "release": "PythonTesting", "reporterDetails": "PythonTesting", "routerName": "PythonTesting", "secVulnerability": "PythonTesting", "serialNumber": "PythonTesting", "serviceProduct": "PythonTesting", "severity": "PythonTesting", "severityKey": "PythonTesting", "sirtBundle": "PythonTesting", "sku": "PythonTesting", "smeContact": "PythonTesting", "software": "PythonTesting", "specialRelease": "PythonTesting", "srCategory1": "PythonTesting", "srCategory2": "PythonTesting", "srCategory3": "PythonTesting", "srCategory4": "PythonTesting", "srReqDate": [{"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}, {"dateStamp": "PythonTesting", "dateType": "PythonTesting", "duration": "PythonTesting", "timeUnit": "PythonTesting"}], "startDate": "PythonTesting", "status": "PythonTesting", "statusKey": "PythonTesting", "technicalCategory1": "PythonTesting", "technicalCategory2": "PythonTesting", "technicalCategory3": "PythonTesting", "technicalCategory4": "PythonTesting", "temperature": "PythonTesting", "theaterDescription": "PythonTesting", "theaterKey": "PythonTesting", "top5": "PythonTesting", "totalOutageTime": "PythonTesting", "urgency": "PythonTesting", "urgencyKey": "PythonTesting", "version": "PythonTesting", "viaDescription": "PythonTesting", "viaKey": "PythonTesting", "warrantyEndDate": "PythonTesting", "yearRoundSupport": "PythonTesting", "zzQ1": "PythonTesting", "zzQ10": "PythonTesting", "zzQ2": "PythonTesting", "zzQ3": "PythonTesting", "zzQ4": "PythonTesting", "zzQ5": "PythonTesting", "zzQ6": "PythonTesting", "zzQ7": "PythonTesting", "zzQ8": "PythonTesting", "zzQ9": "PythonTesting"}}

att = dict(srAttachements={"caseId": "2015-1004-T-0021",
                            "attachment": {"createdBy": "CMUSER", "dateCreated": "Mon+Oct+12+18%3A44%3A20+UTC+2015", "fileType": "",
                                           "path": "/archive/attachments/OETCLR/2015/10/04/T/20151012184420", "private": "",
                                           "sequenceNumber": "0002141498", "size": 19, "title": "Closed_JSA_Cases.xlsx",
                                           "uploadedBy": "DLCRUZ@JUNIPER.NET", "zDate": 20151012, "zTime": 114422}})

att2 = dict(srAttachements={"caseId": "9999-9999-P-9993",
                           "attachment": {"sequenceNumber": "0000026175", "title": "DK7444.txt", "zTime": 73411,
                                          "fileType": "", "private": "", "dateCreated": "20110525 073411",
                                          "createdBy": "", "path": "/archive/attachments/PCLR/2011/05/25/0334/1306334051497",
                                          "zDate": 20110525, "uploadedBy": "", "size": 8}})

# To send messages synchronously
kafka = KafkaClient('172.22.147.232:9092,172.22.147.242:9092,172.22.147.243:9092')
producer = SimpleProducer(kafka)

# Note that the application is responsible for encoding messages to type bytes
print producer.send_messages(b'SAPEvent', json.dumps(sr))
time.sleep(1)
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
try:
    document = sr
    row = []
    utils = Utils()
    row = utils.validate_sr_details( document['srDetails'], row )
except Exception:
    print Exception.message
    print(traceback.format_exc())
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "\n\n"
# Send unicode message
#producer.send_messages(b'SAPEvent', u'?????'.encode('utf-8'))
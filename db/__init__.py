import os
try:
  import pymongo, motor
except:
  os.system("pip install pymongo && pip install motor")
from pymongo import MongoClient as client
def ch(var):
  k = os.environ.get(var)
  return k
mg = ch("MONGO_URI")
database = client(mg)
mongo = databse ["XGAME"]
# MONGO DONE
try:
  import telethon
except:
  os.system("pip install telethon")
token = ch("TOKEN")
api = ch("API_ID")
hash = ch("API_HASH")

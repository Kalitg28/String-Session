from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "27823209"))
API_HASH = environ.get("API_HASH", "1d693fcf3bfea119ca1d9057b08a4495")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7963199045:AAF56QGnfSRVlxz-Oh3O02Geo-cJ_hCUxGM")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6004928770")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002327045567")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://kalitgstringsession:kalitgstringsession@cluster0.rby7z6u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))

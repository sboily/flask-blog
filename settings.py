import os

DEBUG=True
MONGO_HOST = os.getenv('MONGODB_HOST', "localhost")
MONGO_PORT = os.getenv('MONGODB_PORT', "27017")
MONGO_DBNAME = os.getenv('MONGODB_DBNAME', "blog")
SECRET_KEY = "f755389fd79862493fa2f71c55368006"

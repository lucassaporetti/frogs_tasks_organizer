from enum import Enum


class DatabaseType(Enum):
    FILE_STORAGE = 'file-storage'
    API = 'api'
    FIREBASE = 'firebase'
    MYSQL = 'mysql'
    POSTGRESS_SQL = 'postgres'
    MONGO_DB = 'mongo-db'

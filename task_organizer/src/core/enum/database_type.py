from enum import Enum


class DatabaseType(Enum):
    FILE_STORAGET = 'file-storage'
    API = 'api'
    MYSQL = 'mysql'
    POSTGRESS_SQL = 'postgres'
    MONGO_DB = 'mongo-db'

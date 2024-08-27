import os

class Config:
    SECRET_KEY = os.urandom(24)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'dahianna'
    MYSQL_PASSWORD = 'cjX)C_dokwBVi7On'
    MYSQL_DB = 'comercializadora'
    MYSQL_CURSORCLASS = 'DictCursor'

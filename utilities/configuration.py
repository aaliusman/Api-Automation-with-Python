import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


connect_config = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
}


def get_password():
    return "g*"


def connect_db():
    try:
        db_conn = mysql.connector.connect(**connect_config)
        if db_conn.is_connected():
            print("connected successfully")
            return db_conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

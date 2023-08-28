import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'willian1966',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_system;")

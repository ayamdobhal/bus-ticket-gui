import pip
try:
    import mysql.connector
except:
    print('Some dependencies are not installed. Wait while they install...')
    pip.main(['install', '--user', 'mysql-connector-python'])
    import mysql.connector

import ctypes
import json

def TableCheck(CURSOR):
    try:
        cursor.execute("select * from customer;")
        print(cursor.fetchall())
        return True
    except:
        return False

def CreateTables(CONNECTION, CURSOR):
    try:
        CURSOR.execute('''create table booking(
                    tkt_no varchar(255) primary key,
                    username varchar(255),
                    dep_from varchar(255),
                    dep_to varchar(255),
                    dep_date date,
                    meal varchar(255),
                    seat_no int(3),
                    bus_id int(10),
                    price int(7));'''
                )
        CURSOR.execute('''create table buses(
                    bus_id int(10) primary key,
                    bus_name varchar(255));'''
                )
        CURSOR.execute('''create table tkt_status(
                    tkt_no varchar(255) primary key,
                    status varchar(255));'''
                )
        CURSOR.execute('''create table customer(
                    username varchar(255) primary key,
                    password varchar(24) not null,
                    email varchar(255) not null,
                    age int(2) not null,
                    fname varchar(255),
                    lname varchar(255),
                    phone varchar(255) not null);'''
                )
        CONNECTION.commit()
        connection.close()
        print('database created succesfully!')
    except:
        print('Error')

def Credentials():
    global host
    global user
    global password
    global db

    with open('db.json', 'r') as creds:
        res = json.load(creds)
    host = res["host"]
    user = res["username"]
    password = res["password"]
    db = res["database"]    

def ConnectDB():
    global connection, cursor
    connection = mysql.connector.connect(host=host, user=user, password=password, database=db)
    if not connection.is_connected():
        print('Error connecting to the MySQL database.')
        return
    print('Connected to database.')
    cursor = connection.cursor()
    if not TableCheck(cursor):
        print('Required tables not found. Creating and continuing...')
        CreateTables(connection, cursor)
    else:
        print('Tables found! Continuing...')
    return connection, cursor

def getScreenRes():
    user32 = ctypes.windll.user32
    x, y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return x, y

width, height = getScreenRes()

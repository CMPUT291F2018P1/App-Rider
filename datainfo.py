# this is the database for the program.
# all tables are created.
# the data used for testing are originally prepared by Tanner Chell, tchell@ualberta.ca.

import sqlite3
import time
import inputdata as ind
import datetime

connection = None
cursor = None


def connect(path):
    global connection, cursor

    connection = sqlite3.connect('./dbdb.db')
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def bookings(name):
    # The member should be able to list all bookings on rides s/he offers
    global connection, cursor

    sql = "SELECT * FROM bookings WHERE bookings.email = (SELECT email FROM members WHERE members.name = ?)"
    cursor.execute(sql, (name,))
    return 

def b_cancel(name,rid):
    # The member should be able to cancel any bookings on rides s/he offers
    global connection, cursor

    data = (name,rid)
    cursor.execute('DELETE FROM bookings WHERE bookings.email = (SELECT email FROM members WHERE members.name = ?) AND rid = ?;', data)
    connection.commit()
    return

def request(rides):
    # This function is not finished, having problems that I stll can't fix.
    global connection, cursor

    sql = ''' INSERT INTO requests VALUES (?, ?, ?, ?, ?, ?) '''

    cursor.execute(''' INSERT INTO requests VALUES (?, ?, ?, ?, ?, ?) ''', rides)
    return cursor.lastrowid


def search(name):
    # The member should be able to see all his/her ride requests
    # This function search the database using the member's name provided.
    global connection, cursor
    
    sql = "SELECT * FROM requests WHERE requests.email = (SELECT email FROM members WHERE members.name = ?)"
    cursor.execute(sql, (name,))
    return

def search_pickup(name):
    # Also the member should be able to provide a location code or a city
    # and see a listing of all requests with a pickup location matching the location code or the city entered.
    # If there are more than 5 matches, at most 5 matches will be shown at a time.
    global connection, cursor
    
    sql_1 = "SELECT * FROM requests WHERE requests.pickup IN (SELECT lcode FROM locations WHERE locations.city = ?) OR requests.pickup = ? LIMIT 5"
    cursor.execute(sql_1, (name,name))
    return    
    
def search_rides(key1,key2,key3):
    global connection, cursor
    sql = "SELECT * FROM rides WHERE rides.src IN (SELECT lcode FROM locations WHERE locations.city = ?) OR rides.dst = ? LIMIT 5"
    return
    
def loadMessages(email, seen):
    global connection, cursor
    # seen == 0 -> seen = n
    # seen == 1 -> seen = y
    # seen == 2 -> seen doesn't matter, get all
    if seen == 0:
        sql = "select content from inbox where email = ? and seen ='n';"
    elif seen == 1:
        sql = "select content from inbox where email = ? and seen ='y';"
    elif seen == 2:
        sql = "select content from inbox where email = ?;"
    cursor.execute(sql, (email,))
    val = cursor.fetchall()
    return val

def getCNO(email):
    global connection, cursor
    sql = "select cno from cars where owner=?"
    cursor.execute(sql, (email,))
    val = cursor.fetchall()
    return val[0][0]

def addRide(email, date, seats, price, luggageDesc, src, dst, carNum=None, enrouteLoc=None):
    global connection, cursor
    time = datetime.datetime.now()
    rno = (time.second * time.microsecond) % 1999
    
    
    
    cno = getCNO(email)
    print(cno)
    # rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno)
    sql = "insert into rides values (?,?,?,?,?,?,?,?,?)"
    cursor.execute(sql, (rno, price, date, seats, luggageDesc, src, dst, email, cno))    
    return
    

def searchLogin(email, pwd):
    global connection, cursor
    sql = "select count(*) from members where email=? and pwd=?"
    cursor.execute(sql, (email,pwd))
    val = cursor.fetchall()
    return val[0][0] == 1
    

def registerUser(email, pwd, phone, name):
    global connection, cursor
    failed = False
    email.lower()
    atSymbol = 0
    dot = 0
    
    # Checking for correct syntax in email
    for letter in email:
        if letter == "@":
            atSymbol += 1
        if letter == "." and atSymbol == 1:
            dot += 1
    if atSymbol != 1 or dot < 1:
        failed = True
    if failed:
        # First zero - register fail
        # Second digit - non-proper format for email
        return (0,1)
    
    # Checking for correct phone number syntax
    if not phone[0:2].isdigit() or not phone[4:6].isdigit() or not phone[8:11].isdigit():
        # First zero - register fail
        # Second digit - non-proper format for phone number
        print(phone)
        return (0,2)
    if not phone[3] == "-" or not phone[7] == "-":
        # See above
        print(phone)
        return (0,2)
    
    sql = "select count(*) from members where email=?"
    cursor.execute(sql, (email,))
    val = cursor.fetchall()
    if val[0][0] == 1:
        # first zero - register fail
        # second zero - non-unique email
        return (0, 0)
    else:
        sql = "insert into members (email, name, phone, pwd) values (?,?,?,?);"
        cursor.execute(sql, (email,name,phone,pwd,))
        return (1,None)


def main():
    global connection, cursor

    path = "./register.db"
    connect(path)
    ind.drop_tables(connection, cursor)
    ind.define_tables(connection, cursor)
    ind.insert_data(connection, cursor)
    
    return (connection, cursor)


if __name__ == "__main__":
    main()

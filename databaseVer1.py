# this is the database for the program.
# all tables are created.
# the data used for testing are originally prepared by Tanner Chell, tchell@ualberta.ca.

import sqlite3
import time
import datetime as td

connection = None
cursor = None


def connect(path):
    global connection, cursor

    connection = sqlite3.connect('./testdatadb.db')
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return


def drop_tables():
    global connection, cursor

    drop_requests = "DROP TABLE IF EXISTS requests; "
    drop_enroute = "DROP TABLE IF EXISTS enroute; "
    drop_bookings = "DROP TABLE IF EXISTS bookings; "
    drop_rides = "DROP TABLE IF EXISTS rides; "
    drop_locations = "DROP TABLE IF EXISTS locations;"
    drop_cars = "DROP TABLE IF EXISTS cars; "
    drop_members = "DROP TABLE IF EXISTS members; "
    drop_inbox = "DROP TABLE IF EXISTS inbox; "

    cursor.execute(drop_requests)
    cursor.execute(drop_enroute)
    cursor.execute(drop_bookings)
    cursor.execute(drop_inbox)
    cursor.execute(drop_rides)
    cursor.execute(drop_cars)
    cursor.execute(drop_members)
    cursor.execute(drop_locations)


def define_tables():
    global connection, cursor

    cursor.executescript('''create table members (
  email		char(15),
  name		char(20),
  phone		char(12),
  pwd		char(6),
  primary key (email)
);
create table cars (
  cno		int,
  make		char(12),
  model		char(12),
  year		int,
  seats		int,
  owner		char(15),
  primary key (cno),
  foreign key (owner) references members
);
create table locations (
  lcode		char(5),
  city		char(16),
  prov		char(16),
  address	char(16),
  primary key (lcode)
);
create table rides (
  rno		integer primary key,
  price		int,
  rdate		date,
  seats		int,
  lugDesc	char(10),
  src		char(5),
  dst		char(5),
  driver	char(15),
  cno		int,
  foreign key (src) references locations,
  foreign key (dst) references locations,
  foreign key (driver) references members,
  foreign key (cno) references cars
);
create table bookings (
  bno		int,
  email		char(15),
  rno		int,
  cost		int,
  seats		int,
  pickup	char(5),
  dropoff	char(5),
  primary key (bno),
  foreign key (email) references members,
  foreign key (rno) references rides,
  foreign key (pickup) references locations,
  foreign key (dropoff) references locations
);
create table enroute (
  rno		int,
  lcode		char(5),
  primary key (rno,lcode),
  foreign key (rno) references rides,  
  foreign key (lcode) references locations
);  
create table requests (
  rid		integer primary key,
  email		char(15),
  rdate		date,
  pickup	char(5),
  dropoff	char(5),
  amount	int,
  foreign key (email) references members,
  foreign key (pickup) references locations,
  foreign key (dropoff) references locations
);
create table inbox (
  email		char(15),
  msgTimestamp	date,
  sender	char(15),
  content	text,
  rno		int,
  seen		char(1),
  primary key (email, msgTimestamp),
  foreign key (email) references members,
  foreign key (sender) references members,
  foreign key (rno) references rides
);''')
    connection.commit()

    return


def insert_data():
    global connection, cursor

    insert_members = '''
                        INSERT INTO members(email, name, phone, pwd) VALUES
                            ('jane_doe@abc.ca', 'Jane Maria-Ann Doe', '780-342-7584', 'jpass'),
                            ('bob@123.ca', 'Bob Williams', '780-342-2834', 'bpass'),
                            ('maria@xyz.org', 'Maria Calzone', '780-382-3847', 'mpass'),
                            ('the99@oil.com', 'Wayne Gretzky', '780-382-4382', 'tpass'),
                            ('connor@oil.com', 'Connor Mcdavid', '587-839-2838', 'cpass'),
                            ('don@mayor.yeg', 'Don Iveson', '780-382-8239', 'dpass'),
                            ('darryl@oil.com', 'Darryl Katz', '604-238-2380', 'dpass'),
                            ('reilly@esks.org', 'Mike Reilly', '780-389-8928', 'rpass'),
                            ('mess@marky.mark', 'Mark Messier', '516-382-8939', 'mpass'),
                            ('mal@serenity.ca', 'Nathan Fillion', '780-389-2899', 'mpass'),
                            ('kd@lang.ca', 'K. D. Lang', '874-384-3890', 'kpass'),
                            ('nellie@five.gov', 'Nellie McClung', '389-930-2839', 'npass'),
                            ('marty@mc.fly', 'Micheal J. Fox', '780-382-3899', 'mpass'),
                            ('cadence@rap.fm', 'Roland Pemberton', '780-938-2738', 'cpass'),
                            ('john@acorn.nut', 'John Acorn', '780-389-8392', 'jpass');
                        '''

    insert_cars = '''
                            INSERT INTO cars(cno, make, model, year, seats, owner) VALUES
                                 (1, 'Honda', 'Civic', 2010, 4, 'jane_doe@abc.ca'),
                                 (2, 'Ford', 'E-350', 2012, 15, 'bob@123.ca'),
                                 (3, 'Toyota', 'Rav-4', 2016, 4, 'don@mayor.yeg'),
                                 (4, 'Subaru', 'Forester', 2017, 4, 'reilly@esks.org'),
                                 (5, 'Ford', 'F-150', 2018, 4, 'connor@oil.com'),
                                 (6, 'Ram', '2500', 2017, 4, 'mess@marky.mark'),
                                 (7, 'Toyota', 'Matrix', 2007, 4, 'maria@xyz.org'),
                                 (8, 'Dodge', 'Caravan', 2013, 6, 'mess@marky.mark'),
                                 (9, 'Ford', 'Flex', 2011, 4, 'maria@xyz.org'),
                                 (10, 'Volkswagon', 'Vanagon', 1974, 5, 'the99@oil.com'),
                                 (11, 'Toyota', 'Sienna', 2012, 6, 'john@acorn.nut'),
                                 (12, 'Honda', 'Accord', 2010, 4, 'john@acorn.nut'),
                                 (13, 'Jeep', 'Wrangler', 2007, 2, 'cadence@rap.fm');
                            '''
    insert_locations = '''
                        INSERT INTO locations(lcode, city, prov, address) VALUES
                            ('cntr1', 'Edmonton', 'Alberta', 'Rogers Place'),
                            ('cntr2', 'Edmonton', 'Alberta', 'City Hall'),
                            ('sth1', 'Edmonton', 'Alberta', 'Southgate'),
                            ('west1', 'Edmonton', 'Alberta', 'West Ed Mall'),
                            ('cntr3', 'Edmonton', 'Alberta', 'Tyrell Museum'),
                            ('cntr4', 'Edmonton', 'Alberta', 'Citadel Theater'),
                            ('cntr5', 'Edmonton', 'Alberta', 'Shaw Center'),
                            ('sth2', 'Edmonton', 'Alberta', 'Black Dog'),
                            ('sth3', 'Edmonton', 'Alberta', 'The Rec Room'),
                            ('sth4', 'Edmonton', 'Alberta', 'MEC South'),
                            ('nrth1', 'Edmonton', 'Alberta', 'MEC North'),
                            ('nrth2', 'Edmonton', 'Alberta', 'Rexall Place'),
                            ('nrth3', 'Edmonton', 'Alberta', 'Commonwealth'),
                            ('nrth4', 'Edmonton', 'Alberta', 'Northlands'),
                            ('yyc1', 'Calgary', 'Alberta', 'Saddledome'),
                            ('yyc2', 'Calgary', 'Alberta', 'McMahon Stadium'),
                            ('yyc3', 'Calgary', 'Alberta', 'Calgary Tower'),
                            ('van1', 'Vancouver', 'British Columbia', 'BC Place'),
                            ('van2', 'Vancouver', 'British Columbia', 'Rogers Arena'),
                            ('sk1', 'Regina', 'Saskatchewan', 'Mosaic Field'),
                            ('sk2', 'Saskatoon', 'Saskatchewan', 'Wanuskewin'),
                            ('ab1', 'Jasper', 'Alberta', 'Jasper Park Lodge');
                        '''
    insert_rides = '''
                        INSERT INTO rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno) VALUES
                            (1, 50, '2018-11-01', 4, 'Large Bag', 'cntr1', 'yyc1', 'the99@oil.com', 10),
                            (2, 50, '2018-11-05', 4, 'Large Bag', 'yyc1', 'cntr2', 'the99@oil.com', 10),
                            (3, 50, '2018-11-30', 4, 'Medium Bag', 'cntr1', 'yyc1', 'mess@marky.mark', 8),
                            (4, 30, '2018-11-17', 15, '5 large bags', 'nrth1', 'yyc2', 'bob@123.ca', 2),
                            (5, 50, '2018-11-23', 3, 'Backpack', 'cntr2', 'yyc3', 'maria@xyz.org', 7),
                            (6, 10, '2018-07-23', 4, 'Medium Bag', 'west1', 'sth4', 'don@mayor.yeg', 3),
                            (7, 10, '2018-09-30', 4, 'Medium Bag', 'cntr2', 'cntr3', 'reilly@esks.org', 4),
                            (8, 10, '2018-10-11', 4, 'Medium Bag', 'nrth1', 'sth2', 'connor@oil.com', 4),
                            (9, 10, '2018-10-12', 4, 'Medium Bag', 'cntr5', 'sth3', 'jane_doe@abc.ca', 1),
                            (10, 10, '2018-04-26', 4, 'Medium Bag', 'cntr4', 'cntr2', 'bob@123.ca', 2),
                            (11, 100, '2018-08-08', 4, 'Medium Bag', 'cntr1', 'van1', 'mess@marky.mark', 6),
                            (12, 100, '2018-05-13', 2, 'Medium Bag', 'sk1', 'van2', 'bob@123.ca', 2),
                            (13, 75, '2018-06-11', 3, 'Large Bag', 'yyc1', 'sk2', 'the99@oil.com', 10),
                            (14, 10, '2018-10-13', 4, 'Large Bag', 'sth4', 'yyc1', 'reilly@esks.org', 4),
                            (15, 15, '2018-10-05', 5, 'Medium Bag', 'nrth4', 'yyc1', 'the99@oil.com', 10),
                            (16, 75, '2018-10-03', 2, 'Small Bag', 'yyc3', 'sk2', 'connor@oil.com', 5),
                            (17, 150, '2018-10-11', 3, 'Medium Bag', 'sk2', 'van1', 'jane_doe@abc.ca', 1),
                            (18, 10, '2018-10-23', 3, 'Large Bag', 'nrth3', 'yyc1', 'don@mayor.yeg', 3),
                            (19, 10, '2015-04-22', 4, 'Small Bag', 'cntr1', 'cntr2', 'bob@123.ca', 2),
                            (20, 50, '2018-12-11', 1, 'Large Bag', 'cntr2', 'yyc2', 'the99@oil.com', 10),
                            (21, 50, '2018-12-12', 1, 'Large Bag', 'cntr2', 'yyc3', 'the99@oil.com', 10),
                            (22, 10, '2018-09-13', 1, 'Large Bag', 'cntr2', 'cntr4', 'the99@oil.com', 10),
                            (23, 10, '2018-09-14', 1, 'Large Bag', 'cntr2', 'cntr5', 'the99@oil.com', 10),
                            (24, 10, '2018-09-15', 1, 'Large Bag', 'cntr2', 'sth1', 'the99@oil.com', 10),
                            (25, 10, '2018-09-16', 1, 'Large Bag', 'cntr2', 'sth2', 'the99@oil.com', 10),
                            (26, 50, '2018-12-06', 1, 'Large Bag', 'cntr2', 'yyc1', 'bob@123.ca', 2),
                            (27, 53, '2018-09-07', 2, 'Large Bag', 'cntr2', 'yyc3', 'bob@123.ca', 2),
                            (28, 10, '2018-09-08', 1, 'Large Bag', 'cntr2', 'cntr4', 'bob@123.ca', 2),
                            (29, 10, '2018-09-09', 1, 'Large Bag', 'cntr2', 'cntr5', 'bob@123.ca', 2),
                            (30, 10, '2018-09-10', 1, 'Large Bag', 'cntr2', 'sth1', 'bob@123.ca', 2),
                            (31, 10, '2018-09-11', 1, 'Large Bag', 'cntr2', 'sth2', 'bob@123.ca', 2),
                            (32, 10, '2018-09-12', 1, 'Large Bag', 'cntr2', 'sth3', 'bob@123.ca', 2),
                            (33, 10, '2018-09-01', 1, 'Large Bag', 'cntr2', 'cntr1', 'don@mayor.yeg', 3),
                            (34, 10, '2018-09-02', 1, 'Large Bag', 'cntr2', 'nrth1', 'don@mayor.yeg', 3),
                            (35, 10, '2018-09-03', 1, 'Large Bag', 'cntr2', 'cntr3', 'don@mayor.yeg', 3),
                            (36, 10, '2018-09-04', 1, 'Large Bag', 'cntr2', 'cntr4', 'don@mayor.yeg', 3),
                            (37, 10, '2018-09-05', 1, 'Large Bag', 'cntr2', 'sth1', 'don@mayor.yeg', 3),
                            (38, 10, '2018-09-06', 1, 'Large Bag', 'cntr2', 'sth2', 'don@mayor.yeg', 3),
                            (39, 10, '2018-09-07', 1, 'Large Bag', 'cntr2', 'sth3', 'don@mayor.yeg', 3),
                            (40, 50, '2018-09-08', 1, 'Large Bag', 'cntr2', 'yyc1', 'don@mayor.yeg', 3),
                            (41, 100, '2018-11-05', 2, 'Large Bag', 'cntr1', 'sk1', 'don@mayor.yeg', 3),
                            (42, 150, '2018-11-05', 2, 'Large Bag', 'van2', 'nrth2', 'don@mayor.yeg', 3),
                            (43, 10, '2018-10-14', 4, 'Large Bag', 'sth4', 'yyc1', 'jane_doe@abc.ca', 1);
                    '''
    insert_bookings = '''
                        INSERT INTO bookings(bno, email, rno, cost, seats, pickup, dropoff) VALUES
                            (1, 'connor@oil.com', 1, null, 1, null, null),
                            (2, 'connor@oil.com', 2, null, 1, null, null),
                            (3, 'kd@lang.ca', 3, 45, 1, 'cntr2', null),
                            (4, 'reilly@esks.org', 4, 30, 13, null, null),
                            (5, 'don@mayor.yeg', 5, 50, 1, 'cntr2', 'yyc3'),
                            (6, 'marty@mc.fly', 18, null, 3, null, null),
                            (7, 'darryl@oil.com', 20, null, 1, null, null),
                            (8, 'john@acorn.nut', 26, null, 1, null, null),
                            (9, 'cadence@rap.fm', 27, null, 1, null, null),
                            (10, 'connor@oil.com', 5, 45, 1, null, null),
                            (11, 'mal@serenity.ca', 41, null, 1, null, null),
                            (12, 'nellie@five.gov', 42, null, 1, null, null);
                        '''
    insert_enroute = '''
                        INSERT INTO enroute(rno, lcode) VALUES
                            (12, 'yyc1'),
                            (16, 'sk1'),
                            (17, 'cntr2');
                        '''
    insert_requests = '''
                        INSERT INTO requests(rid, email, rdate, pickup, dropoff, amount) VALUES
                            (1, 'darryl@oil.com', '2018-07-23', 'nrth1', 'cntr1', 10),
                            (2, 'nellie@five.gov', '2018-07-22', 'west1', 'sth4', 10),
                            (3, 'mal@serenity.ca', '2018-10-11', 'nrth2', 'sth3', 10),
                            (4, 'don@mayor.yeg', '2018-10-11', 'nrth2', 'sth3', 10),
                            (5, 'the99@oil.com', '2018-10-11', 'nrth1', 'ab1', 10),
                            (6, 'marty@mc.fly', '2018-10-11', 'sk1', 'sth3', 10),
                            (7, 'mess@marky.mark', '2018-10-11', 'nrth2', 'sth3', 1),
                            (8, 'mess@marky.mark', '2018-10-11', 'nrth2', 'sth3', 100),
                            (9, 'jane_doe@abc.ca', '2018-04-26', 'cntr3', 'cntr2', 10);
                        '''
    insert_inbox = '''
                        INSERT INTO inbox(email, msgTimestamp, sender, content, rno, seen) VALUES
                            ('don@mayor.yeg', '2018-08-04', 'darryl@oil.com', 'message content is here', 36, 'n'),
                            ('jane_doe@abc.ca', '2018-09-04', 'darryl@oil.com', '2nd message content is here', 43, 'n'),
                            ('don@mayor.yeg', '2018-010-04', 'darryl@oil.com', '3rd message content is here', 42, 'n');
                        '''


    cursor.execute(insert_members)
    cursor.execute(insert_cars)
    cursor.execute(insert_locations)
    cursor.execute(insert_rides)
    cursor.execute(insert_bookings)
    cursor.execute(insert_enroute)
    cursor.execute(insert_requests)
    cursor.execute(insert_inbox)
    connection.commit()
    return

# System Function 1 some finished
def offer(price, rdate, seats, lugDesc, src, dst, driver, cno):
    # The member should be able to offer rides by providing a date, the number of seats offered, the price per seat, a luggage description, a source location, and a destination location. 
    global connection, cursor
    sql_2 = ''' INSERT INTO rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno) VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?) ''' 
    data = (price, rdate, seats, lugDesc, src, dst, driver, cno)
    cursor.execute(sql,data)
    connection.commit()  
    return
        
        
def add_enroute(rno,lcode):
    global connection, cursor
    sql_2 = ''' INSERT INTO enroute(rno, lcode) VALUES (?, ?) ''' 
    data = (rno,lcode)
    cursor.execute(sql,data)
    connection.commit()          
    return

# System Function 2 not finished
def search_rides(key1,key2,key3):
    global connection, cursor
    
    sql = "SELECT * FROM rides WHERE rides.src IN (SELECT lcode FROM locations WHERE locations.city = ?) OR rides.dst = ? LIMIT 5"    

# System Function 3
def bookings(email):
    # The member should be able to list all bookings on rides s/he offers
    global connection, cursor
    sql = "SELECT * FROM bookings WHERE bookings.email = ?"
    cursor.execute(sql, (email,))
    booking = cursor.fetchall()
    return booking
    
def b_cancel(email,rid):
    # The member should be able to cancel any bookings on rides s/he offers
    global connection, cursor

    data = (email,rid)
    cursor.execute('DELETE FROM bookings WHERE bookings.email ? AND rid = ?;', data)
    connection.commit()
    return

# System Function 4
def request(email,date,pickup,dropoff,amount):
    # Post ride requests.The member should be able to post a ride request by providing a date, a pick up location code, a drop off location code, and the amount willing to pay per seat. 
    # The request rid is set by your system to a unique number and the email is set to the email address of the member.
    global connection, cursor
    sql = ''' INSERT INTO requests VALUES (null, ?, ?, ?, ?, ?) '''
    #cursor.execute("SELECT email FROM members WHERE members.name = ?",(name,))
    #email = str(cursor.fetchone()).replace('"','').replace('"','')
    data = (email,date,pickup,dropoff,amount)
    cursor.execute(sql,data)
    connection.commit()
    return    

# System Function 5
def search(email):
    # The member should be able to see all his/her ride requests
    # This function search the database using the member's name provided.
    global connection, cursor
    
    sql = "SELECT * FROM requests WHERE requests.email = ?"
    cursor.execute(sql, (email,))
    req_n = cursor.fetchall()
    return req_n
    
def search_pickup(name):
    # Also the member should be able to provide a location code or a city
    # and see a listing of all requests with a pickup location matching the location code or the city entered.
    # If there are more than 5 matches, at most 5 matches will be shown at a time.
    global connection, cursor
    
    sql_1 = "SELECT * FROM requests WHERE requests.pickup IN (SELECT lcode FROM locations WHERE locations.city = ?) OR requests.pickup = ? LIMIT 5"
    cursor.execute(sql_1, (name,name))
    req_l = cursor.fetchall()
    return req_l    
    
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


def getCNO(email):
    global connection, cursor
    sql = "select cno from cars where owner=?"
    cursor.execute(sql, (email,))
    val = cursor.fetchall()
    return val[0][0]

def uniqueID(table, IDtype):
    tm = td.datetime.now()
    ID = (tm.second * tm.microsecond) % 1999
    sql = "select count(*) from {} where {}=?".format(table,IDtype)
    cursor.execute(sql, (ID,))
    val = cursor.fetchall()
    if val[0][0] == 0:
        print("ID is {} and type is {}".format(ID, type(ID)))
        return ID
    else:
        return uniqueID(table, IDtype)

def addRide(email, date, seats, price, luggageDesc, src, dst, carNum=None, enrouteLoc=None):
    global connection, cursor
    rno = uniqueID("rides", "rno")
    cno = getCNO(email)
    # rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno)
    sql = "insert into rides values (?,?,?,?,?,?,?,?,?)"
    cursor.execute(sql, (rno, price, date, seats, luggageDesc, src, dst, email, cno))    
    return    
            
def test_data():
    # test to see if each table was succesfully created and if each data was successfull stored into the tables
    cursor.execute("SELECT * FROM members WHERE members.pwd = 'dpass';")
    row1 = cursor.fetchall()
  
    cursor.execute("SELECT * FROM cars WHERE cars.cno = 9;")
    row2 = cursor.fetchall()
    
    cursor.execute("SELECT * FROM locations WHERE locations.city = 'Calgary';")
    row3 = cursor.fetchall()  
    
    cursor.execute("SELECT * FROM rides WHERE rides.price = 50;")
    row4 = cursor.fetchall()   
    
    cursor.execute("SELECT * FROM bookings WHERE bookings.rno = 5;")
    row5 = cursor.fetchall()
    
    cursor.execute("SELECT * FROM enroute WHERE enroute.rno = 12;")
    row6 = cursor.fetchall()
    
    cursor.execute("SELECT * FROM requests WHERE requests.dropoff = 'bntr2';")
    row7 = cursor.fetchall()
    
    cursor.execute("SELECT * FROM inbox WHERE inbox.rno = 36;")
    row8 = cursor.fetchall() 
    
    #print(row1)
    #print(row2)
    #print(row3)
    #print(row4)
    #print(row5)
    #print(row6)
    #print(row7)
    #print(row8)    
    
    # test if it is able to post a ride request
    request('jane_doe@abc.ca','2018-10-21', 'nrth2', 'sth3', 10)
    cursor.execute("SELECT * FROM requests WHERE requests.rdate = '2018-10-21';")
    print(cursor.fetchall())
    
    # test if it is able to list all bookings on rides the member offers
    print(bookings('connor@oil.com'))

    # test if the member is able to see all his/her ride requests
    name_1 = 'mess@marky.mark'
    print(search(name_1))
    
    # test if the member is able to provide a location code or a city
    # and see a listing of all requests with a pickup location matching the location code or the city entered.    
    name_2 = 'Edmonton'
    print(search_pickup(name_2))
    name_3 = 'nrth2'
    print(search_pickup(name_3))    
    
def main():
    global connection, cursor

    path = "./register.db"
    connect(path)
    drop_tables()
    define_tables()
    insert_data()
    
    # test_data()
    
    # connection.commit()
    # connection.close()
    return


if __name__ == "__main__":
    main()

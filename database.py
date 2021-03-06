"""
The following information is CONFIDENTIAL. If you are NOT an admin, and if you are seeing this,
e-mail ssb2189@columbia.edu
"""
import psycopg2.extras


# Final Database - Storing patient records
DBNAME = 'd5nq5opbhumdlr'
USER = 'kznrowmqsnyetc'
PASSWORD = 'RRjBYCRf8crRhzrpHmk-HcPvnb'
HOST = 'ec2-54-163-253-94.compute-1.amazonaws.com'
PORT = '5432'

# Temporary Database - Testing
# DBNAME = 'd2i3vppivu81og'
# USER = 'cmukqvlzfirmnq'
# PASSWORD = 'Dc2dad3DKM8fFovofn8otZ099p'
# HOST = 'ec2-54-235-179-112.compute-1.amazonaws.com'
# PORT = '5432'
print "yo"
#This connects to the database
try:
    print "connecting to db"
    conn = psycopg2.connect("\
    dbname = '" + DBNAME + "'       \
    user = '" + USER + "'           \
    password = '" + PASSWORD + "'   \
    host = '" + HOST + "'           \
    port = '" + PORT + "'           \
                   ")
    conn.autocommit = True
    print "connected to db"
except:
    print("Can't connect to the database :/ Check Wi-Fi.")

print "wassup"
# Defining the cursor
try:
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
except:
    print("Error while importing psycopgy2")

print "shikhar"
# This adds the pi to the records_pi table
def add_pi(pi_code) :
    print "adding pi"	
    # this gets the RaspberryPi's MAC address
    try:
        str = open('/sys/class/net/eth0/address').read()
    except:
        str = "00:00:00:00:00:00"
    address = str[0:17]

    cur.execute("""SELECT records_pi.id FROM records_pi WHERE records_pi.code = (%s) """, (pi_code,))
    rows = cur.fetchall()

    if len(rows) == 0 :
        # Inserts the pi code and address into the records_pi table
        try:
            cur.execute("""INSERT INTO records_pi(code,address) VALUES(%s, %s)""", (pi_code, address))
        except :
            print("Error while inserting into records_pi")
    else :
        print("Code already exists.")



# This adds data to that particular pi
# def add_data(time,vol,last,new,cumul,status,pi_code) :
print "nad"
def add_data(all_data):
    print "adding data"
    time,vol,last,new, cumul, status, pi_code = all_data

    time = round(float(time), 1) - 3600
    vol = round(float(str(vol)),1)
    last = round(float(str(last)),1)
    new = round(float(str(new)),1)
    cumul = round(float(str(cumul)),1)
    status = str(status)
    pi_code = str(pi_code)


    # gets the pi_id from the records_pi table after matching the code
    try:
        cur.execute("""SELECT records_pi.id FROM records_pi WHERE records_pi.code = (%s) """,(pi_code,))
        rows = cur.fetchall()
        pi_id = str(rows[0][0])
    except:
        print("The Pi with that code does not exist")

    # Inserts the row into the data table
    try:
        cur.execute("""INSERT INTO records_data(date_time,raw_vol, las_vol,new_vol, cum_vol, status, pi_id) VALUES(%s, %s, %s, %s, %s, %s, %s)""", (time,vol,last,new,cumul,status,pi_id))
        all_data.pop(0)
    except :
        print("Error while inserting into records_data")









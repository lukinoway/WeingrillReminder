########################################
# - Title:   Weingrill DB Connector
# - Author:  Lukas Pichler
# - Date:    2016-10-13
########################################

import psycopg2

conn = None

def connect():
    global conn
    if not conn:
        conn = psycopg2.connect("dbname='weingrill' user='weingrill' host='localhost' password='weingrill'")
        print "connected to DB"


def import_data(date, starter, main, dessert):
    if conn:
        stmt = """INSERT INTO menuplan(date_info, starter, main, dessert, creation_dt) VALUES('"""+date+"""', '"""+starter+"""', '"""+main+"""', '"""+dessert+"""', NOW())"""
        try:
            cur = conn.cursor()
            cur.execute(stmt)

            conn.commit()

        except psycopg2.Error as e:
            print "error occured while importing data"
            print e.pgcode
            print e.pgerror
    else:
        print "seems that there is no connection"


def close():
    if conn:
        print "close DB connection"
        conn.close()
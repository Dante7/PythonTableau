#!/usr/bin/python
import MySQLdb
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import MySQLdb.cursors

def getFields(cur):
	campos = []
	for f in cur.description:
		campos.append(f[0])
	print campos


db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="Rosario07", # your password
                      db="sakila") 
                      #cursorclass=ySQLdb.cursors.DictCursor) # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM film")

tbl = cur.fetchall()

df = DataFrame(getFields(cur),tbl)

print df

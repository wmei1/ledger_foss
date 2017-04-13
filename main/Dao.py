import sqlite3
import sys
import os
import fileinput
import pickle
import signal
from category import *


class Dao:

	dbFile=None
	dbFlag=False
	conn = None
	cur = None

	def create_db(self):
	cur.execute('''CREATE TABLE LEDGER (
				ID INT PRIMARY KEY NOT NULL,
				NAME CHAR(20),
				EXC REAL,
				DATE DATE,
				CATE CHAR(50),
				DESC CHAR(50))''')

	def insert_row(self,csv):
		cur.execute("INSERT INTO LEDGER VALUES (?,?,?,?,?,?)", csv)

	def delete_row(self,_id):
		cur.execute("DELETE FROM LEDGER WHERE ID=?",(_id,))

	def update_row(self, csv):
		cur.execute('''
					UPDATE LEDGER SET NAME =?,
					EXC=?,
					DATE=?,
					CATE=?,
					DESC=?,
					WHERE ID=?''', csv)

	def print_db(self):
		cursor = cur.execute("SELECT * FROM LEDGER")
		print("ID|NAME|MONEY|DATE|CATEGORY|DESC")
		for row in cursor:
			print(row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5])
		#print(cur.fetchall())

	def startConnection():
		dbFlag=False
		try:
			if(not os.path.isfile('./ledger.db')):
				dbFile = open('ledger.db', 'w+')
				dbFile.close()
				dbFlag = True
			conn = sqlite3.connection()
			cur=conn.cursor()
		except sqlite3.Error as er:
			print('er:',er.message)
		except IOError:
			print('No file found')

		return dbFlag

	def closeConnection():
		try:
			conn.close()
			dbFile.close()
			print('File and Connection Successfully Close')
		except IOError: 
			print("No file found")
		except sqlite3.Error as er:
			print('er:', er.message())



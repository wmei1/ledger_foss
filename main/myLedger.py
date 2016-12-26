
#myLedger

import csv
import sqlite3
import sys
import os
import fileinput

id_num = 0
class myLedger:
	
	def init_db(self, cur):
		#Cols: Id, Name, Money, Date, Category, Descrip, Reconcile,
		cur.execute('''CREATE TABLE ledger (
		Id INT PRIMARY KEY NOT NULL,
		Name CHAR(50),
		Exc REAL,
		Date CHAR(50))''')

	def insert_db(self, cur, csv):
		cur.execute("INSERT INTO ledger VALUES (?,?,?,?)", csv)

	def delete_db(self, cur, _id):
		cur.execute("DELETE from ledger where Id=?;", (_id,))
		
	def update_db(self, cur, csv):
		cur.execute ('''
			UPDATE ledger 
			SET Name = ?,
			Exc = ?,
			Date = ?
			WHERE Id=?''', csv)

	def select_db(self, cur):
		cursor = cur.execute("SELECT * FROM ledger")
		for row in cursor:
			print("ID = ", row[0])
			print("NAME = ", row[1])
			print("Money = ", row[2])
			print("Date = ", row[3], "\n")
		#print(cur.fetchall())

	def program(self, db, cur):
		global id_num
		while True:
			uinput = input("Enter an command, Enter h to show a list of commands: ")

			if uinput is "h":
				print('''h - help text \ns - prints out the ledger \ni - insert a new row \nd - delete a row \nu - update a row \nq - quit program \n''')

			if uinput is "s":
				self.select_db(cur)
					
			if uinput is "i":
				name = input("Enter the name:")
				exc = input("Enter Exchange amt:")
				date = input("enter the date:")
				csv = (id_num,name,exc,date)
				id_num +=1
				#print(csv)
				self.insert_db(cur, csv)
				db.commit()

			if uinput is "d":
				_id = int(input("Enter the id you wish to delete"))
				self.delete_db(cur, _id)
				db.commit()

			if uinput is "u":
				_id = int(input("Enter the id you wish to update"))
				name = input("Enter the name:")
				exc = input("Enter Exchange amt:")
				date = input("enter the date:")
				csv = (name,exc,date, _id)
				self.update_db(cur, csv)
				db.commit()

			if uinput is "q":
				return False


if __name__ == "__main__":

	idCountFile = None
	if (os.path.isfile('./id_count.txt')):
		with open('id_count.txt', 'r+') as idCountFile:
			idCount = idCountFile.readline()
			#print(idCount)	used for debeugging
			id_num = int(idCount)

	dbFlag = False
	dbFile = None
	if (not os.path.isfile('./ledger.db')):
		dbFile = open('ledger.db', 'w+')
		dbFlag = True

	db = sqlite3.connect('ledger.db')
	cur = db.cursor()
	led = myLedger()

	if(dbFlag is True):
		led.init_db(cur)

	db.commit()
	led.program(db, cur)

	with open('id_count.txt', 'w') as idCountFile:
		idCountFile.write(str(id_num))

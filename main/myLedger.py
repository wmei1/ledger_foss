
#myLedger

import csv
import sqlite3
import sys

id_num = 0
class myLedger:
	

	def init_db(self, cur):
		cur.execute('''CREATE TABLE ledger (
		Id INT PRIMARY KEY	NOT NULL,
		Name CHAR(50),
		Exc REAL,
		Date CHAR(50))''')
#Id, Name, Money, Date, Category, Descrip, Reconcile,
	def insert_db(self, cur, csv):
		cur.execute("INSERT INTO ledger VALUES (?,?,?,?)", csv)

	def delete_db(self, cur, _id):
		return
		
	def update_db(self, cur, _id):
		return

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
				delete_db(cur, _id)
				db.commit()

			if uinput is "u":
				_id = int(input("Enter the id you wish to update"))
				update_db(cur, _id)
				db.commit()

			if uinput is "q":
				return False


if __name__ == "__main__":
	db = sqlite3.connect(':memory:')
	temp = 1
	cur = db.cursor()
	led = myLedger()
	led.init_db(cur)
	db.commit()
	led.program(db, cur)




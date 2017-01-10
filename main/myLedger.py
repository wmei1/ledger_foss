
#myLedger

import csv
import sqlite3
import sys
import os
import fileinput
import pickle

id_num = 0
CATE = ['Bank', 'Entertainment', 'Food', 'Other'] 
categories = ['Bank', 'Entertainment', 'Food','Other'] 
class myLedger:
	
	def init_db(self, cur):
		#Cols: Id, Name, Money, Date, Category, Descrip, Reconcile,
		cur.execute('''CREATE TABLE ledger (
		Id INT PRIMARY KEY NOT NULL,
		Name CHAR(50),
		Exc REAL,
		Date CHAR(50),
		Cat CHAR(50),
		Desc CHAR(50))''')

	def insert_db(self, cur, csv):
		cur.execute("INSERT INTO ledger VALUES (?,?,?,?,?,?)", csv)

	def delete_db(self, cur, _id):
		cur.execute("DELETE from ledger where Id=?;", (_id,))
		
	def update_db(self, cur, csv):
		cur.execute ('''
			UPDATE ledger 
			SET Name = ?,
			Exc = ?,
			Date = ?,
			Cat = ?,
			Desc = ?,
			WHERE Id=?''', csv)

	def select_db(self, cur):
		cursor = cur.execute("SELECT * FROM ledger")
		print("ID|NAME|Money|Date|Category|Desc	")
		for row in cursor:
			print(row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5])
		#print(cur.fetchall())

	def program(self, db, cur):
		global id_num, categories,CATE
		while True:
			uinput = input("Enter an command, Enter h to show a list of commands: ")

			if uinput is "h":
				print(' h - help text\n', 
				's - prints out the ledger\n', 
				'i - insert a new row\n', 
				'd - delete a row\n', 
				'u - update a row\n',
				'c - category options' 
				'q - quit program\n')

			if uinput is "s":
				self.select_db(cur)
					
			if uinput is "i":
				name = input("Enter the name:")
				exc = input("Enter Exchange amt:")
				date = input("enter the date:")
				#prints out categories to choose from
				for index in range(len(categories)):
					print(index,'.',categories[index])
				#checks if input is integer.
				cat = None
				while cat is None:
					cate_in = input("Choose a category from the list or enter your own:")
					try:
						val = int(cate_in)
						if val < len(categories):
							cat = categories[val]
						else:
							print("# entered is out of range")
					except ValueError:
						cat = cate_in
						categories.append(cat)
						
				
				desc = input("enter a desc:")
				csv = (id_num,name,exc,date,cat,desc)
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
				cat = input("enter a category:")
				desc = input("enter a desc:")
				csv = (name,exc,date,cat,desc, _id)
				self.update_db(cur, csv)
				db.commit()

			if uinput is "c":
				print(' r - restore to default\n',
				'd - delete a category\n',
				'm - modify a category\n',
				'p - print out the category')
				uinput = input("")
				if uinput is "r":
					categories = CATE
					print("categories are restored to default")
				if uinput is "m":
					for index in range(len(categories)):
						print(index,'.',categories[index])
					mod = input("Enter the category ID")
					temp_category = input("Enter the new name of the category")
					categories[mod] = temp_category
				if uinput is "d":
					for index in range(len(categories)):
						print(index,'.',categories[index])
					mod = input("Enter the ID you want to delete")
					del categories[mod]	
				if uinput is "p":
					for index in range(len(categories)):
						print(index,'.',categories[index])

			if uinput is "q":
				return False


if __name__ == "__main__":

	idCountFile = None
	if (os.path.isfile('./id_count.txt')):
		with open('id_count.txt', 'r+') as idCountFile:
			idCount = idCountFile.readline()
			print(idCount)	#used for debeugging
			id_num = int(idCount)
	if (os.path.isfile('./cate.p')):
		categories = pickle.load( open("cate.p", "rb"))
		

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
	pickle.dump(categories,open('cate.p',"wb"))
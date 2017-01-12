	
#Helper Class for all categories related functions
class category:
	CATE = ['Bank', 'Entertainment', 'Food', 'Other'] 
	categories = ['Bank', 'Entertainment', 'Food','Other'] 
	def print_categories():
		cate = category.categories
		for index in range(len(cate)):
			print(index, '.', cate[index])
	
	def main_category(self):
		#global categories
		cate = category.categories
		print(' r - restore to default\n',
				'd - delete a category\n',
				'm - modify a category\n',
				'p - print out the category')
		uinput = input("")
		if uinput is "r":
			category.categories =['Bank', 'Entertainment', 'Food', 'Other'] 
			print("categories are restored to default")
		if uinput is "m":
			self.print_categories()
			mod = int(input("Enter the category ID"))
			temp_category = input("Enter the new name of the category")
			category.categories[mod] = temp_category
		if uinput is "d":
			self.print_categories()
			mod = int(input("Enter the ID you want to delete"))
			del category.categories[mod]	
		if uinput is "p":
			self.print_categories()

	def add_category():
		cate = category.categories
		cat = None
		while cat is None:
			cate_in = input("Choose a category from the list or enter your own:")
			try:
				val = int(cate_in)
				if val < len(cate):
					cat = cate[val]
				else:
					print("# entered is out of range")
			except ValueError:
				cat = cate_in
				category.categories.append(cat)
		return cat

	def setCategories(cate):
		categories = cate
	
	def getCategories():
		return categories


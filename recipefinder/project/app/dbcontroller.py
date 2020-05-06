from tinydb import TinyDB, Query, where
import validators

db = TinyDB("db-test.json")

class RecipeList:
	recipeList = []

	def __init__(self):
		print("calling recipeList init")
		recipeTable = db.search(where("type") == "recipe")
		for recipe in recipeTable:
			r = RecipeObject(
				recipe["title"],
				recipe["description"],
				recipe["ingredient_list"],
				recipe["image_url"],
				recipe["link"],
			)
			# print(r.title)
			if validators.url(r.linkFull):
				# is actual website
				r.isWebsite = True
			if (
				r.image_url
				== "https://www.webfx.com/blog/images/cdn.designinstruct.com/files/582-how-to-image-placeholders/generic-image-placeholder.png"
			):
				self.recipeList.append(r)
			else:
				self.recipeList.insert(0, r)

	def getFilteredList(self, i_list):
		print("searching")
		if not i_list:
			# empty input list
			return self.recipeList
		foundList = []
		notFoundList = []
		for r in self.recipeList:
			found = 0
			r.numOfInputIng = 0
			for r_ing in r.ingredient_list:
				for ing in i_list:
					if r_ing.lower() == ing.lower():
						# print("found")
						r.numOfInputIng = r.numOfInputIng + 1
						found += 1
			if found:
				foundList.append(r)
			else:
				notFoundList.append(r)

		print("sorting")
		unsorted = foundList + notFoundList
		unsorted.sort(key=lambda x: x.numOfInputIng, reverse=True)
		self.recipeList = unsorted
		return self.recipeList


class RecipeObject:
	def __init__(self, title_, description_, ingredient_list_, image_url_, link_):
		self.title = title_
		self.description = description_
		self.ingredient_list = ingredient_list_
		self.image_url = image_url_
		self.link = (link_[:12] + "..") if len(link_) > 12 else link_
		self.linkFull = link_
		self.numOfInputIng = 0
		self.isWebsite = False

class ShoppingList:
	neededIngredients = []
	usedIngredients = []
	def __init__(self, r_slist, inputIngredientList):
		self.usedIngredients.clear()
		self.neededIngredients.clear()
		# a = shoppingListIngredient()

		#convert rlist to r_olist
		r_olist = self.strListToObjList(r_slist)

		for recipe in r_olist:
			print("r_slist count", len(r_slist))
			for ringredient in recipe.ingredient_list:
				a = shoppingListIngredient()
				if ringredient in inputIngredientList:
					a.name = ringredient
					a.occurences += 1
					self.usedIngredients.append(a)
				else:
					a.name = ringredient
					a.occurences += 3
					self.neededIngredients.append(a)

	def strListToObjList(self, slist):
		olist = []
		print(slist)
		for recipe in slist:
			rec = db.search(where("title") == recipe)
			if (len(rec) == 0):
				#length is zero
				print("length of rec is 0")
				return
			else:
				rec = rec[0]
				ro = RecipeObject(
					rec["title"],
					rec["description"],
					rec["ingredient_list"],
					rec["image_url"],
					rec["link"],
				)
				olist.append(ro)

		print(olist)
		return olist


	def getNeededIngredients(self):
		return self.neededIngredients

	def getUsedIngredients(self):
		return self.usedIngredients

class shoppingListIngredient:
	def __init__(self):
		self.occurences = 0
		self.name = ""

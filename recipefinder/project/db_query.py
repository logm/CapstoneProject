from tinydb import TinyDB, Query, where

db = TinyDB('db.json')

# db.insert({
# 	'type': 'recipe',
# 	'title': 'test123',
# 	'description': 'test test test',
# 	'ingredient_list': ['asd', 'asdd', 'xyz'],
# 	'image_url': 'https://i.pinimg.com/474x/52/bc/e1/52bce14a1196430b6ecabfb51ca930a4.jpg'
# 	'link': 'google.com'
# 	})

class RecipeList:
	def __init__(self, recipeTable):
		for recipe in recipeTable:
			# r = RecipeObject('test1', 'd1', 'i1', 'im2', 'l1')
			r = RecipeObject(recipe['title'], recipe['description'], recipe['ingredient_list'], recipe['image_url'], recipe['link'])
			# print(r.title)
			self.recipeList.append(r)
	recipeList = []
	def getRecipeList(self):
		return self.recipeList




class RecipeObject:
	def __init__(self, title_, description_, ingredient_list_, image_url_, link_):
		self.title = title_
		self.description = description_
		self.ingredient_list = ingredient_list_
		self.image_url = image_url_
		self.link = link_
	# title = ''
	# description = ''
	# ingredient_list = ''
	# image_url = ''
	# link = ''


# r2 = RecipeObject('test1', 'd1', 'i1', 'im2', 'l1')
# print(r2.description)
recipeTable = db.search(where('type') == 'recipe')
rq = RecipeList(recipeTable)
x = rq.getRecipeList()
# print(x[0])
for i in x:
	print(i.description)
print(x[0].title)
# print(rq.getRecipeList())

# for i in rq.getRecipeList:
# 	print(i)
# print(rq.getRecipeList[0])
# recipeList = []

# for recipe in recipeTable:
# 	r = RecipeObject(recipe['title'], recipe['description'], recipe['ingredient_list'], recipe['image_url'], recipe['link'])
# 	print(r.title)
# 	# r = {'title': str(recipe['title']), 'description': recipe['description'], 'ingredient_list': recipe['ingredient_list'], 'image_url': recipe['image_url'], 'link': recipe['link']}
# 	# print(r["title"])
# 	# r.title = recipe['title']
# 	# r.description = recipe['description']
# 	# for ingredient in recipe['ingredient_list']:
# 	# 	print(role)
# 	# 	r.ingredient_list.append(ingredient)
# 	# r.image_url = recipe['image_url']
# 	# r.link = recipe['link']


# 	recipeList.append(r)



print("done")
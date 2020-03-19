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

recipeTable = db.search(where('type') == 'recipe')
recipeList = []

# print(userTable)
for recipe in recipeTable:
	r = {'title': recipe['title'], 'description': recipe['description'], 'ingredient_list': recipe['ingredient_list'], 'image_url': recipe['image_url'], 'link': recipe['link']}

	# r.title = recipe['title']
	# r.description = recipe['description']
	# for ingredient in recipe['ingredient_list']:
	# 	print(role)
	# 	r.ingredient_list.append(ingredient)
	# r.image_url = recipe['image_url']
	# r.link = recipe['link']


	recipeList.append(r)


print(recipeList)

print("done")
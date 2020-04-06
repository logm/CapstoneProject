from tinydb import TinyDB, Query, where


db = TinyDB('db.json')

print("title: ")
inputTitle = input()
print("description: ")
inputDescription = input()
print("ingredient_list: ")
inputIngredient = input()
print("image url: ")
inputImage = input()
print("link: ")
inputLink = input()



db.insert({
	'type': 'recipe',
	'title': inputTitle,
	'description': inputDescription,
	'ingredient_list': [inputIngredient, 'asdd', 'xyz'],
	'image_url': inputImage,
	'link': inputLink
	})



print("done")
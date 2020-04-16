from tinydb import TinyDB, Query, where


db = TinyDB('db.json')

for i in range(133):
	print(i)
	# print("title: ")
	inputTitle = input()
	print("inputTitle", inputTitle)
	# print("description: ")
	inputDescription = input()
	print("inputDescription", inputDescription)
	# print("num of ingredients")
	inputNumOfIng = input()
	inputIngredient = []
	for i in range(int(inputNumOfIng)):
		# print("ingredient: ")
		tmp = input()
		inputIngredient.append(tmp)
	# print("image url: ")
	print("inputIngredient", str(inputIngredient))
	inputImage = input()
	print("inputImage", inputImage)
	# print("link: ")
	inputLink = input()

	print("inputLink", inputLink)

	db.insert({
		'type': 'recipe',
		'title': inputTitle,
		'description': inputDescription,
		'ingredient_list': inputIngredient,
		'image_url': inputImage,
		'link': inputLink
		})




db.count()

print("done")
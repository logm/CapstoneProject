from tinydb import TinyDB, Query, where


db = TinyDB('db.json')




db.insert({
	'type': 'recipe',
	'title': 'test123',
	'description': 'test test test',
	'ingredient_list': ['asd', 'asdd', 'xyz'],
	'image_url': 'https://i.pinimg.com/474x/52/bc/e1/52bce14a1196430b6ecabfb51ca930a4.jpg',
	'link': 'google.com'
	})



print("done")
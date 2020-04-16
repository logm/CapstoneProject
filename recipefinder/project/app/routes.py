from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ingredientSearch
from tinydb import TinyDB, Query, where
import validators

db = TinyDB('db.json')

class RecipeList:
	def __init__(self):
		print("calling recipeList init")
		recipeTable = db.search(where('type') == 'recipe')
		for recipe in recipeTable:
			r = RecipeObject(recipe['title'], recipe['description'], recipe['ingredient_list'], recipe['image_url'], recipe['link'])
			# print(r.title)
			if validators.url(r.linkFull):
				#is actual website
				r.isWebsite = True
			if r.image_url == 'https://www.webfx.com/blog/images/cdn.designinstruct.com/files/582-how-to-image-placeholders/generic-image-placeholder.png':
				self.recipeList.append(r)
			else:
				self.recipeList.insert(0, r)
	recipeList = []
	def getFilteredList(self, i_list):
		print("searching")
		if not i_list:
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
		unsorted.sort(key=lambda x: x.numOfInputIng, reverse = True)
		self.recipeList = unsorted
		return self.recipeList


class RecipeObject:
	def __init__(self, title_, description_, ingredient_list_, image_url_, link_):
		self.title = title_
		self.description = description_
		self.ingredient_list = ingredient_list_
		self.image_url = image_url_
		self.link = (link_[:12] + '..') if len(link_) > 12 else link_
		self.linkFull = link_
		self.numOfInputIng = 0
		self.isWebsite = False

input_ingredient_list = []
rlist = []
print("getting recipes from db")
# recipeTable = db.search(where('type') == 'recipe')
rq = RecipeList()
rlist  = rq.getFilteredList(None)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = ingredientSearch()
	if form.inputingredient.data:
		if form.inputingredient.data not in input_ingredient_list:
			input_ingredient_list.append(form.inputingredient.data)
	form.inputingredient.data = ""

	print("list of input ingredients", str(input_ingredient_list))

	print("creating new rlist")
	rlist  = rq.getFilteredList(input_ingredient_list)


	return render_template('index.html', title='Home',  recipeList = rlist, form = form, input_ingredient_list = input_ingredient_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		print("user name:", form.username.data)
		return redirect(url_for('index'))
	return render_template('login.html',  title='Sign In', form=form)

@app.route('/cart')
def cart():
	return render_template('cart.html', title='Cart')

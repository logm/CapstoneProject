from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ingredientSearch, addToCart
from . import dbcontroller
# from dbcontroller import *



rq = dbcontroller.RecipeList()
print("getting recipes from db")
#global lists
rlist = []
input_ingredient_list = []
cartRecipes = [] # for cart page

rlist  = rq.getFilteredList(None) # load full recipe list on first page load



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = ingredientSearch()
	addToCartForm = addToCart()
	print(addToCartForm.inputCart.data)
	cartRecipes.append(addToCartForm.inputCart.data)

	#prevents duplicate inputs
	if form.inputingredient.data:
		if form.inputingredient.data not in input_ingredient_list and form.inputingredient.data != '':
			input_ingredient_list.append(form.inputingredient.data)
	#clears previous search from searchbox
	form.inputingredient.data = ""

	# print("list of input ingredients", str(input_ingredient_list))

	print("overwrites rlist")
	rlist  = rq.getFilteredList(input_ingredient_list)

	return render_template('index.html', title='Home',  recipeList = rlist, form = form, input_ingredient_list = input_ingredient_list, addToCartForm = addToCartForm)


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
	# cartRecipes = rlist # this should be generated by add to cart
	# sl =ShoppingList(cartRecipes, input_ingredient_list)
	print("input_ingredient_list", input_ingredient_list)
	print("cartRecipes", cartRecipes)
	sl = dbcontroller.ShoppingList(cartRecipes, input_ingredient_list)
	needed = sl.getNeededIngredients()
	used = sl.getUsedIngredients()
	cartRecipesAsObjects = sl.strListToObjList(cartRecipes)
	print("needed", needed)
	print("used", used)
	print("cartRecipesAsObjects", cartRecipesAsObjects)
	return render_template('cart.html', title='Cart', cartRecipes = cartRecipesAsObjects, neededIngredients = needed, usedIngredients = used)
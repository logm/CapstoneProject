from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from tinydb import TinyDB, Query, where


db = TinyDB('db.json')


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguasdel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # recipes = [
    #     {
    #         'image_url': 'https://www.seriouseats.com/recipes/images/2015/07/20150702-sous-vide-hamburger-anova-primary-1500x1125.jpg',
    #         'title': 'Burger',
    #         'description': 'This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
    #         'ingredient_list': {'xyz', 'abc'},
    #         'link': 'google.com'
    #     }
    # ]
    # recipeList = []
    # recipeList.append(recipes)

    recipeTable = db.search(where('type') == 'recipe')
    recipeList = []

    # print(userTable)
    for recipe in recipeTable:
	    r = {'title': recipe['title'], 'description': recipe['description'], 'ingredient_list': recipe['ingredient_list'], 'image_url': recipe['image_url'], 'link': recipe['link']}
	    recipeList.append(r)

    return render_template('index.html', title='Home',  recipeList = recipeList)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

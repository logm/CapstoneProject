from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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
    recipes = [
        {
            'image_url': 'https://www.seriouseats.com/recipes/images/2015/07/20150702-sous-vide-hamburger-anova-primary-1500x1125.jpg',
            'title': 'Burger',
            'description': 'This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
            'ingredient_list': {'xyz', 'abc'},
            'link': 'google.com'
        },
        {
            'image_url': 'https://i.pinimg.com/474x/52/bc/e1/52bce14a1196430b6ecabfb51ca930a4.jpg',
            'title': 'Spaghetti ',
            'description': 'This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
            'ingredient_list': {'xyz', 'abc'},
            'link': 'google.com'
        },
        {
            'image_url': 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/10/11/1/FNK_Simple-Homemade-Pancakes_s4x3.jpg.rend.hgtvcom.826.620.suffix/1476216522537.jpeg',
            'title': 'Pancakes ',
            'description': 'This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
            'ingredient_list': {'xyz', 'abc'},
            'link': 'google.com'
        },
        {
            'image_url': 'https://i.pinimg.com/474x/52/bc/e1/52bce14a1196430b6ecabfb51ca930a4.jpg',
            'title': 'Spaghetti ',
            'description': 'This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.',
            'ingredient_list': {'xyz', 'abc'},
            'link': 'google.com'
        }
    ]
    recipeList = []
    recipeList.append(recipes)
    recipeList.append(recipes)
    recipeList.append(recipes)
    return render_template('index.html', title='Home', user=user, posts=posts, recipeList = recipeList)


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

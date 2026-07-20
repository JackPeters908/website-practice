from bottle import run, route, template, view, static_file

# Routes For Pages

@route('/')
@view('home') # uses views/home.tpl
def home():
    return {}

@route('/about')
def about():
    return template('about')

@route('/contact')
from flask import Flask, render_template
from vsearch import search4letters
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello from flask'
@app.route('/search4')
def do_search():
	return str(search4letters("The world is big"))

@app.route ('/entry')
def entry_page():
	return render_template('entry.html', the_title='Welcome to search4letters on the web!')

app.run()


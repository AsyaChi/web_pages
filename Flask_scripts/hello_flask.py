from flask import Flask, render_template, request
from vsearch import search4letters
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello from flask'
@app.route('/search4', methods=['post']) 
def do_search():
	phrase = request.form['phrase']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4letters(phrase, letters))
	return render_template('results.html',
		the_phrase = phrase,
		the_title = title,
		the_letters = letters,
		the_results = results)

@app.route ('/entry')
def entry_page():
	return render_template('entry.html', the_title='Welcome to search4letters on the web!')

app.run(debug=True)


from flask import Flask, Blueprint, request, redirect, render_template_string, url_for, session
import random

routes = Blueprint('main', __name__)

## to-do: create a larger list and store as CSV
personal_pronoun_list = ["Eu", "Tu", "Você", "Ela", "Ele", "A gente", "Nós", "Vocês", "Elas", "Eles"]
verb_list = ["ir", "ser", "fazer", "ter", "ver", "vir", "estar", "amar", "poder", "dar", "pôr", "comer", "querer", "partir", "falar", "trazer", "estudar", "cantar", "dizer", "sair", "ler", "saber", "rir", "vender", "agir", "pedir", "ouvir", "ficar", "agir", "precisar"]

random.shuffle(verb_list)


@routes.route('/', methods=["POST", "GET"])
def index():
	return render_template_string('''
		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Verbo</title>
			<style>
				body {
					font-family: Arial, sans-serif;
					color: black;
					text-align: center;
					padding: 50px;
					}
				.button-container {
					display: flex;
					justify-content: center;
					gap: 20px;
					margin-top: 100px;
				}
				.button-container form {
					display: inline-block;
				}
				.button-container input[type="submit"] {
					font-size: 20px;
					padding: 15px 30px;
					width: 200px;
					cursor: pointer;
					background-color: #009739;
					color: #FEDD00;
					border: none;
					border-radius: 5px;
					transition: background-color 0.3s ease;
				}
				.button-container input[type="submit"]:hover {
					background-color: #012169;
					color: white;
				}
			</style>
		</head>
		<body>
			<h1>Bem-vindo! Selecione uma opção abaixo, por favor.</h1>
			<div class="button-container">
				<form method="POST" action="/practice">
					<input type="submit" name="action" value="Prática">
				</form>
				<form method="POST" action="/timed">
					<input type="submit" name="action" value="Chronometrado">
				</form>
			</div>
		</body>
		</html>
	''')

@routes.route('/practice', methods=["POST", "GET"])
def practice():
	# Initialize indices 
	if 'verb_counter' not in session:
		session['verb_counter'] = 0
	verb_counter = session['verb_counter']

	if 'score_counter' not in session:
		session['score_counter'] = 0
	score_counter = session['score_counter']

	# If you've gone through all the verbs once, reshuffle them
	if verb_counter >= len(verb_list):
		random.shuffle(verb_list)

	# Select a random pronoun from the list
	current_pronoun = random.sample(personal_pronoun_list, 1)[0]

	# If they have gone through every verb, start back at 0 but keep counter for final score
	current_verb = verb_list[verb_counter%len(verb_list)]

	if request.form['action'] == 'Sim':
		session['score_counter'] += 1
		session['verb_counter'] += 1
	if request.form['action'] == 'Não':
		session['verb_counter'] += 1
	if request.form['action'] == 'Terminei!':
		return redirect(url_for('score'))

	return render_template_string('''
		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device_width, initial-scale=1.0">
			<center><title>Prática</title></center>
		</head>
		<body>
			<h1>{{ current_pronoun }} ({{ current_verb }})</h1>
			<p>Correto?</p>
			<form method="POST">
				<p></p>
				<input type="submit" name="action" value="Sim">
				<input type="submit" name="action" value="Não">
			</form>
				<p></p>
			<form method="POST" action="/score">
				<p><input type="submit" name="action" value="Terminei!"></p>
			</form>
		</body>
		</html>
	''', current_verb=current_verb, current_pronoun=current_pronoun)

@routes.route('/score', methods=["POST", "GET"])
def score():
	verb_counter = session.get('verb_counter', 0)
	score_counter = session.get('score_counter', 0)

	return render_template_string('''
		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device_width, initial-scale=1.0">
			<title>Portuguese Verb Score</title>
		</head>
		<body>
			<h1>Você acertou {{ score_counter }} de {{ verb_counter }}!</h1>
			<form method="POST" action="/reset"
				<p></p>
				<input type="submit" name="action" value="Tentar novamente?">
			</form>
		</body>
		</html>
	''', verb_counter=verb_counter, score_counter=score_counter)

@routes.route('/reset', methods=["POST"])
def reset():
	session['verb_counter'] = 0
	session['score_counter'] = 0

	return redirect('/')


@routes.route('/timed', methods=["POST"])
def timed():
	return "Fique ligado!"
	
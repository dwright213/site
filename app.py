from flask import Flask, render_template, request, g, abort
app = Flask(__name__)

@app.before_request
def set_up_nav():
	g.nav = ['home', 'infos', 'fotos', 'etc']

@app.route('/')
def home():
	# print(request.url)
	# abort(403)
	return render_template('index.html')

@app.route('/infos')
def infos():
	return render_template('infos.html')

@app.route('/fotos')
def fotos():
	return render_template('fotos.html')

@app.route('/etc')
def etc():
	return render_template('etc.html')

if __name__ == "__main__":
	app.run()

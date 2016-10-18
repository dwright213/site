from flask import Flask, render_template, request, g, abort, jsonify
import pytumblr

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

@app.before_request
def set_up_nav():
	g.nav = ['home', 'infos', 'fotos', 'etc']

def tumblr_keys():
	g.client = pytumblr.TumblrRestClient(
	app.config['CONSUMER_KEY'],
	app.config['CONSUMER_SECRET'],
	app.config['OAUTH_TOKEN'],
	app.config['OAUTH_SECRET'])

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

@app.route('/tumblr')
def tumblr():
	tumblr_keys()
	posts = g.client.posts('classicsretold', limit='10', type='photo')['posts']
	photos = []
	for i, post in enumerate(posts):
		photos.append(post['photos'][0]['alt_sizes'][5])
		photos[i]['quote'] = post['caption']

	# return jsonify(posts)
	return jsonify(photos)


if __name__ == "__main__":
	app.run()

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
	tumblr_keys()
	posts = g.client.posts(app.config['PHOTO_BLOG'], limit='100', type='photo', filter='text')['posts']
	return render_template('fotos.html', posts=posts)

# @app.route('/fotosobject')
# def fotosobject():
# 	tumblr_keys()
# 	photos = g.client.posts(app.config['PHOTO_BLOG'], limit='10', type='photo', filter='text')['posts']
# 	# return render_template('fotos.html', photos=photos)
# 	return jsonify(photos)

@app.route('/etc')
def etc():
	return render_template('etc.html')

@app.route('/video/therealgundam')
def video():
	return render_template('video.html', video=app.config['GUNDAM_VIDEO'])

if __name__ == "__main__":
	app.run()

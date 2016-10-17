from flask import Flask, render_template, request, g, abort, jsonify
import pytumblr

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

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

@app.route('/tumblr_info')
def get_tumblr_info():
    client = pytumblr.TumblrRestClient(
        app.config['CONSUMER_KEY'],
        app.config['CONSUMER_SECRET'],
        app.config['OAUTH_TOKEN'],
        app.config['OAUTH_SECRET']
    )
    return jsonify(client.info())

@app.route('/tumblr_photos')
def get_tumblr_photos():
    client = pytumblr.TumblrRestClient(
        app.config['CONSUMER_KEY'],
        app.config['CONSUMER_SECRET'],
        app.config['OAUTH_TOKEN'],
        app.config['OAUTH_SECRET']
    )
    return jsonify(client.posts('classicsretold.tumblr.com', type='photo', limit=1000, filter='text'))

if __name__ == "__main__":
	app.run()

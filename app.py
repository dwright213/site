from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, redirect, url_for
import pytumblr
from flask_mongokit import MongoKit, Document



app = Flask(__name__)
app.config.from_pyfile('settings.cfg')


# mongo stuff
class Blag(Document):
    __collection__ = 'blags'
    structure = {
        'title': unicode,
        'text': unicode,
        'creation': datetime,
    }
    required_fields = ['title', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True
db = MongoKit(app)
db.register([Blag])
# end mongo stuff


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
	return render_template('index.html')

@app.route('/blags')
def blags():
	jason = []
	blags = db.Blag.find()
	for blag in blags:
		jason.append({'title': blag.title, 'text': blag.text, 'id': str(blag._id)})
	return jsonify(jason)

@app.route('/add', methods=['POST'])
def add():
	blag = db.Blag()
	print(request.form)
	blag.title = request.form['title']
	blag.text = request.form['text']
	blag.save()
	return redirect(url_for('blags'))

@app.route('/edit/<id>')
def edit(id):
	blag = db.Blag.find({'id': id})
	return render_template('edit.html', blag=blag)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/infos')
def infos():
	return render_template('infos.html')

@app.route('/fotos')
def fotos():
	tumblr_keys()
	posts = g.client.posts(app.config['PHOTO_BLOG'], limit='100', type='photo', filter='text')['posts']
	return render_template('fotos.html', posts=posts)

@app.route('/etc')
def etc():
	return render_template('etc.html')

@app.route('/video/therealgundam')
def video():
	return render_template('video.html', video=app.config['GUNDAM_VIDEO'])

if __name__ == "__main__":
	app.run()

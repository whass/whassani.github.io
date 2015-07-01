import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from flaskext.markdown import Markdown


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = '../_blogContent'
POST_DIR = 'posts'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite','headerid','extra','toc']
FREEZER_RELATIVE_URLS=True
FREEZER_DESTINATION="../"

app = Flask(__name__,  static_url_path='')



flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md','_blogContent','_blogApp', 'content_update.sh']

@app.route('/css/pygments.css')
def pygments_css():
    return pygments_style_defs('friendly'), 200, {'Content-Type': 'text/css'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hire.html')
def hire():
    return render_template('hire.html')


@app.route("/posts/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@app.route("/categories/<name>/")
def categories(name):
    posts = (p for p in flatpages if name in p.meta['categories'])
    return render_template('posts.html', posts=posts)


@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)

    return render_template('post.html', post=post)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)

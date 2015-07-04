import sys
from flask import Flask, render_template, render_template_string, Markup
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from flask_frozen import Freezer
from flaskext.markdown import Markdown
from markdown.extensions import Extension



class DefaultConfig(object):
    @staticmethod
    def prerender_jinja(text):
        prerendered_body = render_template_string(Markup(text))
        return pygmented_markdown(prerendered_body, flatpages)

    DEBUG = True
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = '../_blogContent'
    POST_DIR = 'posts'
    PAGE_DIR = 'pages'
    FREEZER_DESTINATION_IGNORE = ['.git*', 'CNAME', '.gitignore', 'readme.md','_blogContent','_blogApp', 'content_update.sh']
    FLATPAGES_HTML_RENDERER = prerender_jinja
    FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite','tables','extra','toc']
    PYGMENTS_STYLE = 'friendly'
    FREEZER_RELATIVE_URLS=True
    FREEZER_DESTINATION="../"


app = Flask(__name__)

app.config.from_object(DefaultConfig)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route('/pygments.css')
def pygments_css():
    style = app.config['PYGMENTS_STYLE']
    return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}

@app.route('/')
def home():
    posts = [p for p in flatpages if p.path.startswith(app.config['POST_DIR'])]
    posts.sort(key=lambda item:item['date'], reverse=True)
    return render_template('index.html', posts=posts[:4])

@app.route('/pages/<name>/')
def page(name):
    path = '{}/{}'.format(app.config['PAGE_DIR'], name)
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page) 


@app.route("/posts/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(app.config['POST_DIR'])]
    posts.sort(key=lambda item:item['date'], reverse=True)
    return render_template('posts.html', posts=posts)

@app.route("/categories/<name>/")
def categories(name):
    posts = (p for p in flatpages if name in p.meta['categories'])
    return render_template('posts.html', posts=posts)


@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(app.config['POST_DIR'], name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)

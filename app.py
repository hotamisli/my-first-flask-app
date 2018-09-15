from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from data import Articles
app = Flask(__name__)

Articles = Articles()
#pp.debug = True
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
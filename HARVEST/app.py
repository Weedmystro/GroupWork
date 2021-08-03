from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/menu')
def about():
 return render_template('menu.html')



@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

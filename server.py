import uuid
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    male = db.Column(db.Integer)
    female = db.Column(db.Integer)

    def __init__(self, name, male, female):
        self.name = name
        self.male = male
        self.female = female


# the base route which renders a template
@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/movies/<movie_name>')
def get_movies (movie_name):
    m = Movie(movie_name, 5, 5)
    db.session.add(m)
    db.session.commit()
    return jsonify({'success': True})

'''
# create a movie
@app.route('/movies/create', methods=['POST'])
def create_movie ():
    payload = request.get_json()
    # guard clause to  ensure value is valid
    movie = movie('knowleton', payload['value'])
    db.session.add(movie)
    db.session.commit()
    return jsonify(payload)
'''

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args

from data import Movies

app = Flask(__name__)

movies = Movies()

def get_movies(offset=0, per_page=10):
    return movies[offset: offset + per_page]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/movies')
def movies_list():
   page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
   total = len(movies)
   pagination_movies = get_movies(offset=offset, per_page=per_page)
   print(per_page)
   pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

   return render_template('movies.html', movies=pagination_movies,page=page,per_page=per_page,pagination=pagination)

@app.route('/movie/<string:id>/')
def movie(id):
   return render_template('movie.html', id=id)

if __name__ == "__main__":
    app.run(debug = True)

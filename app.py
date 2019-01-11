from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
import omdb
from data import *

app = Flask(__name__)

def loadMoviesInfo(moviesIds):
    res = []
    for mov_id in moviesIds:
        res.append(getMovieInfo(mov_id[0]))
    return res

def getMovieInfo(movId):
    movie_info = omdb.imdbid(movId, timeout=5)
    movie_info['id'] = movId
    return movie_info

def get_movies(offset=0, per_page=2):
    mov = movies(offset, per_page)
    movie_infos = loadMoviesInfo(mov)
    #print(movie_infos)
    return movie_infos

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
    
    total = getNumberOfMovies()
    pagination_movies = get_movies(offset=offset, per_page=per_page)
    #print(per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('movies.html', movies=pagination_movies,page=page,per_page=per_page,pagination=pagination)

@app.route('/movie/<string:id>/')
def movie(id):
    movie = getMovieInfo(id)
    return render_template('movie.html', movie=movie)

if __name__ == "__main__":
    # can be used for 1000 requests per day
	# Another key -> 596d8b73
    omdb.set_default('apikey', '586cf9a9')
    app.run(debug = True)

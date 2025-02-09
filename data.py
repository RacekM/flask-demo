import os
import sqlite3
import pandas as dd
conn = None



def createDbFile(folderPath):    
    data_url = 'movie_id.tsv'
    data_reader = dd.read_csv(folderPath + data_url, sep = '\t', chunksize=10000)
    for chunk in data_reader:
        df = dd.concat([chunk])
        df.to_sql('movieIds', con=conn, if_exists='append')


if not os.path.exists('films.db'):
    conn = sqlite3.connect('films.db', check_same_thread=False)
    createDbFile("data\\")

    #os.remove('films.db')

conn = sqlite3.connect('films.db', check_same_thread=False)
    
    

def movies(skip, number):
    movies = conn.execute("SELECT MOVIE_ID FROM movieIds LIMIT " + str(skip) + "," + str(number)).fetchall()
    return movies

def getNumberOfMovies():
    #the OMDb database is not containning the newest movies. My db contains about 902882 records, but i will access just 800 000.
    #number = conn.execute("SELECT Count(MOVIE_ID) FROM movieIds ").fetchone()
    #return number[0]
    return 800000

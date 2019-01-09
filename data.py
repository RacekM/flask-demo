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
#print(conn.execute("SELECT * FROM t LIMIT 10,10").fetchall())
    
    

def movies(skip, number):
    movies = conn.execute("SELECT MOVIE_ID FROM movieIds LIMIT " + str(skip) + "," + str(number)).fetchall()
    return movies

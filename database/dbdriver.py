import sqlite3 
dbname = "databasev1.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS genre
    (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE
    )
    '''

)
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

'''
)

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    genre_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genre(id)
    )
    '''
)

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS watch_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        movie_id INTEGER,
        watched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(id)
        FOREIGN KEY (movie_id) REFERENCES movies(id)



    )


    '''
)

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS recommended_content(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    watched BOOLEAN DEFAULT FALSE,
    recommended_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
    FOREIGN KEY (movie_id) REFERENCES movies(id)
   
    )
    '''
)






conn.commit()
conn.close()
import sqlite3 as sql
def showAll(dbname):
    conn = sql.connect(dbname)
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    res = c.fetchall()

    for table in res:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        c.execute(f"SELECT * FROM {table_name}")
        rows = c.fetchall()

        for row in rows:
            print(row)

    conn.close()
def makeTables(dbname):
    conn = sql.connect(dbname)
    c = conn.cursor()
    # Create UserItemInteraction table
    c.execute('''
    CREATE TABLE IF NOT EXISTS UserItemInteraction (
        user_id INTEGER,
        item_id INTEGER,
        interaction_type TEXT,
        interaction_value TEXT,
        interaction_timestamp DATETIME,
        PRIMARY KEY (user_id, item_id),
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (item_id) REFERENCES ItemMetaData(item_id)
    );
    ''')

    # Create ItemMetaData table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ItemMetaData (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre TEXT,
        director_id INTEGER,
        actor_ids TEXT,
        release_year INTEGER,
        title TEXT,
        runtime INTEGER,
        plot_summary TEXT,
        average_rating REAL,
        FOREIGN KEY (director_id) REFERENCES Director(id)
    );
    ''')

    # Create User table
    c.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT,
        registration_date DATETIME
    );
    ''')

    # Create Movie table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Movie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        release_year INTEGER,
        genre TEXT,
        runtime INTEGER,
        plot_summary TEXT,
        average_rating REAL
    );
    ''')

    # Create Director table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Director (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT
    );
    ''')

    # Create Review table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Review (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        user_id INTEGER,
        rating REAL,
        review_text TEXT,
        FOREIGN KEY (movie_id) REFERENCES Movie(id),
        FOREIGN KEY (user_id) REFERENCES User(id)
    );
    ''')

    # Create Actor table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Actor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        birthdate DATE,
        nationality TEXT
    );
    ''')

    # Create ItemSimilarity table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ItemSimilarity (
        item1_id INTEGER,
        item2_id INTEGER,
        similarity_score REAL,
        PRIMARY KEY (item1_id, item2_id),
        FOREIGN KEY (item1_id) REFERENCES ItemMetaData(item_id),
        FOREIGN KEY (item2_id) REFERENCES ItemMetaData(item_id)
    );
    ''')

    # Create UserRecommendation table
    c.execute('''
    CREATE TABLE IF NOT EXISTS UserRecommendation (
        user_id INTEGER,
        recommendation_item_id INTEGER,
        predicted_rating REAL,
        PRIMARY KEY (user_id, recommendation_item_id),
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (recommendation_item_id) REFERENCES ItemMetaData(item_id)
    );
    ''')
    # Create Genre Table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Genre (
        genre_id INTEGER PRIMARY KEY,
        genre_name TEXT
    );
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

def insert_user_item_interaction(dbname, user_id, item_id, interaction_type, interaction_value, interaction_timestamp):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO UserItemInteraction (user_id, item_id, interaction_type, interaction_value, interaction_timestamp)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, item_id, interaction_type, interaction_value, interaction_timestamp))
    conn.commit()
    conn.close()

def insert_item_metadata(dbname, item_id, genre, director_id, actor_ids, release_year, title, runtime, plot_summary, average_rating):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO ItemMetaData (item_id, genre, director_id, actor_ids, release_year, title, runtime, plot_summary, average_rating)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (item_id, genre, director_id, actor_ids, release_year, title, runtime, plot_summary, average_rating))
    conn.commit()
    conn.close()

def insert_user(dbname, id, username, email, password, registration_date):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO User (id, username, email, password, registration_date)
    VALUES (?, ?, ?, ?, ?)
    ''', (id, username, email, password, registration_date))
    conn.commit()
    conn.close()

def insert_movie(dbname, id, title, release_year, genre, runtime, plot_summary, average_rating):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO Movie (id, title, release_year, genre, runtime, plot_summary, average_rating)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id, title, release_year, genre, runtime, plot_summary, average_rating))
    conn.commit()
    conn.close()

def insert_director(dbname, id, firstNameame, lastName):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO Director (id, firstName, lastName)
    VALUES (?, ?)
    ''', (id, firstName, lastName))
    conn.commit()
    conn.close()

def insert_review(dbname, id, movie_id, user_id, rating, review_text):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO Review (id, movie_id, user_id, rating, review_text)
    VALUES (?, ?, ?, ?, ?)
    ''', (id, movie_id, user_id, rating, review_text))
    conn.commit()
    conn.close()

def insert_actor(dbname, id, firstName, lastName, birthdate, nationality):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO Actor (id, firstName, lastName, birthdate, nationality)
    VALUES (?, ?, ?, ?)
    ''', (id, firstName, lastName, birthdate, nationality))
    conn.commit()
    conn.close()

def insert_item_similarity(dbname, item1_id, item2_id, similarity_score):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO ItemSimilarity (item1_id, item2_id, similarity_score)
    VALUES (?, ?, ?)
    ''', (item1_id, item2_id, similarity_score))
    conn.commit()
    conn.close()

def insert_user_recommendation(dbname, user_id, recommendation_item_id, predicted_rating):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO UserRecommendation (user_id, recommendation_item_id, predicted_rating)
    VALUES (?, ?, ?)
    ''', (user_id, recommendation_item_id, predicted_rating))
    conn.commit()
    conn.close()
def insert_genre(dbname, genre_id, genre_name):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute('''
    INSERT OR REPLACE INTO Genre 
    VALUES (?, ?)
    ''', (genre_id, genre_name))
    conn.commit()
    conn.close()

def update_genre(dbname, genre_id, new_name):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute("UPDATE Genre SET genre_name = ? WHERE genre_id = ?", (new_name, genre_id))
    conn.commit()
    conn.close()

# When a user logs in, you want to retrieve their information from the database. 
def get_user_via_username(dbname, username):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT * FROM User WHERE username = ?", (username))
    user = c.fetchone()
    conn.close()
    return user

# When a user searches for a movie by its title, you want to retrieve the movie details.
def get_title_via_(dbname, title):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT * FROM Movie WHERE title=?", (title))
    movie = c.fetchone()
    conn.close()
    return movie

# When you want to display all reviews for a particular movie.
def get_reviews(dbname, movie_id):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT * FROM Review WHERE movie_id=?", (movie_id,))
    reviews = c.fetchall()
    conn.close()
    return reviews

# When you want to show a user the list of movies they have rated. 
def get_ratings_by_user(dbname, user_id):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT Movie.* FROM Movie JOIN Review ON Movie.id = Review.movie_id WHERE Review.user_id=?", (user_id,))
    movies_rated = c.fetchall()
    conn.close()
    return movies_rated



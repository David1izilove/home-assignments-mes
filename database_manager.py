import sqlite3


def create_database():
    """Create a SQLite database to store user scores if it doesn't already exist."""
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        guesses INTEGER,
                        time_taken REAL,
                        score REAL
                    )''')
    conn.commit()
    conn.close()


def save_score(name, guesses, time_taken, score):
    """Save the user's score to the database."""
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO scores (name, guesses, time_taken, score) VALUES (?, ?, ?, ?)',
                   (name, guesses, time_taken, score))
    conn.commit()
    conn.close()


def get_best_score():
    """Retrieve the best score from the database, ranked by the highest score."""
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, guesses, time_taken, score FROM scores ORDER BY score DESC LIMIT 1')
    best = cursor.fetchone()
    conn.close()
    return best

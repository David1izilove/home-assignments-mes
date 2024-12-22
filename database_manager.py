import sqlite3
from contextlib import contextmanager


@contextmanager
def db_connection():
    """
    Context manager for managing SQLite database connection and cursor.
    Yields:
        cursor: SQLite cursor object for executing queries.
    """
    conn = sqlite3.connect('game_scores.db')
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()


def create_database():
    """
    Create a SQLite database to store user scores if it doesn't already exist.
    """
    with db_connection() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            guesses INTEGER,
                            time_taken REAL,
                            score REAL
                        )''')


def save_score(name, guesses, time_taken, score):
    """
    Save the player's score into the database.
    """
    with db_connection() as cursor:
        cursor.execute('INSERT INTO scores (name, guesses, time_taken, score) VALUES (?, ?, ?, ?)',
                       (name, guesses, time_taken, score))


def get_best_score():
    """
    Retrieve the best score from the database, ranked by the highest score.
    """
    with db_connection() as cursor:
        cursor.execute('SELECT name, guesses, time_taken, score FROM scores ORDER BY score DESC LIMIT 1')
        best = cursor.fetchone()
        return best


def get_all_scores(limit=None):
    """
    Retrieve all scores from the database, optionally limited to the latest entries.
    """
    with db_connection() as cursor:
        if limit:
            cursor.execute(
                'SELECT name, guesses, time_taken, score FROM scores ORDER BY score DESC LIMIT ?',
                (limit,)
            )
        else:
            cursor.execute(
                'SELECT name, guesses, time_taken, score FROM scores ORDER BY score DESC'
            )
        return cursor.fetchall()

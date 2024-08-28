import sqlite3
from pympler import asizeof

class wordsolver_db():
    def __init__(self, db_path):
        self.db_path = db_path
    

    def initialize(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = '''
            CREATE TABLE IF NOT EXISTS old_words (
                    word TEXT NOT NULL
                )
        '''
        cursor.execute(query)
        conn.commit()

        query = '''
            CREATE TABLE IF NOT EXISTS sorted_words (
                    word TEXT NOT NULL
                )
        '''
        cursor.execute(query)
        conn.commit()

        conn.close()


    def __check(self):
        pass


    def save_data(self, data):
        # TODO: Think about sorting data, to make retrieval easier
        # TODO: Think about regex-based searching in database

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = '''
            INSERT INTO old_words (word)
            VALUES (?)
        '''
        cursor.executemany(query, data)
        conn.commit()
        conn.close()


    def get_sample(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM old_words ORDER BY RANDOM() LIMIT 1')
        random_entry = cursor.fetchone()
        conn.close()
        return random_entry
    

    def check_word(self, word):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM old_words where word = ?', (word, ))
        result = cursor.fetchone()
        conn.close()
        return result is not None



def get_words_from_source(db_path):
    # print("Starting to download and update word repository")
    # TODO: Add additional word sources
    # TODO: Set periodic database updates
    # TODO: Add set operations for adding and merging
    # TODO: Optimize memory for word-storing objects.

    db_obj = wordsolver_db(db_path=db_path)
    db_obj.initialize()

    try:
        # download nltk words
        import nltk # type: ignore
        from nltk.corpus import words # type: ignore
        import numpy as np

        nltk.download('words')
        words_arr = np.array(words.words())
        five_word_arr = words_arr[np.vectorize(len)(words_arr) == 5]
        five_word_arr = list(map(lambda x : (x, ), five_word_arr))
        # print(type(five_word_arr))
        db_obj.save_data(five_word_arr)

        del five_word_arr
    except Exception as e:
        print(f"Error in downloading NLTK words - {e}")

    # print(asizeof.asizeof(five_word_arr)/(1024 * 1024), "GB")

def get_random_word(db_path):
    db_obj = wordsolver_db(db_path=db_path)
    return str(db_obj.get_sample()[0]).upper()

def check_if_word_exists()
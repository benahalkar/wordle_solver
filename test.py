import os
from utils import get_words_from_source

code_path = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(code_path, "word_solver.db")

get_words_from_source(database_path)
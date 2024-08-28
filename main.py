import os
from utils import get_words_from_source, get_random_word

from play import practice

code_path = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(code_path, "word_solver.db")

# get_words_from_source(database_path)

choice = input("Which mode do you want to play in?\n\t1. Practice\n\t2. Cheat\n>> ")

if int(choice) == 1:
    play_obj = practice(get_random_word(database_path))
    play_obj.start()
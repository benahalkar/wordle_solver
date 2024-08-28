import os
from colorama import init, Fore, Back, Style

init()

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # MacOS and Linux
    else:
        os.system('clear') 

class practice():
    def __init__(self, word):
        self.__word = word
        self._max_chances = 6
        self.chance = 0
        self.solved = False

        self.words_till_now = []
        # NOTE: A lies @ 65 and Z lies @ 91
        self.letters_status = [3 for i in range(65, 91)]

    def __display_letter(self, letter, code, end=""):
        # NOTE: 0 perfect match 
        # NOTE: 1 some match
        # NOTE: 2 no match 
        # NOTE: 3 not selected
        bg_arr = [Back.GREEN, Back.YELLOW, Back.LIGHTBLACK_EX, Back.BLACK]
        fg_arr = [Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE]
        print(f"{bg_arr[code]}{fg_arr[code]}{letter}{Style.RESET_ALL}", end=end)
    

    def _check(self, word):
        stat = []

        for i, letter in enumerate(word):
            if self.__word[i] == letter:
                stat.append(0)
            elif letter in self.__word:
                stat.append(1)
            else:
                stat.append(2)

        return stat
    
    def _display(self):
        

        clear_screen()
        print(self.__word, end="\n-------\n")
        for word, codes in self.words_till_now:
            for letter, code in zip(word, codes):
                self.letters_status[ord(letter.upper()) - 65] = min(code, self.letters_status[ord(letter.upper()) - 65])
                self.__display_letter(letter, code)
            print()
        
        print("\n")

        for letter, code in zip(range(65, 91), self.letters_status):
            self.__display_letter(chr(letter), code, end=" ")
        print()

        if sum(self.words_till_now[-1][1]) == 0: 
            self.solved = True



    def start(self):
        print(self.__word)
        while self.chance < self._max_chances and not self.solved:
            word = input(f"{self.chance + 1} >> ")[:5].upper()
            codes = self._check(word)
            self.words_till_now.append((word, codes))
            self._display()
            self.chance += 1


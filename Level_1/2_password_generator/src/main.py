import random
import string
from abc import ABC, abstractmethod

import nltk

try:
    nltk.data.find('corpora/words.zip')
except LookupError:
    nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int=4):
        self.length = length

    def generate(self) -> str:
        return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 16, include_numbers: bool = True, include_symbols: bool = True):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        return "".join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words: int = 4, sep: str = '-', capitalize: bool = False, min_word_size: int = 3):
        self.num_of_words = num_of_words
        self.separator = sep
        self.capitalize = capitalize
        self.vocabulary_list = nltk.corpus.words.words()
        self.vocabulary_list = [word for word in self.vocabulary_list if len(word) >= min_word_size]


    def generate(self):
        password_words = [random.choice(self.vocabulary_list) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() for word in password_words]

        return self.separator.join(password_words)


if __name__ == '__main__':
    p_obj = MemorablePasswordGenerator()
    print(p_obj.generate())
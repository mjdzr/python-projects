from src.wordle import Wordle

wordle = Wordle(file_path='src/data/unigram_freq.csv', word_col = "word", count_col= "count")
wordle.run()
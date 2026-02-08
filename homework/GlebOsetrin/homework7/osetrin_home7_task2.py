words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
def my_words(new_words):
    for key, value in new_words.items():
        print(key * value)
my_words(words)

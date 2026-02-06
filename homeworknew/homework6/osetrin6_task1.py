text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer '
        'urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
fin_words = []
for word in words:
    if word.endswith(','):
        new_word = word[:-1] + 'ing' + word[-1]
    elif word.endswith('.'):
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    fin_words.append(new_word)
best_text = ' '.join(fin_words)
print(best_text)

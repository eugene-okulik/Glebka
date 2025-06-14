# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова, но уже преобразованного.

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
        "facilisis vitae semper at, dignissim vitae libero")
words = text.split()
result_worlds = []
for word in words:
    if word.endswith(".") or word.endswith(","):
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
        result_worlds.append(new_word)
new_text = "".join(result_worlds)
print(new_text)

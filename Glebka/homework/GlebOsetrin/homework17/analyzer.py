import os
import argparse

# запуск через консоль
# python Glebka/homework/GlebOsetrin/homework17/analyzer.py Glebka/homework/GlebOsetrin/homework17/logs --text ERROR

parser = argparse.ArgumentParser()

parser.add_argument("path", help="Path to file or folder")
parser.add_argument("--text", required=True, help="Text to search")

args = parser.parse_args()

path = args.path
search_text = args.text

files = []

if os.path.isfile(path):
    files.append(path)
else:
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks = {}

    current_time = ""
    current_text = ""

    for line in lines:
        if len(line) >= 19 and line[4] == "-" and line[7] == "-":
            if current_text:
                blocks[current_time] = current_text
            current_time = line[:19]
            current_text = line
        else:
            current_text += line

    if current_text:
        blocks[current_time] = current_text

    for time, text in blocks.items():
        if search_text.lower() in text.lower():
            words = text.split()

            for i, word in enumerate(words):
                if search_text.lower() in word.lower():
                    start = max(0, i - 5)
                    end = i + 6
                    context = " ".join(words[start:end])

                    print('=' * 50)
                    print('Файл:', file)
                    print('Время:', time)
                    print('Контекст:', context)
                    break

            break

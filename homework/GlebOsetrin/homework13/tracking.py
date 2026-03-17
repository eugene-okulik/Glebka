import os
import datetime

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')
print(file_path)


def read_file():
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for line in read_file():
    print(line.strip())


for line in read_file():
    line = line.split('. ', 1)[1]

    date_part, text = line.split(' - ')
    date_obj = datetime.datetime.strptime(date_part, '%Y-%m-%d %H:%M:%S.%f')

    if 'неделю позже' in text:
        result = date_obj + datetime.timedelta(days=7)
        print(result)

    elif 'день недели' in text:
        print(date_obj.strftime('%A'))

    elif 'сколько дней назад была эта дата' in text:
        now = datetime.datetime.now()
        diff = now - date_obj
        print(diff.days)

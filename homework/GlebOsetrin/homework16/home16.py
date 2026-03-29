import mysql.connector as mysql
import creds
import os
from dotenv import load_dotenv
import csv

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSW')
database = os.getenv('DB_NAME')

connection = mysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

base_dir = os.path.dirname(__file__)

file_path = os.path.join(
    base_dir,
    '..',
    '..',
    'eugene_okulik',
    'Lesson_16',
    'hw_data',
    'data.csv'
)

missing_creds = []

with open(file_path, newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print('Все строчки:', row)
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

cursor.execute("""
    SELECT COUNT(*)
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects sub ON l.subject_id = sub.id
    JOIN books b ON b.taken_by_student_id = s.id
    WHERE s.name=%s
      AND s.second_name=%s
      AND g.title=%s
      AND b.title=%s
      AND sub.title=%s
      AND l.title=%s
      AND m.value=%s
""", (
    name,
    second_name,
    group_title,
    book_title,
    subject_title,
    lesson_title,
    int(mark_value)
))

result = cursor.fetchone()[0]

if not result:
    missing_creds.append(row)

if missing_creds:
    print('Отсутствуют в базе:')
    for row in missing_creds:
        print(row)
else:
    print('Все данные в базе')

connection.close()

import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor()
cursor.execute(
    'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)',
    ('QATesters', '2026-03-01', '2027-04-01')
)
cursor.execute(
    'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)',
    ('QATesters', '2026-03-01', '2027-04-01')
)
db.commit()
group_id = cursor.lastrowid
print("group_id:", group_id)

cursor.execute(
    'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)',
    ('Dima', 'Mamkin', group_id)
)
db.commit()
student_id = cursor.lastrowid
print("student_id:", student_id)

books = ['QABest', 'Python best', 'Okulik best']
for book in books:
    cursor.execute(
        'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
        (book, student_id)
    )
db.commit()
subjects = ['Databases', 'Programming', 'Testing']
subject_ids = []

for subject in subjects:
    cursor.execute(
        'INSERT INTO subjects (title) VALUES (%s)',
        (subject,)
    )
    subject_ids.append(cursor.lastrowid)

db.commit()
print('subject_ids:', subject_ids)
lessons_map = {
    subject_ids[0]: ['INSERT', 'VALUES'],
    subject_ids[1]: ['Functions', 'tasks'],
    subject_ids[2]: ['test-cases', 'bugs']
}

lesson_ids = []

for subject_id, lessons in lessons_map.items():
    for lesson in lessons:
        cursor.execute(
            'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)',
            (lesson, subject_id)
        )
        lesson_ids.append(cursor.lastrowid)

db.commit()
print('lesson_ids:', lesson_ids)
marks = [5, 5, 4, 4, 5, 5]

for lesson_id, mark in zip(lesson_ids, marks):
    cursor.execute(
        'INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)',
        (student_id, lesson_id, mark)
    )

db.commit()
cursor.execute(
    'SELECT value FROM marks WHERE student_id = %s',
    (student_id,)
)
print('marks:', cursor.fetchall())
cursor.execute(
    'SELECT title FROM books WHERE taken_by_student_id = %s',
    (student_id,)
)
print('books:', cursor.fetchall())
cursor.execute("""
SELECT
s.name,
g.title group_name,
b.title book,
l.title lesson,
sub.title subject,
m.value mark
FROM students s
Left JOIN `groups` g ON g.id = s.group_id
Left JOIN books b ON b.taken_by_student_id = s.id
Left JOIN marks m ON m.student_id = s.id
Left JOIN lessons l ON l.id = m.lesson_id
Left JOIN subjects sub ON sub.id = l.subject_id
WHERE s.id = %s
""", (student_id,))
rows = cursor.fetchall()

print('FULL DATA:')

for name, group, book, lesson, subject, mark in rows:
    print(
        f'Name: {name}, Group: {group}, Book: {book}, '
        f'Lesson: {lesson}, Subject: {subject}, Mark: {mark}'
    )

db.close()

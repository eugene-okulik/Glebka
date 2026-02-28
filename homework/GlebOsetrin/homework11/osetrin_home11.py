class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


book1 = Book('Идиот', 'Достоевский', 640, '111-111', False)
book2 = Book('Война и мир', 'Толстой', 1640, '111-222', False)
book3 = Book('Мастер и маргарита', 'Булгаков', 540, '111-333', False)
book4 = Book('Гарри Поттер', 'Кэтлин', 840, '111-444', True)
book5 = Book('Властелин колец', 'Толкин', 1140, '111-555', False)


for book in [book1, book2, book3, book4, book5]:
    if book.reserved:
        print(
            f'Название книги: {book.title}, Автор: {book.author}, Всего страниц: {book.pages}, '
            f'Материал: {Book.page_material}, зарезервирована'
        )
    else:
        print(
            f'Название книги: {book.title}, Автор: {book.author}, Всего страниц: {book.pages},'
            f'Материал: {Book.page_material}'
        )


class SchoolBook(Book):
    school_subject = ['Математика', 'История', 'География']
    school_class = 9
    availability_task = True

    def __init__(self, title, author, pages, isbn, school_subject, school_class, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.school_subject = school_subject
        self.school_class = school_class


school_book1 = SchoolBook('Алгебра', 'Марткович', 333, 'Математика', 8, False)
school_book2 = SchoolBook('История', 'Геродот', 444, 'История', 7, True)
school_book3 = SchoolBook('География', 'Смирнова', 222, 'География', 9, False)


for book in [school_book1, school_book2, school_book3]:
    if book.reserved:
        print(
            f'Название книги: {book.title}, Автор: {book.author}, '
            f'Всего страниц: {book.pages}, '
            f'Предмет: {book.school_subject}, класс: {book.school_class}, '
            f'зарезервирована'
        )
    else:
        print(
            f'Название книги: {book.title}, Автор: {book.author}, '
            f'Всего страниц: {book.pages}, '
            f'Предмет: {book.school_subject}, класс: {book.school_class}'
        )

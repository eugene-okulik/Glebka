import datetime
my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
my_month = python_date.strftime('%B')
my_fulldate = python_date.strftime('%d.%m.%Y %H:%M')

print(my_month)
print(my_fulldate)

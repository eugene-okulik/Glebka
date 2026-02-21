PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

names = [line.split()[0] for line in PRICE_LIST.splitlines()]
prices = [int(line.split()[1][:-1]) for line in PRICE_LIST.splitlines()]

price_dict = dict(zip(names, prices))

print(price_dict)
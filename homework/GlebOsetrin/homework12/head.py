from flowers import Rose, Chrysanthemum, Gerbera, Lily
from bouquet import Bouquet

rose1 = Rose('red', 70)
rose2 = Rose('white', 70)
rose3 = Rose('pink', 70)
rose4 = Rose('yellow', 70)

Gerbera1 = Gerbera('red', 50)
Gerbera2 = Gerbera('orange', 50)

Chrysanthemum1 = Chrysanthemum('while', 50)
Chrysanthemum2 = Chrysanthemum('yellow', 50)

Lily1 = Lily('white', 50)
Lily2 = Lily('yellow', 50)

bouquet = Bouquet()

bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(rose3)
bouquet.add_flower(Lily1)
bouquet.add_flower(Chrysanthemum1)

print('Цветы в букете:')
print(bouquet.flowers)

print('Стоимость букета:')
print(bouquet.total_price())

print('Среднее время жизни:')
print(bouquet.life_time())

bouquet.sort_by_price()

print('Сортировка по цене:')
print(bouquet.flowers)

flowers = bouquet.find_by_life(7)

print('Цветы которые живут >= 7 дней:')
print(flowers)

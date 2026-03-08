class Flower:


    def __init__(self, name, color, price, life_days, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.life_days = life_days
        self.stem_length = stem_length


    def __str__(self):
        return f'{self.name} {self.color}'


class Rose(Flower):


    def __init__(self, color, stem_length):
        super().__init__('Rose', color, 400, 8, stem_length)


class Chrysanthemum(Flower):
    def __init__(self, color, stem_length):
        super().__init__('Chrysanthemum', color, 250, 10, stem_length)


class Gerbera(Flower):
    def __init__(self, color, stem_length):
        super().__init__('Gerbera', color, 200, 9, stem_length)


class Lily(Flower):
    def __init__(self, color, stem_length):
        super().__init__('Lily', color, 450, 12, stem_length)

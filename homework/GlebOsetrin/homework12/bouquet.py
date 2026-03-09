class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        total = 0

        for flower in self.flowers:
            total = total + flower.price
        return total

    def life_time(self):
        total = 0
        for flower in self.flowers:
            total = total + flower.life_days
        return total / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def find_by_life(self, days):
        result = []

        for flower in self.flowers:
            if flower.life_days >= days:
                result.append(flower)
        return result

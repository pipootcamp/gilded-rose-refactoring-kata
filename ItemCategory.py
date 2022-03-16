class ItemCategory():
    def __init__(self, item):
        pass

    @staticmethod
    def increase_quality(item):
        if item.quality < 50:
            item.quality = item.quality + 1

    @staticmethod
    def decrease_quality(item, i):
        if item.quality > 0:
            item.quality = item.quality - i

    @staticmethod
    def has_expired(sell_in):
        return sell_in < 0

    @staticmethod
    def is_concert_ticket(name):
        return name == "Backstage passes to a TAFKAL80ETC concert"

    @staticmethod
    def is_cheese(name):
        return name == "Aged Brie"

    @staticmethod
    def is_sulfuras(name):
        return name == "Sulfuras, Hand of Ragnaros"
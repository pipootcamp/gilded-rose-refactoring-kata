from ItemCategory import ItemCategory


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_category = ItemCategory(item)
            self.update_one_item(item)

    def update_one_item(self, item):
        self.update_item_quality(item)
        self.update_sell_in(item)
        if self.has_expired(item):
            self.update_expired(item)

    def update_expired(self, item):
        if self.is_cheese(item):
            self.increase_quality(item)
        elif self.is_concert_ticket(item):
            item.quality = 0
        elif self.is_sulfuras(item):
            return
        else:
            self.decrease_quality(item, 1)

    def update_sell_in(self, item):
        if self.is_sulfuras(item):
            return
        item.sell_in = item.sell_in - 1

    def update_item_quality(self, item):
        if self.is_cheese(item) or self.is_concert_ticket(item):
            self.update_cheese_and_ticket_quality(item)
        elif self.is_sulfuras(item):
            item.quality = 80
        elif "Conjured" in item.name:
            self.decrease_quality(item, 2)
        else:
            self.decrease_quality(item, 1)

    def update_cheese_and_ticket_quality(self, item):
        self.increase_quality(item)
        if self.is_concert_ticket(item):
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrease_quality(self, item, i):
        if item.quality > 0:
            item.quality = item.quality - i

    def has_expired(self, item):
        return item.sell_in < 0

    def is_concert_ticket(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_cheese(self, item):
        return item.name == "Aged Brie"

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



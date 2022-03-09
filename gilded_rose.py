# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_one_item(item)

    def update_one_item(self, item):
        self.update_item_quality(item)
        self.update_sell_in(item)
        if self.has_expired(item):
            self.update_expired(item)

    def has_expired(self, item):
        return item.sell_in < 0

    def update_expired(self, item):
        if self.is_cheese(item):
            if item.quality < 50:
                item.quality = item.quality + 1
        else:
            if self.is_concert_ticket(item):
                item.quality = item.quality - item.quality
            else:
                if item.quality > 0:
                    if self.is_sulfuras(item):
                        return
                    item.quality = item.quality - 1

    def update_sell_in(self, item):
        if self.is_sulfuras(item):
            return
        item.sell_in = item.sell_in - 1

    def update_item_quality(self, item):
        if self.is_cheese(item) or self.is_concert_ticket(item):
            self.update_cheese_and_ticket_quality(item)

        else:
            if item.quality > 0:
                if self.is_sulfuras(item):
                    item.quality = 80
                else:
                    if "Conjured" in item.name:
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1

    def update_cheese_and_ticket_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if self.is_concert_ticket(item):
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1

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

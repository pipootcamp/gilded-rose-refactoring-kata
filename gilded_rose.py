# -*- coding: utf-8 -*-
from ItemCategory import ItemCategory, decrease_quality, has_expired, is_concert_ticket, is_cheese, is_sulfuras


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_category = ItemCategory(item)
            self.update_one_item(item, item_category)

    def update_one_item(self, item, category):
        self.update_item_quality(item, category)
        self.update_sell_in(item, category)
        if has_expired(self.sell_in, item):
            self.update_expired(item, category)

    def update_expired(self, item, category):
        if is_cheese(self.name, item):
            self.increase_quality(item, category)
        elif is_concert_ticket(self.name, item):
            item.quality = 0
        elif is_sulfuras(self.name, item):
            return
        else:
            decrease_quality(item, category, 1)

    def update_sell_in(self, item, category):
        if is_sulfuras(self.name, item):
            return
        item.sell_in = item.sell_in - 1

    def update_item_quality(self, item, category):
        if is_cheese(self.name, item) or is_concert_ticket(self.name, item):
            self.update_cheese_and_ticket_quality(item)
        elif is_sulfuras(self.name, item):
            item.quality = 80
        elif "Conjured" in item.name:
            decrease_quality(item, 2, 1)
        else:
            decrease_quality(item, 1, 1)

    def update_cheese_and_ticket_quality(self, item):
        self.increase_quality(item)
        if is_concert_ticket(self.name, item):
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

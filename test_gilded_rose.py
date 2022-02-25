# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in(self):
        items = [Item("foo", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_quality(self):
        items = [Item("foo", 11, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sellpassed(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_agedbrie(self):
        items = [Item("Aged Brie", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)


    def test_maxquality(self):
        items = [Item("Aged Brie", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstagespasses(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_Conjureditems(self):
        items = [Item("Concert Conjured", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_Conjureditems2(self):
        items = [Item("Conjured Sword", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()

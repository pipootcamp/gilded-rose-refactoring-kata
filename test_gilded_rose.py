# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_should_decrease_sellin_by_one(self):
        items = [Item("foo", 7, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)

    def test_should_decrease_quality_by_one(self):
        items = [Item("foo", 7, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_should_decrease_double_if_sellin_lessthan_zero(self):
        items = [Item("foo", 0, 2)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_be_negative(self):
        items = [Item("foo", 4, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_agedbries_should_increase_quality(self):
        items =[Item("Aged Brie", 4, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_should_not_be_greater_than_50(self):
        items = [Item("Aged Brie", 7, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_should_not_decrease_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 7, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
    #@unittest.skip("porque jose dijo")
    def test_sulfuras_should_not_decrease_in_sellin(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)

    def test_backstage_passes_quality_increases_by_2_if_sell_in_less_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_quality_increases_by_3_if_sell_in_less_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_quality_decreases_to_0_if_sell_in_equals_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_items_degrade_double(self):
        items = [Item("Conjured cheese", 10, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    def test_sulfuras_quality_always_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()

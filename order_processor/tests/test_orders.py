import unittest

from order_processor.lib.order import Order
from order_processor.lib.chocolate import Chocolate


class TestOrders(unittest.TestCase):

    # High Level (Nearly) End to End Tests
    def test_get_string_output_milk(self):
        primary_chocolate = Chocolate("milk")
        order = Order(primary_chocolate, 12, 2, 5)
        self.assertEqual(order.get_string_output(), "milk 7,dark 0,white 0")

    def test_get_string_output_dark(self):
        primary_chocolate = Chocolate("dark")
        order = Order(primary_chocolate, 13, 4, 1)
        self.assertEqual(order.get_string_output(), "milk 0,dark 9,white 0")

    def test_get_string_output_white(self):
        primary_chocolate = Chocolate("white")
        order = Order(primary_chocolate, 6, 2, 2)
        self.assertEqual(order.get_string_output(), "milk 1,dark 0,white 4")

    def test_get_string_output_with_no_bonus(self):
        primary_chocolate = Chocolate("milk")
        order = Order(primary_chocolate, 12, 2, 100)
        self.assertEqual(order.get_string_output(), "milk 6,dark 0,white 0")


if __name__ == '__main__':
    unittest.main()

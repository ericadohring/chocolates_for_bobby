from order_processor.lib.chocolate import Chocolate
from order_processor.lib.chocolate_types import ChocolateTypes
from collections import Counter


class Order:

    def __init__(self, primary_chocolate, cash, price, bonus_ratio):
        self.primary_chocolate = primary_chocolate
        self.num_purchased_primary_chocolates = cash // price
        self.num_bonus_packs = self.num_purchased_primary_chocolates // bonus_ratio

    def get_string_output(self):
        order_info = self.primary_chocolate.get_bonus_info(
            self.num_bonus_packs)
        order_info[self.primary_chocolate.get_name(
        )] += self.num_purchased_primary_chocolates
        return(
            f'milk {order_info[ChocolateTypes.MILK.value]},'
            f'dark {order_info[ChocolateTypes.DARK.value]},'
            f'white {order_info[ChocolateTypes.WHITE.value]}')

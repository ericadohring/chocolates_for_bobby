import csv
from order_processor.lib.order import Order
from order_processor.lib.chocolate import Chocolate


def process_orders(input_file_path):
    try:
        with open(input_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                chocolate_type, cash, price, bonus_ratio = row["type"][1:-1], int(
                    row["cash"]), int(row["price"]), int(row["bonus_ratio"])
                primary_chocolate = Chocolate(chocolate_type)
                order = Order(primary_chocolate, cash, price, bonus_ratio)
                print(order.get_string_output())
    except FileNotFoundError as fnfe:
        print(f'Cannot find input file "{input_file_path}." Please try again.')

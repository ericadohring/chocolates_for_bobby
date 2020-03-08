import os

import sys
from order_processor.lib.order_processor import process_orders

if __name__ == '__main__':
    input_file_name = sys.argv[1:][0]
    process_orders(input_file_name)

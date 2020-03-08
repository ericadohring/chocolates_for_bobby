
from order_processor.lib.chocolate_types import ChocolateTypes
from collections import Counter

DARK = ChocolateTypes.DARK.value
MILK = ChocolateTypes.MILK.value
WHITE = ChocolateTypes.WHITE.value

# enum_list = list(map(int, Color))


class Chocolate:

    def __init__(self, chocolate_type,):
        self.chocolate_type = chocolate_type

    def get_bonus_info(self, num_bonus_packs):
        default_bonus_info = get_default_bonus_info()
        if num_bonus_packs == 0:
            return default_bonus_info
        if self.chocolate_type == MILK:
            return get_milk_bonus_info(default_bonus_info, num_bonus_packs)
        elif self.chocolate_type == DARK:
            return get_dark_bonus_info(default_bonus_info, num_bonus_packs)
        elif self.chocolate_type == WHITE:
            return get_white_bonus_info(default_bonus_info, num_bonus_packs)

    def get_name(self):
        return self.chocolate_type


def get_default_bonus_info():
    chocolate_types = ChocolateTypes.get_chocolate_types()
    generic_bonus_info = Counter()
    for chocolate_type in chocolate_types:
        generic_bonus_info[chocolate_type] = 0
    return generic_bonus_info


def get_milk_bonus_info(default_bonus_info, num_bonus_packs):
    default_bonus_info[MILK] = num_bonus_packs
    return default_bonus_info


def get_dark_bonus_info(default_bonus_info, num_bonus_packs):
    default_bonus_info[DARK] = 2 * num_bonus_packs
    return default_bonus_info


def get_white_bonus_info(default_bonus_info, num_bonus_packs):
    default_bonus_info[MILK] = num_bonus_packs
    default_bonus_info[WHITE] = num_bonus_packs
    return default_bonus_info

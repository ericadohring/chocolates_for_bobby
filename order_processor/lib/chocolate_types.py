from enum import Enum


class ChocolateTypes(Enum):
    DARK = "dark"
    MILK = "milk"
    WHITE = "white"

    @staticmethod
    def get_chocolate_types():
        return [chocolate_type.name for chocolate_type in ChocolateTypes]
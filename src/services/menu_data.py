# Req 3
from src.models.dish import Ingredient, Dish
from csv import DictReader


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as menu:
            data = DictReader(menu)
            for item in data:
                dish = Dish(item["dish"], float(item["price"]))

                if dish not in self.dishes:
                    self.dishes[dish] = dish

                self.dishes[dish].add_ingredient_dependency(
                    Ingredient(item["ingredient"]), int(item["recipe_amount"])
                )

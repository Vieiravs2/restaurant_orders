import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = []
        self.read_csv(source_path)

    def read_csv(self, source_path: str):
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            dish_created = {}

            for dish_name, dish_price, ing_name, ing_quantity in reader:
                dish_name, dish_price, ing_name, ing_quantity = map(
                    str.strip,
                    (dish_name, dish_price, ing_name, ing_quantity)
                )

                dish = dish_created.get(dish_name)
                if dish is None:
                    dish = Dish(dish_name, float(dish_price))
                    self.dishes.append(dish)
                    dish_created[dish_name] = dish

                ingredient = Ingredient(ing_name)
                dish.add_ingredient_dependency(ingredient, int(ing_quantity))
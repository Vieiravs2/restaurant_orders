from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    picanha = Dish("Picanha a Moda", 100.0)
    invalidPrice = 'Dish price must be float.'
    lowerOrEqualZero = 'Dish price must be greater then zero.'

    with pytest.raises(TypeError, match=invalidPrice):
        Dish("Invalid Dish", "Price being a text")

    with pytest.raises(ValueError, match=lowerOrEqualZero):
        Dish("Worthless dish", 0)

    assert picanha.name == "Picanha a Moda"
    assert picanha.price == 100.0

    assert picanha != Dish("Maminha a Moda", 80.0)
    assert picanha == Dish("Picanha a Moda", 100.0)

    assert hash(picanha) == hash(Dish("Picanha a Moda", 100.0))
    assert hash(picanha) != hash(Dish("Maminha a Moda", 80.0))

    assert repr(picanha) == "Dish('Picanha a Moda', R$100.00)"

    picanha.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    picanha.add_ingredient_dependency(Ingredient("carne"), 1)
    picanha.add_ingredient_dependency(Ingredient("queijo provolone"), 1)
    picanha.add_ingredient_dependency(Ingredient("ovo"), 1)

    assert len(picanha.recipe) == 4
    assert len(picanha.get_ingredients()) == 4
    assert len(picanha.get_restrictions()) == 3


from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    picanha = Dish("Picanha a Moda", 100.0)
    maminha = Dish("Maminha a Moda", 80.0)
    cheese = Ingredient("queijo mussarela")
    invalidPrice = 'Dish price must be float.'
    lowerOrEqualZero = 'Dish price must be greater then zero.'

    with pytest.raises(TypeError, match=invalidPrice):
        Dish("Invalid Dish", "ThisIsString")

    with pytest.raises(ValueError, match=lowerOrEqualZero):
        Dish("Prato sem valor", 0)

    assert picanha.name == "Picanha a Moda"
    assert picanha.price == 100.0

    assert maminha.name == "Maminha a Moda"
    assert maminha.price == 80.0

    assert picanha != maminha
    assert picanha == Dish("Picanha a Moda", 100.0)

    assert hash(picanha) == hash(Dish("Picanha a Moda", 100.0))
    assert hash(picanha) != hash(maminha)

    assert repr(picanha) == "Dish('Picanha a Moda', R$100.00)"

    picanha.add_ingredient_dependency(cheese, 2)

    assert len(picanha.recipe) == 1
    assert len(picanha.get_ingredients()) == 1
    assert len(picanha.get_restrictions()) == 2


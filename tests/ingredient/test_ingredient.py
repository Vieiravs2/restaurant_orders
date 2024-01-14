from src.models.ingredient import Ingredient
from src.models.ingredient import restriction_map


def test_ingredient():
    flour = Ingredient('farinha')
    bacon = Ingredient('bacon')
    cheese = Ingredient('queijo mussarela')

    assert flour == flour
    assert cheese != bacon

    assert bacon.name == 'bacon'
    assert hash(bacon) == hash('bacon')
    assert repr(bacon) == "Ingredient('bacon')"

    assert flour.name == 'farinha'
    assert hash(flour) == hash('farinha')
    assert repr(flour) == "Ingredient('farinha')"

    assert cheese.restrictions == restriction_map().get('queijo mussarela')
    assert flour.restrictions == restriction_map().get('farinha')
    assert bacon.restrictions == restriction_map().get('bacon')

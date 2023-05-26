from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("pizza", 46.50)
    dish2 = Dish("pasta bolgnese", 22.50)
    ing1 = Ingredient("farinha")

    assert dish1.name == "pizza"
    assert dish1.price == 46.50
    assert dish1.__hash__() == hash(dish1)

    assert dish1.name != "pitza"
    assert dish1.__hash__() != dish2.__hash__()
    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish2) is False
    assert dish1.__repr__() == "Dish('pizza', R$46.50)"

    dish1.add_ingredient_dependency(ing1, 1)

    assert dish1.get_restrictions() == {Restriction.GLUTEN}
    assert dish1.get_ingredients() == {ing1}

    with pytest.raises(TypeError):
        Dish(1123, "abc")

    with pytest.raises(ValueError):
        Dish("test", -1.5)

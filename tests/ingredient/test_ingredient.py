from src.models.ingredient import (
    Ingredient,
)  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    ing = Ingredient("farinha")
    sameIng = Ingredient("farinha")
    othering = Ingredient("bacon")

    assert ing.name == "farinha"
    assert ing.__eq__(sameIng)

    assert ing.__repr__() == "Ingredient('farinha')"
    assert ing.__hash__() == sameIng.__hash__()

    assert ing.restrictions.__eq__(Ingredient("farinha").restrictions)

    assert ing.__hash__() == othering.__hash__()

    with pytest.raises(AssertionError):
        assert ing.__hash__() == othering.__hash__()
        assert ing.__eq__(othering)

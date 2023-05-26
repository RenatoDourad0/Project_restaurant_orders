from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ing = Ingredient("farinha")
    sameIng = Ingredient("farinha")
    othering = Ingredient("bacon")

    assert ing.name == "farinha"
    assert ing.__repr__() == "Ingredient('farinha')"

    assert ing.__eq__(sameIng) is True
    assert ing.__eq__(othering) is False

    assert ing.__hash__() == sameIng.__hash__()
    assert ing.__hash__() != othering.__hash__()

    assert ing.restrictions == {Restriction.GLUTEN}

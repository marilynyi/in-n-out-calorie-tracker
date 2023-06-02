from project import burgerStyleValid, shakeFlavorValid, beverageSizeValid
import pytest


def test_burgerStyleValid():
    assert burgerStyleValid(1, "🍔 Hamburger", 1) == ("🍔 Hamburger", 390)
    assert burgerStyleValid(2, "🍔 Cheeseburger", 3) == ("🍔 Cheeseburger (Protein style)", 330)
    assert burgerStyleValid(3, "🍔 Double-Double", 2) == ("🍔 Double-Double (with mustard & ketchup)", 590)
    with pytest.raises(ValueError):
        assert burgerStyleValid(-1, -1, -1)
        assert burgerStyleValid(1, "🍔 Hamburger", -1)
        assert burgerStyleValid(1, "🍔 Hamburger", 0)

def test_shakeFlavorValid():
    assert shakeFlavorValid(1, "🍫 Chocolate Shake") == 580
    assert shakeFlavorValid(2, "🍦 Vanilla Shake") == 570
    assert shakeFlavorValid(3, "🍓 Strawberry Shake") == 590
    with pytest.raises(ValueError):
        assert shakeFlavorValid(-1, "🍫 Chocolate Shake")
        assert shakeFlavorValid(0, "🍫 Chocolate Shake")
        assert shakeFlavorValid(10, "🍓 Strawberry Shake")

def test_beverageSizeValid():
    assert beverageSizeValid(1, "🥤 Coca-Cola®", "s") == ("🥤 Coca-Cola® (Small)", 130)
    assert beverageSizeValid(2, "🥤 Diet Coke®", "m") == ("🥤 Diet Coke® (Medium)", 0)
    assert beverageSizeValid(4, "🥤 Dr Pepper®", "l") == ("🥤 Dr Pepper® (Large)", 260)
    assert beverageSizeValid(10, "🥤 Sweet Tea", "xl") == ("🥤 Sweet Tea (Extra Large)", 260)
    with pytest.raises(ValueError):
        assert beverageSizeValid(-1, -1, -1)
        assert beverageSizeValid(4, "🥤 Dr Pepper®", " l ")
        assert beverageSizeValid(2, "🥤 Coca-Cola®", "s")
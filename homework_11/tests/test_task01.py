from task01.task01 import SimplifiedEnum


class FigureEnum:
    __keys = ("SQUARE", "CIRCLE", "TRIANGLE", "SPHERE")


class FurnitureEnum:
    __keys = ("SOFA", "TABLE", "CHAIR")


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_not_using_metaclass():
    assert not hasattr(FigureEnum, "CIRCLE")
    assert not hasattr(FurnitureEnum, "SOFA")


def test_using_metaclass():
    assert ColorsEnum.RED == "RED"
    assert hasattr(SizesEnum, "XL")

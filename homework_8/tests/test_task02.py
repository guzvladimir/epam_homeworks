import pytest
from task02.task02 import TableData


@pytest.fixture()
def presidents():
    return TableData(
        database_name="example.sqlite",
        table_name="presidents",
    )


def test_len(presidents):
    assert len(presidents) == 3


def test_getitem(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains(presidents):
    assert ("Yeltsin" in presidents) == True
    assert ("Putin" in presidents) == False


def test_iter(presidents):
    names = [president[0] for president in presidents]
    countries = [president[2] for president in presidents]
    assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
    assert countries == ["Russia", "US", "Kekistan"]

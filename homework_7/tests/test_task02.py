from task02.task02 import backspace_compare


def test_backspace_compare_positive():
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")
    assert backspace_compare("1bc#y##x", "#112#p##x")
    assert backspace_compare("", "a#")


def test_backspace_compare_negative():
    assert not backspace_compare("a#c", "b")
    assert not backspace_compare("qwerty##", "qwer#ty#")
    assert not backspace_compare("12##3#4", "1")

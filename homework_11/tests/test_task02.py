from task02.task02 import ElderDiscount, MorningDiscount, Order


def test_order_without_discount():
    order_without_discount = Order(100)
    assert order_without_discount.final_price() == 100


def test_order_morning_discount():
    order_morning_discount = Order(100, MorningDiscount)
    assert order_morning_discount.final_price() == 50


def test_order_elder_discount():
    order_elder_discount = Order(100, ElderDiscount)
    assert order_elder_discount.final_price() == 10

"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def discount_price(self, order: Order) -> float:
        pass


class NoDiscount(BaseStrategy):
    def discount_price(order: Order) -> float:
        return 0


class MorningDiscount(BaseStrategy):
    def discount_price(order: Order) -> float:
        return order.price * 0.5


class ElderDiscount(BaseStrategy):
    def discount_price(order: Order) -> float:
        return order.price * 0.9


class Order:
    def __init__(self, price: float, discount_strategy: BaseStrategy = NoDiscount):
        self.price = price
        self._discount_strategy = discount_strategy

    @property
    def discount_strategy(self) -> BaseStrategy:
        return self._discount_strategy

    @discount_strategy.setter
    def discount_strategy(self, discount_strategy: BaseStrategy):
        self._discount_strategy = discount_strategy

    def final_price(self) -> float:
        return self.price - self._discount_strategy.discount_price(self)

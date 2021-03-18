# pylint: skip-file
from abc import ABC, abstractmethod
from enum import Enum, unique


@unique
class PizzaType(Enum):
    CHEESE = 'cheese'
    VEG = 'veg'


class Pizza:

    @abstractmethod
    def prepare(self):
        raise NotImplementedError()

    def bake(self):
        print('baking the pizza')

    def cut(self):
        print('cutting pizza into slices')

    def box(self):
        print('boxing the pizza')


class NewyorkCheesePizza(Pizza):

    def prepare(self):
        print('preparing newyork cheese pizza')


class ChicagoCheesePizza(Pizza):

    def prepare(self):
        print('preparing chicago cheese pizza')


class NewyorkVegPizza(Pizza):
    def prepare(self):
        print('preparing newyork veg pizza')


class ChicagoVegPizza(Pizza):
    def prepare(self):
        print('preparing chicago veg pizza')


class PizzaStore:

    @abstractmethod
    def _create(self, pizza_type):
        raise NotImplementedError()

    def order(self, pizza_type):
        p = self._create(pizza_type)
        p.prepare()
        p.bake()
        p.cut()
        p.box()
        return p


class NewyorkPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == PizzaType.CHEESE:
            return NewyorkCheesePizza()
        elif pizza_type == PizzaType.VEG:
            return NewyorkVegPizza()


class ChicagoPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == PizzaType.CHEESE:
            return ChicagoCheesePizza()
        elif pizza_type == PizzaType.VEG:
            return ChicagoVegPizza()


ps = ChicagoPizzaStore()
ps.order(PizzaType.CHEESE)

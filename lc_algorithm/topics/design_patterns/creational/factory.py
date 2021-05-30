# pylint: skip-file
from abc import ABC, abstractmethod
from enum import Enum, unique


@unique
class PizzaType(Enum):
    CHEESE = 'cheese'
    VEG = 'veg'


class PizzaMaker:

    @abstractmethod
    def prepare(self):
        raise NotImplementedError()

    def bake(self):
        print('baking the pizza')

    def cut(self):
        print('cutting pizza into slices')

    def box(self):
        print('boxing the pizza')


class NewyorkCheesePizzaMaker(PizzaMaker):

    def prepare(self):
        print('preparing newyork cheese pizza')


class ChicagoCheesePizzaMaker(PizzaMaker):

    def prepare(self):
        print('preparing chicago cheese pizza')


class NewyorkVegPizzaMaker(PizzaMaker):
    def prepare(self):
        print('preparing newyork veg pizza')


class ChicagoVegPizzaMaker(PizzaMaker):
    def prepare(self):
        print('preparing chicago veg pizza')


class PizzaStore:
    """ Pizza Factory """
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
            return NewyorkCheesePizzaMaker()
        elif pizza_type == PizzaType.VEG:
            return NewyorkVegPizzaMaker()


class ChicagoPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == PizzaType.CHEESE:
            return ChicagoCheesePizzaMaker()
        elif pizza_type == PizzaType.VEG:
            return ChicagoVegPizzaMaker()


ps = ChicagoPizzaStore()
ps.order(PizzaType.CHEESE)

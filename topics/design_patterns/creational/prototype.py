"""
Prototype pattern involves creating new objects by copying existing objects.
The object whose copies are made is called the prototype.

1. cloning instead of the creating a new object if creating a expensive.
2. removes the need of creating a subclasses.
"""
from abc import ABC, abstractmethod
from copy import deepcopy


class Engine:
    pass


class F16Engine(Engine):
    pass


class F16TurboEngine(Engine):
    pass


class AircraftPrototype(ABC):

    @abstractmethod
    def clone(self):
        """
        Abstract clone method.
        """


class F16(AircraftPrototype):

    def __init__(self):
        self.__engine = F16Engine()

    def clone(self):
        return deepcopy(self)

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine


class AircraftFactory:

    def clone(self, aircraft):
        return aircraft.clone()


f = AircraftFactory()
f16 = F16()
f16_clone = f.clone(f16)
f16_clone.engine = F16TurboEngine()
import pdb
pdb.set_trace()
f16_clone = f.clone(f16)
import pdb
pdb.set_trace()

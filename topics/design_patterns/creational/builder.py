"""
builder pattern encapsulates or hides the process of building
a complex object and separates the representation of the object
and its construction. The separation allows us to construct
different representations using the same construction process

1. Build complex objects step by step
2. Hides the complexity of the building process.
3. Separates the representation and construction of the object.

The class diagram consists of the following entities

* Builder
* Concrete Builder
* Director
* Product

https://refactoring.guru/design-patterns/builder
"""

from abc import ABC, abstractmethod


class Engine:
    pass


class Wing:
    pass


class F16Engine(Engine):
    pass


class BoeingEngine(Engine):
    pass


class F16Wing(Wing):
    pass


class BoeingWing(Wing):
    pass


class F16:
    pass


class Boeing:
    @property
    def engine(self, value):
        self.engine = value

    @property
    def wing(self, value):
        self.wing = value


class AircraftBuilder(ABC):

    @abstractmethod
    def build_engine(self):
        """
        Abstract engine build method.
        """

    @abstractmethod
    def build_wings(self):
        """
        Abstract wing build method.
        """

    # @abstractmethod
    # def build_cockpit(self):
    #     """
    #     Abstract cockpit build method.
    #     """

    # @abstractmethod
    # def build_bathroom(self):
    #     """
    #     Abstract bathroom build method.
    #     """

    @abstractmethod
    def get_result(self):
        """
        Abstract method to get the build aircraft.
        """


class F16Builder(AircraftBuilder):

    def __init__(self):
        self.f16 = F16()

    def build_engine(self):
        self.f16.engine = F16Engine()

    def build_wings(self):
        self.f16.wing = F16Wing()

    def get_result(self):
        return self.f16


class BoeingBuilder(AircraftBuilder):

    def __init__(self):
        self.boeing = Boeing()

    def build_engine(self):
        self.boeing.engine = BoeingEngine()

    def build_wings(self):
        self.boeing.wing = BoeingWing()

    def get_result(self):
        return self.boeing


class Director:

    def __init__(self, builder: AircraftBuilder):
        self.builder = builder

    def construct(self):
        self.builder.build_engine()
        self.builder.build_wings()


class Client:
    def make_aircraft(self):
        builder = F16Builder()
        director = Director(builder)
        director.construct()
        f16_aircraft = builder.get_result()
        return f16_aircraft


c = Client()
a = c.make_aircraft()
import pdb
pdb.set_trace()

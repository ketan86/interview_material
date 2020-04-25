"""
Singleton is a creational design pattern that lets you ensure that a class has
only one instance, while providing a global access point to this instance.


1. ** Violates ** the single responsibility principle due to multiple
   functionality.
     - Ensure that a class has just a single instance
     - Provide a global access point to that instance
"""


class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance:
            raise Exception('class instance exist, use `get_instance` instead')
        Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

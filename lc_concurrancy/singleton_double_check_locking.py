
import threading
import concurrent.futures
from typing import Type

class SingletonMixin:
    """Mixin class to make your class a Singleton class.

    Steps:
        1. Define  `instance`(classmethod) and `__new__` method.
           - calling `instance` method allows us to create a new instance.
           - implement `__new__` method to restrict the creation of the
             singleton instance directly.
           - only allow `instance` method to access the `__new__` method one
             time while creating an single instance.

        2. In `instance` method,
           - if instance is already created, return
           - if not, take rlock and check if instance is created or not
             **** this is called double checking to avoid waiting threads
                  to create instance if they had passed instace absence
                  check and enters critical section when first thread
                  completes the instance creation.
           - if not instance created so far, create a new instance by calling
             `cls(*args, **kwargs)` method. It calls `__new__` internally to
             create a new class instance.

    """

    _instance = None
    _rlock = threading.RLock()
    _inside_instance = False

    @classmethod
    def instance(cls, *args, **kwargs):
        """Get *the* instance of the class, constructed when needed using (kw)args.

        Return the instance of the class. If it did not yet exist, create it
        by calling the "constructor" with whatever arguments and keyword arguments
        provided.

        This routine is thread-safe. It uses the *double-checked locking* design
        pattern ``https://en.wikipedia.org/wiki/Double-checked_locking``_ for this.

        :param args: Used for constructing the instance, when not performed yet.
        :param kwargs: Used for constructing the instance, when not performed yet.
        :return: An instance of the class
        """
        thread_name = threading.current_thread()
        print(f'trying to create the instance {thread_name}')
        if cls._instance is not None:
            print(f'instance is already found {cls._instance}, {thread_name}')
            return cls._instance
        with cls._rlock:
            print(f'rlocked the instance creation {thread_name}')
            # re-check, perhaps it was created in the mean time...
            if cls._instance is None:
                print(f'inside the instance creation {thread_name}')
                cls._inside_instance = True
                try:
                    cls._instance = cls(*args, **kwargs)
                    print(f'created a new instance {thread_name}')
                finally:
                    cls._inside_instance = False
        return cls._instance

    def __new__(cls, *args, **kwargs):
        """Raise Exception when not called from the :func:``instance``_ class method.

        This method raises RuntimeError when not called from the instance class method.

        :param args: Arguments eventually passed to :func:``__init__``_.
        :param kwargs: Keyword arguments eventually passed to :func:``__init__``_
        :return: the created instance.
        """
        thread_name = threading.current_thread()

        if cls is SingletonMixin:
            raise TypeError(f"Attempt to instantiate mixin class {cls.__qualname__}")

        # NOTE: direct instance creation using `Singleton()` would enter
        # this section but fails to validate that it was called from the
        # `instance` classmethod.

        if cls._instance is None:
            print(f'instance is not found {thread_name}')
            with cls._rlock:
                print(f'got a lock {thread_name}')
                if cls._instance is None and cls._inside_instance:
                    print(f'instance was not found. created {thread_name}')
                    return super().__new__(cls, *args, **kwargs)

        raise RuntimeError(
            f"Attempt to create a {cls.__qualname__} instance outside of instance()"
        )




class ConfigSingleton(SingletonMixin):
    pass
ConfigSingleton.instance()

futures = []
with concurrent.futures.ThreadPoolExecutor(100) as executor:
    for i in range(200):
        future = executor.submit(ConfigSingleton.instance)
        futures.append(future)
    
for f in futures:
    print(f.result())

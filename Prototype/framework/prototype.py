from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def createClone(self):
        pass

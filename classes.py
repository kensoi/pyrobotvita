"""
Объекты расположены здесь
"""

from abc import ABC, abstractmethod


class Robot:
    def __init__(self, code: str, name:str)->None:
        self.code = code
        self.name = name


class Building(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.floors = 1


class House(Building):
    def __init__(self, floors:int = 1) -> None:
        super().__init__()
        self.floors = floors


class Barn(Building):
    def __init__(self) -> None:
        super().__init__()
"""
Обучения технологии постройки зданий
"""

from classes import Robot, House, Barn


def learn_build_home(robot: Robot)->Robot:
    """
    Научить робота строить дом
    """

    def build_home(self)->None:
        """
        Построить дом
        """
        print(f"{self.name} только что построил дом!")
        return House()

    robot.build_home = build_home


def learn_build_barn(robot: Robot)->None:
    """
    Научить робота строить сарай
    """
    
    def build_barn(self)->None:
        """
        Построить сарай
        """
        print(f"{self.name} только что построил сарай!")
        return Barn()

    robot.build_barn = build_barn

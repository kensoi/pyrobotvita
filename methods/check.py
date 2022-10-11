"""
Проверка способностей робота
"""

from classes import Robot


def check_skills(robot:Robot)->None:
    """
    Проверка способностей робота
    """

    print(f"Проверка способностей у робота \"{robot.name}\":")
    print(f"build_home: {hasattr(robot, 'build_home')}")
    print(f"build_barn: {hasattr(robot, 'build_barn')}")
    print(f"add_floor: {hasattr(robot, 'add_floor')}")
    print(f"remove_floor: {hasattr(robot, 'remove_floor')}")
    print()
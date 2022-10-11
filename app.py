from classes import Robot
from methods.check import check_skills
from methods.build import learn_build_barn, learn_build_home
from methods.floor_count import learn_add_floor, learn_remove_floor


def main():
    print("Создаём робота...\n")

    # Первичное создание робота и проверка его способностей
    
    robot = Robot("АА001221-56", "В") 

    check_skills(robot) # проверка способностей

    # Первое обучение робота

    print("Обучаем робота...\n")

    learn_build_home(robot) # робот учится строить дома
    learn_build_barn(robot) # робот учится строить сараи

    robot.name = "Вита"

    check_skills(robot) # проверка способностей

    # Второе обучение робота
    
    print("Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n")

    learn_add_floor(robot) # робот учится строить дополнительный этаж к дому
    learn_remove_floor(robot) # робот учится сносить 1 этаж у дома

    robot.name = "Виталий"

    check_skills(robot) # проверка способностей


if __name__ == "__main__":
    main()
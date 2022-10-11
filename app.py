from classes import Robot
from methods.check import check_skills
from methods.build import learn_build_barn, learn_build_home
from methods.floor_count import learn_add_floor, learn_remove_floor

def main():
    print("Создаём робота...\n")
    robot = Robot("АА001221-56", "В") # Первичное создание робота
    check_skills(robot)

    print("Обучаем робота...\n")
    learn_build_home(robot)
    learn_build_barn(robot)
    robot.name = "Вита"
    check_skills(robot)

    print("Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n")
    learn_add_floor(robot)
    learn_remove_floor(robot)
    robot.name = "Виталий"
    check_skills(robot)

if __name__ == "__main__":
    main()
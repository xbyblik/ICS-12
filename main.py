""" головний модуль задачі
- виводить розрахункову таблицю на екран та в файл
- виводить первинні данні на екран
"""

# Импортируем нужные модули
import os
from process_data import get_analytics
from data_service import show_movement_fixed_assets, show_help_types_fixed_assets, get_movement_fixed_assets, get_help_types_fixed_assets

# Задаем размер консоли
# Для того чтобы влазил весь даваемый контент
os.system("mode 54,10")


MAIN_MENU = \
"""
~~~~~~~~~~~  ОБРОБКА РУХУ ОСНОВНИХ ЗАСОБІВ ~~~~~~~~~~~

1 - Вивід аналіз руху основних засобів
2 - Запис аналіз руху основних засобів в файл
3 - Вивід рух основних засобів
4 - вивід довідника видів основних засобів
0 - завершення роботи
------------------------------------------------------
"""

STOP_MESSAGE = '\nДля продовження натисніть <Enter>'

# Сохраняем третью таблицу (Аналитику) в файл "./data/Result.txt"
def save_analytics(analytics):

        with open("./data/result.txt", "w", encoding="utf-8") as file:
            for analytic in analytics:
                line = \
                    analytic['enterprise']                      + ';' + \
                    analytic['type_fixed_assets']               + ';' + \
                    str(analytic['Remainder_01/01/18'])         + ';' + \
                    str(analytic['Received_2018'])              + ';' + \
                    str(analytic['Released_2018'])              + ';' + \
                    str(analytic['Balance_01/01/19'])           + ';' + \
                    str(analytic['Changes_cost_in_year'])       + '\n'

                file.write(line)
            print("------------- Сохранение прошло успешно. -------------")
# Функция вывода третей таблицы (Аналитики)
def showAnalytics():

    TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"

    HEADER = \
"""
================================================================================================================================================================
  Підприємтсво  |   Вид основних засобів    |   Залишок на 1.01.18  |   Надійшло у 2018 |   Вибуло у 2018   |   Залишок на 1.01.19  |   Зміни вартості за рік
================================================================================================================================================================
"""

    FOOTER = \
'''
================================================================================================================================================================
'''

    analytics = get_analytics()

    print(TITLE)
    print(HEADER)

    for analytic in analytics:
        print(
            f"{analytic['enterprise']:19}",
            f"{analytic['type_fixed_assets']:27}",
            f"{analytic['Remainder_01/01/18']:>18}",
            f"{analytic['Received_2018']:>20}",
            f"{analytic['Released_2018']:>17}",
            f"{analytic['Balance_01/01/19']:>24}",
            f"{analytic['Changes_cost_in_year']:>26}"

        )
    print(FOOTER)
# Функция вывода первой таблицы
def showMovements():
    TITLE = "Рух основних засобів"

    HEADER = \
"""
================================================================================================================
  Підприємтсво  |   Код виду основних засобів    |   Залишок на 1.01.18  |   Надійшло у 2018 |   Вибуло у 2018
================================================================================================================
"""
    FOOTER = \
'''
================================================================================================================
'''
    movements = get_movement_fixed_assets()

    print(TITLE)
    print(HEADER)

    for movement in movements:
        print(
            f"{movement[0]:<43}",
            f"{movement[1]:<18}",
            f"{movement[2]:<20}",
            f"{movement[3]:<20}",
            f"{movement[4]}"
        )

    print(FOOTER)
# Функция вывода второй таблицы
def showDirectory():
    TITLE = "Довідник видів основних засобів"

    HEADER = \
"""
==========================================================
  Код виду основних засобів  |   Вид основних засобів
==========================================================
"""
    FOOTER = \
'''
==========================================================
'''
    directorys = get_help_types_fixed_assets()

    print(TITLE)
    print(HEADER)

    for directory in directorys:
        print(
            f"{directory[0]:32}",
            f"{directory[1]}"
        )

    print(FOOTER)

# Делаем цикл для выбора действия пользователем
while True:

    # Очищаем консоль от мусора и прошлых операций
    os.system("cls")
    # Выводим главное меню
    print(MAIN_MENU)
    # Даем пользователю выбор команды для обработки
    command = input("Введіть номер команди: ")

    # Обработка команд пользователя
    if command == "0":
        os.system("cls")
        os.system("mode 60,10")
        print("\nПрограма завершила роботу.")
        exit(0)
    elif command == "1":
        # Очищаем консоль от мусора и прошлых операций
        os.system("cls")
        os.system("mode 160,20")
        showAnalytics()
        input('\n' + STOP_MESSAGE)
    elif command == "2":
        os.system("cls")
        analytics = get_analytics()
        save_analytics(analytics)
        input(STOP_MESSAGE)
    elif command == "3":
        os.system("mode 112,20")
        showMovements()
        input(STOP_MESSAGE)
    elif command == "4":
        os.system("mode 58,15")
        showDirectory()
        input(STOP_MESSAGE)

    # В случае некорректно заданного значения выводим ошибку и завершаем процесс работы.
    else:
        os.system("cls")
        os.system("mode 62,10")
        input("\nНекоректний номер команди, для продовження натисніть <Enter>")

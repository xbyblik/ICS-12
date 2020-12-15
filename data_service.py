""" Модуль для работы с файлами первичных данных
- считывание и вывод на экран
"""


def get_movement_fixed_assets():
    """ Получаем список основного движения средств полученного из файла 'dovidka.txt'

    Returns:
        array_assets: Список основного движения средств
    """
    with open("./data/dovidka.txt") as fixed_assets:
        from_file = fixed_assets.readlines()

    # Сборник движения средств
    array_assets = []

    # Разбиваем строки из полученного файла в массив
    for line in from_file:
        line = line[:-2]
        line_list = line.split(';')
        array_assets.append(line_list)

    # Выводим отформатированный файл
    return array_assets

def show_movement_fixed_assets(fixed_assets):
    """ Выводим на экран список основного движения средств в заданном диапазоне

    Returns:
        fixed_assets([list]): Список основного движения средств
    """

    fixed_assets_code_from = input("З якого коду засобів?\n")
    fixed_assets_code_to   = input("По який?\n")

    for fixed_asset in fixed_assets:
        if fixed_assets_code_from < fixed_asset[1] < fixed_assets_code_to:
            print("Підприємство: {:18}| Код виду основних засобів: {:2}| Залишок на 1.01.2018: {:21}| Надійшло у 2018: {:21}| Вибуток у 2018: {:21}".format( fixed_asset[0], fixed_asset[1], fixed_asset[2], fixed_asset[3], fixed_asset[4]))

def get_help_types_fixed_assets():
    """ Получаем список справки видов основных средств из файла 'dovidka2.txt'

    Returns:
        array_assets: Список справки вида основных средств
    """
    with open("./data/dovidka2.txt") as fixed_assets:
        from_file = fixed_assets.readlines()

    # Сборник движения средств
    array_assets = []

    # Разбиваем строки из полученного файла в массив
    for line in from_file:
        line = line[0:-1]
        line_list = line.split(';')
        array_assets.append(line_list)

    # Выводим отформатированный файл
    return array_assets

def show_help_types_fixed_assets(help_types_fixed_assets):
    """ Выводим на экран список справки вида основных средств в заданном диапазоне

    Returns:
        types_fixed_assets([list]): Список справки основного вида средств
    """

    help_types_fixed_assets_code_from = input("З якого коду засобів?\n")
    help_types_fixed_assets_code_to   = input("По який?\n")

    for help_types_fixed_asset in help_types_fixed_assets:
        if help_types_fixed_assets_code_from < help_types_fixed_asset[1] < help_types_fixed_assets_code_to:
            print("Код виду основних засобів: {:6}| Вид основних засобів: {:2}".format( help_types_fixed_asset[0], help_types_fixed_asset[1]))

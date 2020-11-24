""" Делаем аналитику основого движения средств
"""

from data_service import get_movement_fixed_assets, get_help_types_fixed_assets

# Шаблон для заполнения таблицы "Анализа движения основных средств"
temp_analysis_move_fixed_assets = {
    'enterprise'            : '',   # Підприємтсво
    'type_fixed_assets'     : '',    # Вид основних засобів
    'Remainder_01/01/18'    : 0,    # Залишок на 1.01.18
    'Received_2018'         : 0,    # Надійшло у 2018
    'Released_2018'         : 0,    # Вибуло у 2018
    'Balance_01/01/19'      : 0,    # Залишок на 1.01.19
    'Changes_cost_in_year'  : 0     # Зміни вартості за рік
}

def get_analytics():
    """ Делаем и возвращаем пользователю аналитику движения  средств

    Returns:
        analytics_list: Список движения средств
    """

    def get_type_funds(code):
        """ Делаем и возвращаем пользователю аналитику движения  средств

        Args:
            type_fixed_assets([code]): Код вида основных средств

        Returns:
            [type]: Название вида средств
        """
        for types_asset in types_assets:
            if types_asset[0] == code:
                return types_asset[1]

        return "Вид стредств не найден!"


    # Массив с конечной информацией
    analytics_list = []

    # Получаем информацию с двух таблиц
    types_assets    = get_help_types_fixed_assets()
    movement_assets = get_movement_fixed_assets()

    for movement_asset in movement_assets:

        # Создаем шаблон заполняемой строки
        temp = temp_analysis_move_fixed_assets.copy()

        temp["enterprise"]           = movement_asset[0]
        temp["type_fixed_assets"]    = get_type_funds(movement_asset[1])
        temp["Remainder_01/01/18"]   = movement_asset[2].split(",")[0]
        temp["Received_2018"]        = movement_asset[3].split(",")[0]
        temp["Released_2018"]        = movement_asset[4].split(",")[0]
        temp["Balance_01/01/19"]     = int(temp["Remainder_01/01/18"]) + int(temp["Received_2018"]) - int(temp["Released_2018"])
        temp["Changes_cost_in_year"] = int(temp["Balance_01/01/19"]) - int(temp["Remainder_01/01/18"])

        analytics_list.append(temp)


    return analytics_list

ggwp = get_analytics()
for ggw in ggwp:
    print(ggw)

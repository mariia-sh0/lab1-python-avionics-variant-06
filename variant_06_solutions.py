"""
Лабораторна робота: Варіант 6
Студент: [Шокур Марія]
Група: [1]
"""

# Задача 1: Вибір джерела навігації (if/elif/else)
def select_nav_source(gps_avail: bool, gps_acc: float, ins_calib: bool) -> str:
    """
    - gps_avail та gps_acc < 5.0 -> "GPS"
    - ins_calib -> "INS"
    - інакше -> "Star Tracker"
    """
    if gps_avail and gps_acc < 5.0:
        selected_nav_source = "GPS"
    elif ins_calib:
        selected_nav_source = "INS"
    else:
        selected_nav_source = "Star Tracker"
    print("Результат задачі №1")
    print(f'Обране джерело навігаційних даних: {selected_nav_source}')
    return selected_nav_source

#Можливий приклад даних для перевірки коду
select_nav_source(gps_avail=True, gps_acc=3.2, ins_calib=False)

# Задача 2: Аналіз температурних зон супутника (match-case)
def check_temp_zone(zone_data: list) -> str:
    """
    Приймає [zone_name, [t1, t2, t3]].
    - zone_name == "ENGINE" та середнє(t1,t2,t3) > 100 -> "Перегрів двигуна"
    - будь-яка інша зона -> "Зона {zone_name} в нормі"
    """
    match zone_data:
        case ["ENGINE",[t1, t2, t3]] if (t1+t2+t3) / 3 > 100:
            return "Перегрів двигуна"
        case [zone_name, _ ]:
            return f"Зона {zone_name} в нормі"
        case _:
            return f"Помилка y форматі даних"     
#Приклади вхідних даних для перевірки
print("Результат задачі №2")
print(check_temp_zone(zone_data = ["ENGINE", [95, 125, 100]]))
# print(check_temp_zone(zone_data = ["NOT_ENGINE", [70, 100, 100]]))


# Задача 3: Пошук подолання швидкості звуку (for / break)
def find_supersonic_second(speeds: list) -> int | None:
    """
    За допомогою циклу for знаходить першу секунду (індекс), коли швидкість > 340 м/с,
    і перериває цикл за допомогою break.
    """
    ...

# Задача 4: Зменшення частоти дискретизації (range)
def downsample_telemetry(data: list) -> list:
    """
    За допомогою range з кроком 3 відбирає кожен 3-й елемент списку data.
    """
    ...

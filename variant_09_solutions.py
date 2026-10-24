# lab1-python-avionics-variant-9
"""
Лабораторна робота: Варіант 9
Студент: Панков Максим
Група: номер 2
"""

# Задача 1: Пріоритет команд авіоніки (dict.get)
def get_command_priority(cmd_code: str) -> str:
    """
    Шукає код команди у словнику пріоритетів.
    За допомогою методу .get() повертає "Невідома команда: пріоритет 0", якщо код відсутній.
    """
    ...

# Задача 2: Вектор тяги двигунів (match-case)
def decode_thrust_vector(data: tuple) -> str:
    """
    Приймає (engine_id, pitch_angle, yaw_angle).
    - pitch == 0, yaw == 0 -> "Двигун {id}: Тяга за осі умовної нейтралі"
    - engine_id in (1, 2) -> "Основний двигун {id} у маневрі (p={pitch}, y={yaw})"
    """
    ...

# Задача 3: Гальмування в атмосфері Марса (while / break)
def simulate_mars_entry(v0: float) -> tuple:
    """
    У циклі while зменшує швидкість на 8% щосекунди.
    Працює до v <= 100 м/с або break при t > 120 с.
    Повертає кортеж (кінцева_швидкість, час_t).
    """
    t=0
    while True:
        v0=v0*0.92
        t+=1
        if v0<=100 or t>120:
            break
    return v0,t

# Задача 4: Інтегрування потужності (zip)
def calculate_consumed_energy(i_list: list, u_list: list, dt: float = 0.1) -> float:
    """
    Обчислює повну спожиту енергію P = sum(I_i * U_i) * dt за допомогою zip.
    """
    ...
v0=5000
print(simulate_mars_entry(v0))
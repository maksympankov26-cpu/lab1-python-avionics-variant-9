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
    branch=dict(autopilot=1, engine_shutdown=2,display_turn_on=3)
    branch.get(cmd_code,"Невідома команда: пріоритет 0")
    if isinstance(branch.get(cmd_code,"Невідома команда: пріоритет 0"),int):
        return f'{cmd_code}: пріоритет {branch.get(cmd_code,"Невідома команда: пріоритет 0")}'
    return branch.get(cmd_code,"Невідома команда: пріоритет 0")
# Задача 2: Вектор тяги двигунів (match-case)
def decode_thrust_vector(data: tuple) -> str:
    """
    Приймає (engine_id, pitch_angle, yaw_angle).
    - pitch == 0, yaw == 0 -> "Двигун {id}: Тяга за осі умовної нейтралі"
    - engine_id in (1, 2) -> "Основний двигун {id} у маневрі (p={pitch}, y={yaw})"
    """
    match data:
        case (engine_id, 0,0):
            return f"Двигун {engine_id}: Тяга за осі умовної нейтралі"
        case (1|2 as engine_id, pitch_angle, yaw_angle):
            return f"Основний двигун {engine_id} у маневрі (p={pitch_angle}, y={yaw_angle})"
        case (engine_id,pitch_angle,yaw_angle):
            return f"Двигун {engine_id} у маневрі (p={pitch_angle}, y={yaw_angle})"
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
    P=0
    for I, U in zip(i_list, u_list):
        print(I,U)
        P=P+I*U*dt
        print(P)
    return P
cmd_code=input('Введіть назву команди:')
print(get_command_priority(cmd_code))
data=(int(input("Введіть номер ID тяги двигуна:")),float(input("Введіть значення кута нахилу:")),float(input("Введіть значення кута повороту:")))
print(decode_thrust_vector(data))
v0=5000
print(simulate_mars_entry(v0))
i_list=list(map(float,input("Введіть виміри струму:").split()))
u_list=list(map(float,input("Введіть виміри напруги:").split()))
dt=0.1
print(calculate_consumed_energy(i_list, u_list, dt))
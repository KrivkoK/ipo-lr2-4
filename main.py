import math

def calculate_function(X, Y, Z):
    # Вычисляем |cos(X) - cos(Y)|
    cos_sin_vich = abs(math.cos(X) - math.cos(Y))
    
    # Вычисляем 1 + 2 * sin^2(Y)
    sin_squared = 1 + 2 * (math.sin(Y) ** 2)
    
    # Вычисляем |cos(X) - cos(Y)|^(1 + 2 * sin^2(Y))
    first_part = cos_sin_vich ** sin_squared
    
    # Вычисляем (1 + Z + Z^2/2 + Z^3/3 + Z^4/4)
    second_part = 1 + Z + (Z**2) / 2 + (Z**3) / 3 + (Z**4) / 4
    
    # Возвращаем итоговое значение функции
    return first_part * second_part

# Пример использования
X = float(input("Введите значение X (в радианах): "))
Y = float(input("Введите значение Y (в радианах): "))
Z = float(input("Введите значение Z: "))

result = calculate_function(X, Y, Z)
print(f"Результат вычисления функции: {result}")

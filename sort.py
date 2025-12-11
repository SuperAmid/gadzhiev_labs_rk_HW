"""
Лабораторная работа №3-4
Функциональные возможности языка Python
Задача 4: Сортировка по модулю в порядке убывания
"""

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print("Исходный массив:", data)
    print()
    
    # Способ 1: Без lambda - используем встроенную функцию abs
    result = sorted(data, key=abs, reverse=True)
    print("Способ 1 (без lambda):")
    print(result)
    print()
    
    # Способ 2: С lambda - создаем анонимную функцию для вычисления модуля
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("Способ 2 (с lambda):")
    print(result_with_lambda)





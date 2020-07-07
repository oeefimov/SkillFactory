#'''Итоговый проект по модулю 0'''

import numpy as np

def pick_a_number(number):
    """Функция угадывания числа number в интервале от 1 до 100 включительно.
       Использует метод бинарного поиска.
    """ 
    counter = 0    # Счетчик попыток
    predict = 0    # Претендент на загаданное число
    min_num = 0    # Нижняя граница сужаемого интервала поиска
    max_num = 101  # Верхняя граница сужаемого интервала поиска
           
    while predict != number:
        counter += 1
        predict = min_num + int((max_num - min_num) / 2)
        if number > predict:
            min_num = predict
        elif number < predict: 
            max_num = predict
    
    return counter 

def score_game(game_function, iteration):
    """Функция определения среднего числа попыток
       при угадывании числа каким-либо игровым алгоритмом
       
       Входные параметры:
       game_function - функция, реализующая игровой алгоритм
       iteration - количество вызовов game_function для вычисления среднего
    """
    
    # Список количеств попыток, полученных при вызовах game_function
    counter_list = []
    
    # Набор случайных чисел для их последовательного угадывания
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=iteration)
    
    # Вызов игровой функции для каждого случайного числа из набора 
    for num in random_array:
        counter_list.append(game_function(num))
    
    # Подсчет среднего числа попыток
    score = int(np.mean(counter_list))
    
    return(score)

print(f"Ваш игровой алгоритм использует в среднем {score_game(pick_a_number, 1000)} попыток")
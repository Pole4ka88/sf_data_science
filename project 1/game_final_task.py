"""Игра Угадай число!
Компьютер сам загадывает число от 1 до 100 и сам же его угадывает 
за минимальное количество попыток.
"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Угадываем число, корректируя при этом диапазон угадывания

    Args:
        number (int, optional): Загаданное число. Defaults to 1

    Returns:
        int: число попыток
    """
    
    range_start = 1 #минимальное число в диапазоне поиска
    range_end = 101 #максимальное число в диапазоне поиска
    count = 0 # счетчик попыток
    
    while True:
        predict_number = np.random.randint(range_start, range_end) #выбираем рандомное число для начала поиска
        count += 1
        if predict_number == number: break
        #корректируем диапазон поиска, "отсекая" тот интервал, в котором уже точно нет загаданного числа
        #повторяем пока не угадаем число
        elif predict_number < number: range_start = predict_number          
        elif predict_number > number: range_end = predict_number            
    return (count)
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем программа угадывает число (1000 подходов)

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #контрольный список для количеств попыток
    np.random.seed(1) #фиксируем для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел

    for number in random_array: count_ls.append(random_predict(number)) #угадали каждое число из списка, с помощью нашей программы. 
        #добавили в контрольный список количество попыток угадывания каждого числа
    
    score = int(np.mean(count_ls)) #вычислили среднее число попыток на основании контрольного списка
    print(f'Ваш алгоритм угадыват число в среднем за {score} попыток')
    return (score)        


if __name__ == "__main__":
    # RUN    
    score_game(random_predict)
"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # компьютер загадывает рандомное число

# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: ")) #угадывающий вводит первое предполагаемое число
    
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")
    #основываясь на подсказках пользователь вводит свои варианты, пока не угадает число
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла

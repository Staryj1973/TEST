#print('alex')
n = 729 
# Создаём бесконечный цикл
while True:
    # Проверяем условие, что остаток от деления на 3 равен 0.
    if n % 3 == 0:
        # Если условие выполняется, новое число — результат целочисленного деления на 3.
        n = n // 3 
        # Проверяем условие, что в результате деления получили 1.
        if n == 1: 
            # Выводим утвердительное сообщение
            print('n - is the power of the number 3!')
            # Выходим из цикла
            break 
    else: 
        # В противном случае выводим сообщение-опровержение
        print('n - is not the power of the number 3!') 
        # Выходим из цикла
        break 
## Будет выведено:
## n - is the power of the number 3!
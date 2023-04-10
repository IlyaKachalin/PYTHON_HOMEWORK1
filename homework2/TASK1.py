# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите количество монеток: "))
list = []
for i in range(n):
    t = random.randint(0, 1)
    list.append(t)
print(list)

list2 = []
list3 = []
for i in range(n):
    if list[i] == 1:
        list2.append(list[i])
    else:
        list3.append(list[i])
if (len(list2) >= len(list3)):
    print(f"Перевернуть нужно {len(list3)} монеток")
else:
    print(f"Перевернуть нужно {len(list2)} монеток")

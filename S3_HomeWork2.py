print("\033[H\033[J", end="")
""" Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.    """
list = [1, 12, 3, 10, 8, 685, 98, 65, 9, -6, -11, 52, 74, -2]
k = int(input('Введите число: '))

# list_of_difference = []
# for el in list:
#     list_of_difference.append((k - el) if ((k - el) > 0) else (el - k))
# print(min(list_of_difference))   # - Так мы находим минимальную Разницу. А не значение ближайшего эл.

count = 1 
# начало боевого кода:
nearest = 0
difference = 1000000000
for el in list:
    if difference > abs(el - k):
        difference = abs(el - k)
        nearest = el
    # конец боевого кода.
    print(f'{count}. el = {el},\t мин-ая разница на данный момент = {difference}. Ближайший = {nearest}')
    count += 1

print(nearest)  # тоже в итоговый код.

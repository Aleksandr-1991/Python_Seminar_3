print("\033[H\033[J", end="")
""" Задача №17. Дан список чисел. Определите, сколько в нём
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6                    """

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list_1)))

list_2 = []

for el in list_1:
    if el not in list_2:
        list_2.append(el)

print(len(list_2))
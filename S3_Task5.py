print("\033[H\033[J", end="")
""" Обойти чётные элементы на нечётных поз..    """
array = [10, 21, 31, 40, 51, 60, 70, 80, 91]
for i in range(0, len(array), 2):
    if array[i] % 2 == 0:
        print(array[i])
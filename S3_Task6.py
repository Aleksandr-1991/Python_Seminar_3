print("\033[H\033[J", end="")
""" Поменять местами последний эл. с 1ым.    """
array = [5, 651, 612, 62, 621, 612, 98, 2, 65, 3, 69, 98]
print(array)
# temp = array[0]
# array[0] = array[-1]
# array[-1] = temp
# print(array)

last = array.pop()
print(array)
first = array.pop(0)
print(array)

array.insert(0, last)
print(array)
array.append(first)
print(array)
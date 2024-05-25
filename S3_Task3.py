print("\033[H\033[J", end="")
""" Задача №21. Напишите программу для печати всех уникальных значений в спискe словарей.
Input: [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, 
{"VII" : "S005"}, {" V " : "S009"}, {"VIII" : "S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}.    """

list = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, 
{"VII" : "S005"}, {" V " : "S009"}, {"VIII" : "S007"}]   # Cписок словарей.

set_1 = set()

for dict_1 in list:
    for value in dict_1.values():
        set_1.add(value)

print(set_1)
# "Сет компрехеншн / множественное включение." - со слов лектора Дмитрий Читалов:
print({dict_1[item] for dict_1 in list for item in dict_1})
print({pizda[chlen] for pizda  in list for chlen in pizda})   # Запомнить!


if hasattr(list, '__iter__'):
    print("Этот объект итерируемый")
else:
    print("Этот объект не итерируемый")
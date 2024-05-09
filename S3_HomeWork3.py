print("\033[H\033[J", end="")
""" В настольной игре Скрабл (Scrabble) каждая буква имеет опр-ценность.
В случае с анг-алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Прога вычисляет ст-ть введенного пол-лем слова k  и выв его на экран. 
На вход только 1 слово, к-ое содержит либ тол анг, либ тол русские буквы.
Пример: 
k = 'ноутбук' # 12              """


k = input('Введите одно слово только на русском или только на английском: ')
eng = 'abcdefghijklmnopqrstuvwxyz'
rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

list_English = {1:'AEIUOLSNTR', 2:'DG', 3:'BMCP',
                4:'FWHVY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ЩФЪ'}

if k[0].lower() in eng:
    sum = 0
    for letter in k:
        for key, value in list_English.items():
            if letter.upper() in value:
                sum += key
else:
    if k[0].lower() in rus:
        sum = 0
        for letter in k:
            for key, value in list_Russian.items():
                if letter.upper() in value:
                    sum += key
print(sum)
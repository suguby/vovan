# -*- coding: utf-8 -*-

# Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать,
# какие символы в секретных зашифрованных посланиях употребляются чаще других.
# Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов.
# Поэтому он хочет построить гистограмму количества символов в сообщении.
# Гистограмма – это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз,
# соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

# Формат входных данных
#
# Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы,
# цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк.
# Размер входного файла не превышает 2048 байт. Текст содержит хотя бы один непробельный символ.
# Все строки входного файла не длиннее 200 символов.


# Формат выходных данных
#
# Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#»,
# количество которых должно быть равно количеству символов c в данном тексте.
# Под каждым столбиком напишите символ, соответствующий ему.
# Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке,
# первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга.
# Отсортируйте столбики в порядке увеличения кодов символов.


# Примеры
#    Hello, world!
#         #
#         ##
#    #########
#    !,Hdelorw


#    Twas brillig, and the slithy toves
#    Did gyre and gimble in the wabe;
#    All mimsy were the borogoves,
#    And the mome raths outgrabe.
#             #
#             #
#             #
#             #
#             #
#             #         #
#             #  #      #
#          #  # ###  ####
#          ## ###### ####
#          ##############
#          ##############  ##
#    #  #  ############## ###
#    ########################
#    ,.;ADTabdeghilmnorstuvwy

file_name = input(
    'Введите имя файла без расширения(поддерживается только .txt): ')

f = open(file_name + '.txt', 'r')
long_str = f.read().strip()
long_str = ''.join(long_str.split())

number_of_letters = {}

for letter in long_str:
    number_of_letters[letter] = number_of_letters.get(letter, 0) + 1

sort_number_of_letters = [list(x) for x in number_of_letters.items()]
sort_number_of_letters.sort()

width_histogram = len(sort_number_of_letters)
height_histogram = max(number_of_letters.values())
sort_letters = ''.join([x[0] for x in sort_number_of_letters])
histogram = [[' '] * width_histogram for x in range(height_histogram)]

for i in range(height_histogram):
    for j in range(width_histogram):
        if sort_number_of_letters[j][1] > 0:
            histogram[i][j] = '#'
            sort_number_of_letters[j][1] -= 1

for row in histogram[::-1]:
    print(''.join(row))
print(sort_letters)

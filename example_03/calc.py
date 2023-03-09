import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]

        if(coef_str[0] == '-'):
            coef_str = sys.argv[index].replace('-','')
            # print('coef_str_if', coef_str)
        else:
            coef_str = sys.argv[index]
            # print('coef_str_else', coef_str)

        if(coef_str.isdigit() == True):
            coef_str = sys.argv[index]
            # print(f'{coef_str} явл-ется числом', )
        else:
            print('Ошибка! Введите натуральное число!')

    except:
        while True:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
            # Проверка, есть ли минус числа и нулевой коэффициент?
            if (coef_str[0] != '0' or index == 2 or index == 3):
                if (coef_str[0] == '-'):
                    coef_str_buff = coef_str.replace('-', '')
                    if (coef_str_buff.isdigit()):
                        break
                if (coef_str.isdigit()):
                    break

            print("Ошибка! Введите натуральное число!")

    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    # Если дискриминат равен нулю, то корень может быть только одним
    if D == 0.0:
        root = -b / (2.0 * a)
        # result.append(root)
        if (root > 0.0):
            root1 = math.sqrt(root)
            result.append(root1)
            result.append(-root1)

    # Если дискриминат больше нули, то корень может быть четырем
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)

        if (root1 == 0):
            result.append(abs(root1))
        elif (root2 == 0):
            result.append(abs(root2))

        if (root1 > 0.0):
            root3 = math.sqrt(root1)
            result.append(root3)
            result.append(-root3)

        if (root2 > 0.0):
            root4 = math.sqrt(root2)
            result.append(root4)
            result.append(-root4)

    return result


def delete_space_into_list(string):
    new_str = []
    str_value = ''
    for i in string:
        if(i != ' '):
            str_value += i
        else:
            new_str.append(float(str_value))
            str_value = ''

    new_str.append(float(str_value))

    return new_str

def convert(input_text_file='input.txt'):
    file = open(input_text_file, 'r')

    dictionary = {}
    lenght = 0

    a = []
    b = []
    c = []

    for i in file:
        value = delete_space_into_list(i)
        a.append(value[0])
        b.append(value[1])
        c.append(value[2])

        lenght += 1

    dictionary['a'] = a
    dictionary['b'] = b
    dictionary['c'] = c

    # print(value)
    return dictionary, lenght

def main():
    # values, lenght = convert(sys.argv[1])
    values, lenght = convert()
    file_b = open('output_beautiful.txt', 'w')
    file = open('output.txt', 'w')
    answers = {}
    # print(values)
    try:
        print('=' * 100)
        for i in range(lenght):
            for key in values:
                if (key == 'a'):
                    a = values[key][0 + i]
                    print('Коэффициент А:', a)
                if (key == 'b'):
                    b = values[key][0 + i]
                    print('Коэффициент B:', b)
                if (key == 'c'):
                    c = values[key][0 + i]
                    print('Коэффициент C:', c)

            # Вычисление корней
            roots = get_roots(a, b, c)
            answers['root: ' + str(i)] = roots
            # Вывод корней
            len_roots = len(roots)
            if len_roots == 0:
                print('Нет корней')
            elif len_roots == 1:
                print('Один корень {}'.format(round(roots[0], 2)))
            elif len_roots == 2:
                print('Два кореня: {} и {}'.format(round(roots[0], 2), round(roots[1], 2)))
            elif len_roots == 3 and roots[0] == 0.0:
                print('Три корня: {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 3:
                print('Два корня: {} и {}'.format(round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 4:
                print(
                    'Четыре корня: {} и {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2),
                                                             round(roots[3], 2)))
            print('='*100)

        file_b.write('='*100)
        file_b.write('\n')
        for key, value in answers.items():
            file_b.write(str(key) + '\n')
            file_b.write(str(value) + '\n')
            file.write(str(value))
            file.write('\n')
            file_b.write('='*100)
            file_b.write('\n')

    except:
        print('Ошибка заполнения!')


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()


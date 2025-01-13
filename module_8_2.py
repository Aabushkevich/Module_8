def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result =+ i
        except TypeError:
            incorrect_data =+ 1
    return tuple(result,incorrect_data)

def calculate_average(numbers):
    try:
        a = sum(numbers)/len(numbers)
        return a
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 'В numbers записан некорректный тип данных'

print(f'Результат 1:{calculate_average("1,2,3")}')
print(f'Результат 2:{calculate_average([1,"Строка",3,"Еще Строка"])}')
print(f'Результат 3:{calculate_average(567)}')
print(f'Результат 4:{calculate_average([41,15,36,13])}')

"""Не могу понять, правильно работает программа или нет?В первых 3х случаях перехватывается ошибка,
 в 4м - выдается результат, но вывод не такой как в задании"""

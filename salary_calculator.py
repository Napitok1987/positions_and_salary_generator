class OutOfRangeError(Exception):  # исключение для значений вне заданной области
    pass


class IncorrectSalary(Exception):  # исключение для значений вне заданной области
    pass


try:
    salary = 0
    print('Выберите форму сотрудничества:', '[1] Трудоустройство в штат', '[2] Договор ИП', '[3] Договор ГПХ', sep='\n')
    employment_type: int = int(input())
    if employment_type not in range(1, 4):  # проверка на соотвествие введённых данных заданным ограничениям
        raise OutOfRangeError()
    else:
        print('Введи сумму "на руки" о которой договорились')
        salary_net: int = int(input())
        if 10000 > salary_net or salary_net > 1000000:
            raise IncorrectSalary()
        elif employment_type in range(1, 4):
            if employment_type == 1 or employment_type == 3:
                salary = int(salary_net / 0.87)
            elif employment_type == 2:
                salary = int(salary_net * 1.06)
        print('Зарплата составит {salary} рублей 00 копеек'.format(salary=str(salary)))

except ValueError:  # обработка случая когда введена буква или символ
    print('Вы ввели недопустимое значение. Пожалуйста, перезапустите программу и введите число в диапазоне от 1 '
          'до 3')
except OutOfRangeError:
    print('Вы ввели число вне диапазона от 1 до 3.')
except IncorrectSalary:
    print('Вы ввели сумму меньше 10 000 или больше 1 000 000 рублей')
else:
    print('Программа завершила работу')

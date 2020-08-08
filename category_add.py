# Это программа для формирования списка должностей и зарплат, на базе которого работает программа для создания
# предложений о сотрудничестве
import csv
import sys


class OutOfRangeError(Exception):  # исключение для значений вне заданной области
    pass


def category_add():
    print('Вы хотите:', '[1] Добавить позицию разработчика', '[2] Добавить позицию тестировщика', '[3] Выйти из '
                                                                                                  'программы',
          sep='\n')
    position_type = input()  # выбор какую позицию добавляем - разработчик/тестировщика или выход из программы
    try:
        position_type = int(position_type)
        if position_type not in range(1, 4):  # проверка на соотвествие введённых данных заданным ограничениям
            raise OutOfRangeError()
        elif position_type in range(1, 4):
            if position_type == 3:  # выход из программы
                sys.exit(1)
            else:
                pos_name_template = input('Введите название позиции: ')
                salary_net_min: int = int(input("Введите минимальную ставку \"на руки\" для даннрой категории: "))
                salary_net = salary_net_min
                salary_net_max: int = int(input("Введите максимальную ставку \"на руки\" для данной категории: "))
                salary_step: int = int(input('Какой шаг зарплаты между категориями Вы хотите установить?: '))
                num_pos = int((salary_net_max - salary_net_min) / salary_step)
                pos_counter: int = 1  # стартовое значение счётчика для правильного сохранения названий категории.
                # Стартовое значение единица, так как не может быть "Ведущего инженера 0 категории"
                for i in range(0, num_pos + 1):
                    pos_name: str = str(pos_name_template + " " + str(pos_counter) + " категории")
                    salary_gross = float("{0:.2f}".format(salary_net / 0.87))
                    if position_type == 1:  # сохранение данных для должностей разработчиков
                        with open("devpos.csv", 'a', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([pos_name, salary_net, salary_gross])
                    elif position_type == 2:  # сохранение данных для должностей тестировщиков
                        with open("qapos.csv", 'a', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([pos_name, salary_net, salary_gross])
                    print(pos_name)
                    print(salary_net)
                    print(salary_gross)
                    pos_counter = pos_counter + 1
                    salary_net = salary_net + salary_step
    except ValueError:  # обработка случая когда введена буква или символ
        print('Вы ввели недопустимое значение. Пожалуйста, перезапустите программу и введите число в диапазоне от 1 '
              'до 3')
    except OutOfRangeError:
        print('Вы ввели число вне диапазона от 1 до 3.')
    finally:
        print('Программа завершила работу')


category_add()
while True:
    flag = input('Хотите добавить другие позиции? [да/нет]: ')
    if flag == 'да':
        category_add()
    else:
        break

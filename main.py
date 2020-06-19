import csv
from csv import DictWriter
print('Вы хотите добавить позицию:', "[1] разработчика", '[2] тестировщика', sep='\n')
position_type: int = int(input())
pos_name_template = input('Введите название позиции: ')
num_pos = int(input('Сколько категорий для данной позиции Вы хотете добавить?: '))
salary: int = int(input("Введите ставку \"на руки\" для первой категории: "))
salary_step: int = int(input('Какой шаг зарплаты между категориями Вы хотите установить?: '))
pos_counter: int = 1
for i in range(0, num_pos):
    pos_name: str = str(pos_name_template+" "+str(pos_counter)+" категории")
    if position_type == 1:
        with open("devpos.csv", mode='a') as csvfile:
            fieldnames = ['pos_name', 'salary']
            writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'pos_name': pos_name, 'salary': salary})
    elif position_type == 2:
        with open("qapos.csv", mode='a') as csvfile:
            fieldnames = ['pos_name', 'salary']
            writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'pos_name': pos_name, 'salary': salary})
    else:
        print('К сожалению, в данный момент мы не поддерживаем позиции по другим направлениям')
    print(salary)
    print(pos_name)
    pos_counter = pos_counter+1
    salary = salary+salary_step


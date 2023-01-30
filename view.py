from names_list import fst_names_list, lst_names_list, sub_list
import random as rnd


def choice_todo():
    print("\n Какое действие вы хотите выполнить:\n\
    0 - Вывести весь список;\n\
    1 - Ввести ученика;\n\
    2 - Ввести предмет;\n\
    3 - Ввести оценку;\n\
    4 - Показать перечень учеников \n\
    5 - Показать оценки конкретного ученика \n\
    6 - Рандомное заполнение (ученик\предмет\оценка) \n\
    7 - Средний балл \n\
    8 - Для выхода \n")
    ch = int (input("Введите цифру: "))
    return ch

def get_student():
    student = input ("Введите имя и фамилию студента: ") 
    return student

def get_sub():
    sub = input ("Введите наименование предмета: ")
    return sub

def get_mark():
    mark = int(input ("Введите оценку по предмету: "))
    return mark

def rnd_names():
    name= "".join(rnd.choice(fst_names_list)+" "+rnd.choice(lst_names_list)) #for i in range(3))
    return name

def rnd_sub():
    sub= rnd.choice(sub_list)
    return sub

def rnd_mark():
    mark = rnd.randint(1,5)
    return mark




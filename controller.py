from view import choice_todo, get_student, get_sub, get_mark, rnd_names, rnd_sub, rnd_mark
import pickle
import random as rnd
from statistics import mean
import os
def clear(): return os.system('cls')

students = {}
names_list = []
sub_list = []


def start():
    clear()
    while True:
        
        ch = choice_todo()
        if ch == 0:
            print(students)

        elif ch == 1:
            name = get_student()
            if name not in names_list:
                names_list.append(name)
                students[name] = {}
                for i in sub_list:
                    students[name][i] = []
        
        elif ch == 2:
            sub = get_sub()
            if sub not in sub_list:
                sub_list.append(sub)
                for i in names_list:
                    students[i][sub] = []
        
        elif ch == 3:
            name = get_student()
            sub = get_sub()
            mark = get_mark()
            students[name][sub].append(mark)
        
        elif ch == 4:
            for i in students.keys():
                print(i)

        elif ch == 5:
            name = get_student()
            print(students[name])
        
        elif ch == 6:
            for i in range(100):
                name= rnd_names()
                if name not in names_list:
                    names_list.append(name)
                sub = rnd_sub()
                if sub not in sub_list:
                    sub_list.append(sub)
                mark = rnd_mark()
                students[name]={sub:[mark]}
                    
        elif ch == 7:
            av_mark={}
            name = get_student()
            sub = get_sub()
            av_mark=mean(students[name][sub])
            print(f"\n средний балл {name} по {sub} ---> {av_mark} \n")

        elif ch == 8:
            print("Вы вышли из программы!")
            break

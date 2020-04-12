#!/usr/bin/python3

from pyrob.api import *
i = 2
mark = 0
def run():
    global i
    global mark
    while mark == 0:
        for j in range(i):
            if wall_is_on_the_right() == False:
                move_right()
            if wall_is_on_the_right() == True:
                mark = 1
                break
        if mark == 0:
            fill_cell()            
        i+=1
        run()
@task
def task_7_5():
    global mark
    global i
    i = 2
    mark = 0
    i = 2
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    run()
    
    

if __name__ == '__main__':
    run_tasks()

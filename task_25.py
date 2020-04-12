#!/usr/bin/python3

from pyrob.api import *

def run():
    while wall_is_on_the_right() == False:
        fill_cell()
        move_right()
        fill_cell()
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        move_up()
        move_right()
        fill_cell()
        if wall_is_on_the_right() == False:
            move_right()
            if wall_is_on_the_right() == False:
                move_right()
    

@task
def task_2_2():
    move_down(2)
    i=3
    while i !=0:
        run()
        i-=1
    move_up()
    move_left(2)


if __name__ == '__main__':
    run_tasks()

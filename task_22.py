#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while 1>0:
        fill_cell()
        if wall_is_on_the_right()  == False:
            while wall_is_on_the_right()  == False:
                move_right()
                fill_cell()
            if wall_is_beneath() == False:
                move_down()
            fill_cell()
            while wall_is_on_the_left() == False:
                move_left()
                fill_cell()
            if wall_is_beneath() == False:
                move_down()
        if wall_is_on_the_left() == True and wall_is_beneath() == True and cell_is_filled() == True:
            break
        


if __name__ == '__main__':
    run_tasks()

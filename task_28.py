#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled = 0
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            filled += 1
            if filled == 5:
                return
            move_right()
        if cell_is_filled() != True:
            move_right()
            

        


if __name__ == '__main__':
    run_tasks()

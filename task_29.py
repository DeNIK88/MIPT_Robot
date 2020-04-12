#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    filled = 0
    while wall_is_on_the_right() == False:
        if cell_is_filled() == True:
            filled += 1
            if filled == 3:
                break
            move_right()
        if cell_is_filled() != True:
            filled = 0
            move_right()
            


if __name__ == '__main__':
    run_tasks()

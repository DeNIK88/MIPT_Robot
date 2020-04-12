#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    quan_to_fill = 1
    move_down()
    for i in range(13):
        move_right()
        for j in range(quan_to_fill):
            fill_cell()
            move_right()
        quan_to_fill += 1
        move_down()
        while wall_is_on_the_left() == False:
            move_left()
    move_right()

if __name__ == '__main__':
    run_tasks()

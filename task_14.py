#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while wall_is_on_the_right() == False:
        if wall_is_above() == False and wall_is_beneath() == True:
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_beneath() == False and wall_is_above() == True:
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif wall_is_above() == False and wall_is_beneath() == False:
            move_up()
            fill_cell()
            move_down(n=2)
            fill_cell()
            move_up()
            move_right()
        elif wall_is_above() == True and wall_is_beneath() == True:
            fill_cell()
            move_right()
        else:
            move_right()
    if wall_is_above() == False and wall_is_beneath() == True:
        move_up()
        fill_cell()
        move_down()
    elif wall_is_beneath() == False and wall_is_above() == True:
        move_down()
        fill_cell()
        move_up()
    elif wall_is_above() == False and wall_is_beneath() == False:
        move_up()
        fill_cell()
        move_down(n=2)
        fill_cell()
        move_up()
    elif wall_is_above() == True and wall_is_beneath() == True:
        fill_cell()

if __name__ == '__main__':
    run_tasks()

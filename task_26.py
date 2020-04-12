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

@task(delay=0.02)
def task_2_4():
    move_down()
    run()
    move_down(4)
    move_left(38)
    run()
    move_down(4)
    move_left(38)
    run()
    move_down(4)
    move_left(38)
    run()
    move_down(4)
    move_left(38)
    run()
    move_up()
    move_left(38)
if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.05)

def task_8_30():
    neprohod = 0
    while neprohod < 2:
        while not wall_is_on_the_right():
            if not wall_is_beneath():
                move_down()
                neprohod = 0
            move_right()
        if wall_is_on_the_right():
            neprohod += 1

        while not wall_is_on_the_left():
            if not wall_is_beneath():
                move_down()
                neprohod = 0
            move_left()
        if wall_is_on_the_left():
            neprohod += 1
if __name__ == '__main__':
    run_tasks()

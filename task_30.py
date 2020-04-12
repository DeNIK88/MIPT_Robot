#!/usr/bin/python3

from pyrob.api import *

def draw_cube():
    global size_cube
    i = 1
    while i < size_cube:
        if i > 1:
            fill_cell()
            move_up()
            i += 1
        else:
            move_up()
            i += 1
    i = 1

    while i < size_cube:
        if i > 1:
            fill_cell()
            move_right()
            i += 1
        else:
            move_right()
            i += 1
    i = 1
    while i < size_cube:
        if i > 1:
            fill_cell()
            move_down()
            i += 1
        else:
            move_down()
            i += 1
    i = 1
    while i < size_cube:
        if i > 1:
            fill_cell()
            move_left()
            i += 1
        else:
            move_left()
            i += 1
    size_cube -= 2

@task(delay=0.05)
def task_9_3():
    global size_cube
    size_cube = 1
    while not wall_is_beneath():
        move_down()
        size_cube+=1
    while size_cube != 1:
        draw_cube()
        move_right()
        move_up()
    while not wall_is_on_the_left():
        if not wall_is_beneath():
            move_down()
        elif not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()

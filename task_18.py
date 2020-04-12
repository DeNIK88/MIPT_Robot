#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while wall_is_on_the_left() == False:
        move_left()
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up()
            while wall_is_on_the_left() == False:
                move_left()
            break
        elif wall_is_beneath() == False:
            move_down()
            while wall_is_on_the_left() == False:
                move_left()
            while wall_is_above() == False:
                move_up()
            break
    else:
        while wall_is_on_the_right() == False:
            move_right()
            if wall_is_above() == False:
                while wall_is_above() == False:
                    move_up()
                while wall_is_on_the_left() == False:
                    move_left()
                break
            elif wall_is_beneath() == False:
                move_down()
                while wall_is_on_the_left() == False:
                    move_left()
                while wall_is_above() == False:
                    move_up()
                break
            

if __name__ == '__main__':
    run_tasks()

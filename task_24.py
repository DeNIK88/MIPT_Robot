#!/usr/bin/python3

from pyrob.api import *

def run():
    move_down(n=2)
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_up()
    move_left(n=2)
@task
def task_2_1():
    run()


if __name__ == '__main__':
    run_tasks()

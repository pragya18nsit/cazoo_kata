#!/usr/bin/python3

import pytest
import unittest

from coordinate import Coordinate
from grid import Grid
from rover import Rover


@pytest.fixture
def rover_obj():
    '''Returns a Rover instance with CURRent position'''
    return Rover()


@pytest.mark.parametrize("command, position", [("R", "0:0:E"), ("RR", "0:0:S"), ("RRR", "0:0:W"), ("RRRR", "0:0:N")])
def test_rotate_right(rover_obj, command, position):
    assert rover_obj.execute(command) == position


@pytest.mark.parametrize("command, position", [("L", "0:0:W"), ("LL", "0:0:S"), ("LLL", "0:0:E"), ("LLLL", "0:0:N")])
def test_rotate_left(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("M", "0:1:N"), ("MMM", "0:3:N")])
def test_move_up(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("MMMMMMMMMM", "0:0:N"), ("MMMMMMMMMMMMMMM", "0:5:N")])
def test_wrap_from_top_to_bottom_when_moving_north(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("RM", "1:0:E"), ("RMMMMM", "5:0:E")])
def test_move_right(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("RMMMMMMMMMM", "0:0:E"), ("RMMMMMMMMMMMMMMM", "5:0:E")])
def test_wrap_from_right_to_left_when_moving_north(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("LM", "9:0:W"), ("LMMMMM", "5:0:W")])
def test_move_left(rover_obj, command, position):
    assert rover_obj.execute(command) == position

@pytest.mark.parametrize("command, position", [("LLM", "0:9:S"), ("LLMMMMM", "0:5:S")])
def test_move_south(rover_obj, command, position):
    assert rover_obj.execute(command) == position


## there is an obstacle at 3rd move..so cant move 4 positions right..
@pytest.mark.parametrize("command, position", [("MMMM", "O:0:3:N"), ("RMMMMMM", "O:1:0:E")])
def test_stop_at_obstacle( command, position):
    obstacle1_coordinate = Coordinate(0, 4)
    obstacle2_coordinate = Coordinate(2 ,0)

    grid = Grid([obstacle1_coordinate, obstacle2_coordinate])
    rover_obj = Rover(grid)
    assert rover_obj.execute(command) == position

if __name__ == '__main__':
    unittest.main()

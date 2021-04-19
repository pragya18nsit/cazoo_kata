from coordinate import Coordinate
from direction_enum import DirectionEnum
from grid import Grid


class Rover(object):

    def __init__(self, grid=Grid()):
        self.direction = "N"
        self.directionMap = DirectionEnum()
        self.coordinate = Coordinate(0, 0)
        self.grid = grid
        self.prefix = ""

    def execute(self, commands):

        for command in commands:
            if command == "R":
                # self.direction = self.rotate_right()

                self.direction = self.directionMap.get_rotated_direction(self.direction, "right")
            elif command == "L":
                # self.direction = self.rotate_left()

                self.direction = self.directionMap.get_rotated_direction(self.direction, "left")
                #
                # self.directions = self.get_rotated_direction(self.direction)
                # self.direction = self.directions[1]
            elif command == "M":
                self.coordinate, is_obstacle = self.grid.get_next_coordinate_for(self.coordinate, self.direction)

                # self.move_rover()
                if is_obstacle:
                    self.prefix = "O:"


        return self.prefix + str(self.coordinate.x) + ":" + str(self.coordinate.y) + ":" + self.direction

    # def rotate_right(self):
    #     if self.direction == "N":
    #         self.direction = "E"
    #     elif self.direction == "S":
    #         self.direction = "W"
    #     elif self.direction == "W":
    #         self.direction = "N"
    #     else:
    #         self.direction = "S"
    #     return self.direction
    #
    #
    #
    # def rotate_left(self):
    #     if self.direction == "N":
    #         self.direction = "W"
    #     elif self.direction == "S":
    #         self.direction = "E"
    #     elif self.direction == "W":
    #         self.direction = "S"
    #     else:
    #         self.direction = "N"
    #     return self.direction

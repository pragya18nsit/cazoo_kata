from coordinate import Coordinate


class Grid(object):

    def __init__(self, obstacles=[]):
        self.max_width = 10
        self.max_height = 10
        self.obstacles = obstacles

    def get_next_coordinate_for(self, coordinate, direction):
        y = coordinate.get_y()
        x = coordinate.get_x()
        if direction == "N":
            y = (y + 1) % self.max_height
        elif direction == "E":
            x = (x + 1) % self.max_width
        elif direction == "W":
            if x > 0:
                x = x - 1
            else:
                x = self.max_width - 1
        elif direction == "S":
            if y > 0:
                y = y - 1
            else:
                y = self.max_height - 1

        new_coordinate = Coordinate(x, y)

        if self.is_new_coordinate_an_obstacle(self.obstacles, new_coordinate, coordinate):
            return coordinate, True
        else:
            return new_coordinate, False

    def is_new_coordinate_an_obstacle(self, obstacles, new_coordinate, coordinate):
        for obstacle in obstacles:
            if obstacle.x == new_coordinate.x and obstacle.y == new_coordinate.y:
                print("obstacle found")
                return True
        return False


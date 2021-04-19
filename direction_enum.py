
class DirectionEnum(object):

    def __init__(self):
        self.directionMap = {
            "N": {"value" : "N", "left": "W","right": "E"},
            "S": {"value": "S", "left":"E","right":  "W"},
            "E": {"value": "E", "left": "N", "right": "S"},
            "W": {"value": "W", "left" : "S", "right" : "N"}
        }

    def get_value_of_direction(self, direction):
        directions =  self.directionMap[direction]
        return directions["value"]

    def get_rotated_direction(self, direction, leftorright):
        directions =  self.directionMap[direction]
        if leftorright == "right":
            return directions["right"]
        elif leftorright == "left":
            return directions["left"]

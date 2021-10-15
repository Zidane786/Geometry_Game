class Rectangle:
    def __init__(self, point1, point2):
        """
        point1 and point2 are object of Class Point which will become instance attribute of
        Rectangle Class this 2 point will create rectangle
        """
        self.point1 = point1
        self.point2 = point2


class Point:
    def __init__(self, x, y):
        """
        x,y are coordinate which which create Point
        :param x: coordinate
        :param y: coordinate
        """
        self.x = x
        self.y = y

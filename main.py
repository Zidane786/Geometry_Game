class Rectangle:
    def __init__(self, point1, point2):
        """
        point1 and point2 are object of Class Point which will become instance attribute of
        Rectangle Class this 2 point will create rectangle
        """
        self.point1 = point1
        self.point2 = point2

    def display_coord(self):
        """
        :return:Print Co-ordinate to lower left and upper right of Rectangle
        """
        print(f"Rectangle Co-ordinate:- {self.point1.x},{self.point1.y}",
              f"and {self.point2.x},{self.point2.y}")


class Point:
    def __init__(self, x, y):
        """
        x,y are coordinate which which create Point
        :param x: coordinate
        :param y: coordinate
        """
        self.x = x
        self.y = y

    def fall_in_rect(self, point1, point2):
        """
        check if point lies inside rectangle or not!


        :param point1: lower left or upper right point of rectangle
        :param point2: lower left or upper right point of rectangle
        :return:True if point falls inside rectangle else return False
        """
        if point1.x < self.x < point2.x and point1.y < self.y < point2.y:
            return True
        else:
            return False

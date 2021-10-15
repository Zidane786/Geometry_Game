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

    def area(self):
        """
        :return:Area of Rectangle
        """
        length = self.point2.x - self.point1.x
        width = self.point2.y - self.point1.y
        return width * length


class Point:
    def __init__(self, x, y):
        """
        x,y are coordinate which which create Point
        :param x: coordinate
        :param y: coordinate
        """
        self.x = x
        self.y = y

    def fall_in_rect(self, rect_obj):
        """
        check if point lies inside rectangle or not!


        :param rect_obj: object of Rectangle class is passed
        :return:True if point falls inside rectangle else return False
        """
        if rect_obj.point1.x < self.x < rect_obj.point2.x and \
                rect_obj.point1.y < self.y < rect_obj.point2.y:
            return True
        else:
            return False

    def distance_from_points(self, x, y):

        """
        :param x: co-ordinate of point
        :param y: co-ordinate of point
        :return: Distance between 2 Point
        """

        x_axis = self.x - x
        y_axis = self.y - y
        return ((x_axis * x_axis) + (y_axis * y_axis)) ** (0.5)  # num**0.5 give squareroot of the num

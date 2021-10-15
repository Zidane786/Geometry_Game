from random import randint as ri


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

    def area_of_rect(self):
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
        return ((x_axis * x_axis) + (y_axis * y_axis)) ** 0.5  # num**0.5 give square root of the num


# we want point1<point2 or point2<point1 visa versa so we will run randint() as shown below so there is no
p1 = Point(ri(0, 9), ri(0, 9))
p2 = Point(ri(10, 19), ri(10, 19))

# creating Rectangle Object
rect1 = Rectangle(p1, p2)
rect1.display_coord()

# user input for Point Object so we can check if it fall inside rectengle or not
user_point = Point(float(input("Guess X:-")), float(input("Guess Y:-")))

print(f"Your Point was Inside Rectange:-{user_point.fall_in_rect(rect1)}")

print(f"Length of Rectangle is {rect1.area_of_rect()}")

# return distance between 2 point
print(f"Distance between Point of co-ord {int(6)},{int(3)} and \
{user_point.x},{user_point.y}is :-{user_point.distance_from_points(3, 6):.2f}")

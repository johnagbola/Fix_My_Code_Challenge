class Square:
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            if key == 'width':
                self.height = value

    def area(self):
        """ Area of the square """
        return self.width ** 2

    def perimeter(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.perimeter())

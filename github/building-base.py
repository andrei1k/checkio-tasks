
class Building:
    """ Defines a building
    """

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):

        return {"north-east":[self.south + self.width_NS, self.west + self.width_WE],
                "south-east":[self.south, self.west + self.width_WE],
                "south-west":[self.south, self.west],
                "north-west":[self.south + self.width_NS, self.west]}

    def area(self):
        """ Returns the area of the building
        """
        return self.width_NS * self.width_WE

    def volume(self):
        """ Return the volume of the building
        """
        return self.area() * self.height

    def __repr__(self):
        return ("Building(" + str(self.south) + ", " + str(self.west) + ", "
                + str(self.width_WE) + ", " + str(self.width_NS) + ", "
                + str(self.height) + ")")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"

    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

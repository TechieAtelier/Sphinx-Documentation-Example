import math
from utils.validator import validate_positive_number

class Circle:
    """Represents a circle with a radius.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """Initializes a Circle with a given radius.

        Args:
            radius (float): The radius of the circle. Must be a positive number.

        Raises:
            ValueError: If the radius is not a positive number.
        """
        validate_positive_number(radius)
        self.radius = radius

    def area(self):
        """Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

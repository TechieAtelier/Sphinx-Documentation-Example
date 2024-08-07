from utils.validator import validate_positive_number

class Rectangle:
    """Represents a rectangle with a length and width.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, length, width):
        """Initializes a Rectangle with a given length and width.

        Args:
            length (float): The length of the rectangle. Must be a positive number.
            width (float): The width of the rectangle. Must be a positive number.

        Raises:
            ValueError: If the length or width is not a positive number.
        """
        validate_positive_number(length)
        validate_positive_number(width)
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

from utils.validator import validate_positive_number

class Triangle:
    """Represents a triangle with a base and height.

    Attributes:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
    """

    def __init__(self, base, height):
        """Initializes a Triangle with a given base and height.

        Args:
            base (float): The base of the triangle. Must be a positive number.
            height (float): The height of the triangle. Must be a positive number.

        Raises:
            ValueError: If the base or height is not a positive number.
        """
        validate_positive_number(base)
        validate_positive_number(height)
        self.base = base
        self.height = height

    def area(self):
        """Calculates the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        return 0.5 * self.base * self.height

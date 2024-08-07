def validate_positive_number(value):
    """Validates that the given value is a positive number.

    Args:
        value (float): The number to be validated.

    Raises:
        ValueError: If the value is not a positive number.
    """
    if value <= 0:
        raise ValueError("The value must be positive.")

"""
Input Validators - Utility Functions

Provides validation functions for user inputs in the Todo application.
"""


def validate_todo_title(title: str) -> bool:
    """
    Validate that a todo title is not empty or whitespace-only.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if the title is valid, False otherwise
    """
    return bool(title and title.strip())


def validate_todo_id(todo_id: str) -> bool:
    """
    Validate that a todo ID is a positive integer.

    Args:
        todo_id (str): The ID string to validate

    Returns:
        bool: True if the ID is valid, False otherwise
    """
    try:
        id_value = int(todo_id)
        return id_value > 0
    except (ValueError, TypeError):
        return False


def validate_positive_integer(value: str) -> bool:
    """
    Validate that a string represents a positive integer.

    Args:
        value (str): The value to validate

    Returns:
        bool: True if the value is a positive integer, False otherwise
    """
    try:
        int_value = int(value)
        return int_value > 0
    except (ValueError, TypeError):
        return False


def validate_non_empty_string(value: str) -> bool:
    """
    Validate that a string is not empty or whitespace-only.

    Args:
        value (str): The string to validate

    Returns:
        bool: True if the string is valid, False otherwise
    """
    return bool(value and value.strip())
"""
Todo Entity - Domain Model

Represents a single todo item with its properties and behaviors.
"""

from datetime import datetime
from typing import Optional


class Todo:
    """
    Represents a todo item in the application.

    Attributes:
        id (int): Unique identifier for the todo
        title (str): The task description
        description (str): Optional additional details
        completed (bool): Task completion status
        created_at (datetime): Timestamp of creation
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new Todo instance.

        Args:
            id (int): Unique identifier for the todo
            title (str): The task description (must not be empty)
            description (str): Optional additional details
            completed (bool): Task completion status (defaults to False)
        """
        if not title or not title.strip():
            raise ValueError("Title must not be empty or whitespace-only")

        self.id = id
        self.title = title.strip()
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()

    def __repr__(self):
        """String representation of the Todo."""
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"

    def __eq__(self, other):
        """Check equality based on id, title, and completion status."""
        if not isinstance(other, Todo):
            return False
        return (self.id == other.id and
                self.title == other.title and
                self.completed == other.completed)

    def mark_completed(self):
        """Mark the todo as completed."""
        self.completed = True

    def update_title(self, new_title: str):
        """
        Update the title of the todo.

        Args:
            new_title (str): New title for the todo

        Raises:
            ValueError: If new_title is empty or whitespace-only
        """
        if not new_title or not new_title.strip():
            raise ValueError("Title must not be empty or whitespace-only")
        self.title = new_title.strip()
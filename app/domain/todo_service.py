"""
Todo Service - Domain Layer

Implements the business logic for todo operations.
"""

from typing import List, Optional
from app.domain.todo import Todo
from app.infrastructure.memory_repository import MemoryRepository
from app.utils.validators import validate_todo_title


class TodoService:
    """
    Service class that implements the business logic for todo operations.

    This service orchestrates the interactions between the domain entities
    and the infrastructure layer (repository).
    """

    def __init__(self, repository: MemoryRepository):
        """
        Initialize the TodoService with a repository.

        Args:
            repository (MemoryRepository): The repository to use for data storage
        """
        self.repository = repository

    def create_todo(self, title: str, description: str = "") -> int:
        """
        Create a new todo with validation.

        Args:
            title (str): The title of the new todo
            description (str): Optional description for the new todo

        Returns:
            int: The ID of the created todo

        Raises:
            ValueError: If the title is invalid
        """
        if not validate_todo_title(title):
            raise ValueError("Title must not be empty or whitespace-only")

        # Create a new Todo instance with an initial ID of 0 (will be assigned by repository)
        todo = Todo(id=0, title=title, description=description, completed=False)
        return self.repository.add(todo)

    def get_todo_list(self) -> List[Todo]:
        """
        Retrieve all todos.

        Returns:
            List[Todo]: A list of all todos in the repository
        """
        return self.repository.get_all()

    def update_todo(self, id: int, new_title: str) -> bool:
        """
        Update a todo's title with validation.

        Args:
            id (int): The ID of the todo to update
            new_title (str): The new title for the todo

        Returns:
            bool: True if the update was successful, False otherwise
        """
        if not validate_todo_title(new_title):
            return False

        return self.repository.update(id, new_title)

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo with validation.

        Args:
            id (int): The ID of the todo to delete

        Returns:
            bool: True if the deletion was successful, False otherwise
        """
        # Check if the todo exists before attempting to delete
        existing_todo = self.repository.get_by_id(id)
        if existing_todo is None:
            return False

        return self.repository.delete(id)

    def complete_todo(self, id: int) -> bool:
        """
        Mark a todo as complete with validation.

        Args:
            id (int): The ID of the todo to mark as complete

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        # Check if the todo exists before attempting to complete
        existing_todo = self.repository.get_by_id(id)
        if existing_todo is None:
            return False

        return self.repository.complete(id)

    def validate_input(self, title: str) -> bool:
        """
        Validate user input for a todo title.

        Args:
            title (str): The title to validate

        Returns:
            bool: True if the title is valid, False otherwise
        """
        return validate_todo_title(title)
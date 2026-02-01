"""
In-Memory Repository - Infrastructure Layer

Implements the repository interface using in-memory storage.
"""

from typing import Dict, List, Optional
from app.domain.todo import Todo


class MemoryRepository:
    """
    In-memory repository for storing Todo items.

    This implementation uses a dictionary for O(1) lookups and a counter
    for generating unique IDs.
    """

    def __init__(self):
        """Initialize the repository with empty storage and ID counter."""
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add(self, todo: Todo) -> int:
        """
        Add a new todo to the repository.

        Args:
            todo (Todo): The todo item to add

        Returns:
            int: The ID of the added todo
        """
        # If the todo doesn't have an ID yet, assign the next available one
        if todo.id == 0 or todo.id not in self._todos:
            todo.id = self._next_id
            self._next_id += 1

        self._todos[todo.id] = todo
        return todo.id

    def get_by_id(self, id: int) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.

        Args:
            id (int): The ID of the todo to retrieve

        Returns:
            Optional[Todo]: The todo if found, None otherwise
        """
        return self._todos.get(id)

    def get_all(self) -> List[Todo]:
        """
        Retrieve all todos in the repository.

        Returns:
            List[Todo]: A list of all todos in the repository
        """
        return list(self._todos.values())

    def update(self, id: int, title: str) -> bool:
        """
        Update a todo's title by ID.

        Args:
            id (int): The ID of the todo to update
            title (str): The new title

        Returns:
            bool: True if the update was successful, False otherwise
        """
        if id not in self._todos:
            return False

        try:
            self._todos[id].update_title(title)
            return True
        except ValueError:
            # If the title is invalid, the update fails
            return False

    def delete(self, id: int) -> bool:
        """
        Delete a todo by ID.

        Args:
            id (int): The ID of the todo to delete

        Returns:
            bool: True if the deletion was successful, False otherwise
        """
        if id not in self._todos:
            return False

        del self._todos[id]
        return True

    def complete(self, id: int) -> bool:
        """
        Mark a todo as completed by ID.

        Args:
            id (int): The ID of the todo to mark as completed

        Returns:
            bool: True if the operation was successful, False otherwise
        """
        if id not in self._todos:
            return False

        self._todos[id].mark_completed()
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID without assigning it.

        Returns:
            int: The next available ID
        """
        return self._next_id
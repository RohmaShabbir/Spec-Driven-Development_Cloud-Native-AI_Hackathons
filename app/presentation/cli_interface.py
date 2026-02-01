"""
CLI Interface - Presentation Layer

Handles console user interaction for the Todo application.
"""

from typing import List, Optional
from app.domain.todo import Todo
from app.domain.todo_service import TodoService
from app.utils.validators import validate_todo_title, validate_positive_integer


class CLIInterface:
    """
    Console interface for the Todo application.

    Handles user input/output and translates commands to service calls.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI interface with a todo service.

        Args:
            todo_service (TodoService): The service to use for todo operations
        """
        self.todo_service = todo_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("TODO APPLICATION - MAIN MENU")
        print("="*50)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Complete Todo")
        print("5. Delete Todo")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's choice as a string
        """
        return input("Enter your choice (1-6): ").strip()

    def handle_add_todo(self):
        """Handle the add todo operation."""
        print("\n--- ADD TODO ---")
        title = input("Enter todo title: ").strip()

        if not validate_todo_title(title):
            print("Error: Title cannot be empty or whitespace-only.")
            return

        description = input("Enter description (optional): ").strip()

        try:
            todo_id = self.todo_service.create_todo(title, description)
            print(f"Success: Todo added with ID {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_todos(self):
        """Handle the view todos operation."""
        print("\n--- VIEW TODOS ---")
        todos = self.todo_service.get_todo_list()

        if not todos:
            print("No todos found.")
            return

        print(f"Found {len(todos)} todo(s):")
        print("-" * 60)
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"[{status}] ID: {todo.id} | Title: {todo.title}")
            if todo.description:
                print(f"    Description: {todo.description}")
            print(f"    Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 60)

    def handle_update_todo(self):
        """Handle the update todo operation."""
        print("\n--- UPDATE TODO ---")
        todos = self.todo_service.get_todo_list()

        if not todos:
            print("No todos found to update.")
            return

        self.display_todos_list(todos)

        todo_id_str = input("Enter the ID of the todo to update: ").strip()

        if not validate_positive_integer(todo_id_str):
            print("Error: Please enter a valid positive integer for the ID.")
            return

        todo_id = int(todo_id_str)
        new_title = input("Enter the new title: ").strip()

        if not validate_todo_title(new_title):
            print("Error: Title cannot be empty or whitespace-only.")
            return

        success = self.todo_service.update_todo(todo_id, new_title)
        if success:
            print(f"Success: Todo {todo_id} updated successfully.")
        else:
            print(f"Error: Failed to update todo with ID {todo_id}. It may not exist.")

    def handle_complete_todo(self):
        """Handle the complete todo operation."""
        print("\n--- COMPLETE TODO ---")
        todos = self.todo_service.get_todo_list()

        if not todos:
            print("No todos found to complete.")
            return

        self.display_todos_list(todos)

        todo_id_str = input("Enter the ID of the todo to complete: ").strip()

        if not validate_positive_integer(todo_id_str):
            print("Error: Please enter a valid positive integer for the ID.")
            return

        todo_id = int(todo_id_str)
        success = self.todo_service.complete_todo(todo_id)
        if success:
            print(f"Success: Todo {todo_id} marked as complete.")
        else:
            print(f"Error: Failed to complete todo with ID {todo_id}. It may not exist.")

    def handle_delete_todo(self):
        """Handle the delete todo operation."""
        print("\n--- DELETE TODO ---")
        todos = self.todo_service.get_todo_list()

        if not todos:
            print("No todos found to delete.")
            return

        self.display_todos_list(todos)

        todo_id_str = input("Enter the ID of the todo to delete: ").strip()

        if not validate_positive_integer(todo_id_str):
            print("Error: Please enter a valid positive integer for the ID.")
            return

        todo_id = int(todo_id_str)
        success = self.todo_service.delete_todo(todo_id)
        if success:
            print(f"Success: Todo {todo_id} deleted successfully.")
        else:
            print(f"Error: Failed to delete todo with ID {todo_id}. It may not exist.")

    def display_todos_list(self, todos: List[Todo]):
        """Display a formatted list of todos."""
        if not todos:
            print("No todos found.")
            return

        print(f"Current todos ({len(todos)} total):")
        print("-" * 60)
        for todo in todos:
            status = "✓ Completed" if todo.completed else "○ Pending"
            print(f"ID: {todo.id} | [{status}] | Title: {todo.title}")
            if todo.description:
                print(f"  Description: {todo.description}")
        print("-" * 60)

    def handle_exit(self):
        """Handle the exit operation."""
        print("\nThank you for using the Todo Application!")
        print("Goodbye!")

    def display_error_message(self, message: str):
        """
        Display an error message to the user.

        Args:
            message (str): The error message to display
        """
        print(f"\nError: {message}")
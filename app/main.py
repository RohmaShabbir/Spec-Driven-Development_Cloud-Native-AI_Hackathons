"""
Todo Application - Main Entry Point

Entry point for the console-based Todo application.
"""

from app.domain.todo_service import TodoService
from app.infrastructure.memory_repository import MemoryRepository
from app.presentation.cli_interface import CLIInterface


def main():
    """
    Main function to run the Todo application.

    Initializes all components and runs the main application loop.
    """
    # Initialize the infrastructure layer
    repository = MemoryRepository()

    # Initialize the domain layer
    todo_service = TodoService(repository)

    # Initialize the presentation layer
    cli_interface = CLIInterface(todo_service)

    # Run the application loop
    print("Welcome to the Todo Application!")

    while True:
        cli_interface.display_menu()
        choice = cli_interface.get_user_choice()

        if choice == "1":
            cli_interface.handle_add_todo()
        elif choice == "2":
            cli_interface.handle_view_todos()
        elif choice == "3":
            cli_interface.handle_update_todo()
        elif choice == "4":
            cli_interface.handle_complete_todo()
        elif choice == "5":
            cli_interface.handle_delete_todo()
        elif choice == "6":
            cli_interface.handle_exit()
            break
        else:
            cli_interface.display_error_message(
                "Invalid choice. Please enter a number between 1 and 6."
            )

        # Pause to let user see the result before showing the menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
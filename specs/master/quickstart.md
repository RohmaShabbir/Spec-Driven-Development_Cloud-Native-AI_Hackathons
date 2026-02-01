# Quickstart Guide: Todo Application - Phase I

## Prerequisites

- Python 3.13+ installed
- UV package manager installed

## Setup

1. Clone the repository (if applicable):
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Install dependencies (UV environment):
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## Running the Application

To run the Todo application:

```bash
python app/main.py
```

Or with explicit Python path:

```bash
PYTHONPATH=. python app/main.py
```

## Using the Application

Once started, the application will display a console menu with the following options:

1. **Add Todo**: Enter a new task title to create a todo
2. **View Todos**: Display all current todos with their status
3. **Update Todo**: Select a todo by ID and provide a new title
4. **Complete Todo**: Mark a todo as completed by selecting its ID
5. **Delete Todo**: Remove a todo by selecting its ID
6. **Exit**: Quit the application

### Example Workflow

1. Start the application: `python app/main.py`
2. Choose "Add Todo" and enter "Buy groceries"
3. Choose "View Todos" to see your list
4. Choose "Complete Todo" and select the grocery task
5. Choose "View Todos" to confirm completion
6. Choose "Exit" to close the application

## Troubleshooting

- If you get a "command not found" error for UV, ensure UV is installed: `pip install uv`
- If Python 3.13+ is not available, install the latest Python version
- If the application fails to start, ensure you're running from the project root directory

## Architecture Overview

The application follows a clean architecture pattern:
- **Domain Layer**: Contains the Todo entity and business logic
- **Infrastructure Layer**: Handles in-memory storage
- **Presentation Layer**: Manages console user interface
- **Utils**: Provides helper functions like input validation

## Development

To modify the application:
1. Edit files in the `app/` directory following the layered architecture
2. Test changes by running the application
3. Ensure all functionality remains intact after modifications
# API Contracts: Todo Application - Phase I

## Console Interface Contracts

### Add Todo Operation
- **Command**: User selects "Add Todo" option from menu
- **Input**: String containing task title
- **Validation**: Title must not be empty or whitespace-only
- **Output**: Success message with assigned ID, or error message
- **State Change**: New Todo object added to in-memory repository

### View Todos Operation
- **Command**: User selects "View Todos" option from menu
- **Input**: None required
- **Output**: Formatted list of all Todo objects with ID, title, and completion status
- **State Change**: None

### Update Todo Operation
- **Command**: User selects "Update Todo" option from menu
- **Input**: Integer ID and new title string
- **Validation**: ID must exist, title must not be empty
- **Output**: Success confirmation or error message
- **State Change**: Todo object's title updated in repository

### Complete Todo Operation
- **Command**: User selects "Complete Todo" option from menu
- **Input**: Integer ID
- **Validation**: ID must exist
- **Output**: Success confirmation or error message
- **State Change**: Todo object's completed status set to True

### Delete Todo Operation
- **Command**: User selects "Delete Todo" option from menu
- **Input**: Integer ID
- **Validation**: ID must exist
- **Output**: Success confirmation or error message
- **State Change**: Todo object removed from repository

## Internal Service Contracts

### TodoService.create_todo(title: str, description: str = "") -> int
- **Precondition**: Title is non-empty string
- **Postcondition**: New Todo exists in repository with unique ID
- **Return**: Assigned ID (positive integer) or raises exception on validation failure

### TodoService.get_todo_list() -> List[Todo]
- **Precondition**: None
- **Postcondition**: None
- **Return**: List of all Todo objects (empty list if none exist)

### TodoService.update_todo(id: int, new_title: str) -> bool
- **Precondition**: ID exists in repository, title is non-empty
- **Postcondition**: Todo with specified ID has updated title
- **Return**: True on success, False on failure (invalid ID or title)

### TodoService.complete_todo(id: int) -> bool
- **Precondition**: ID exists in repository
- **Postcondition**: Todo with specified ID has completed=True
- **Return**: True on success, False on failure (invalid ID)

### TodoService.delete_todo(id: int) -> bool
- **Precondition**: ID exists in repository
- **Postcondition**: Todo with specified ID removed from repository
- **Return**: True on success, False on failure (invalid ID)

### TodoService.validate_input(title: str) -> bool
- **Precondition**: None
- **Postcondition**: None
- **Return**: True if title is valid (non-empty, non-whitespace), False otherwise
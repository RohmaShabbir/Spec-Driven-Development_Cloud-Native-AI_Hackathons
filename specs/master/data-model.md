# Data Model: Todo Application - Phase I

## Todo Entity

### Attributes
- **id**: `int` (auto-incremented unique identifier)
- **title**: `str` (non-empty task description)
- **description**: `str` (optional additional details)
- **completed**: `bool` (task completion status, default: False)
- **created_at**: `datetime` (timestamp of creation, optional)

### Validation Rules
- `id` must be unique within the application session
- `title` must not be empty or whitespace-only
- `completed` defaults to `False` when creating new todos
- `created_at` is set automatically when creating new todos

### State Transitions
- `completed` can transition from `False` to `True` (complete operation)
- `completed` cannot transition from `True` back to `False` (based on specification)
- `title` can be updated while maintaining other attributes (update operation)

## Todo Repository Interface

### Operations
- `add(todo: Todo) -> int`: Adds a new todo and returns its ID
- `get_by_id(id: int) -> Todo | None`: Retrieves a todo by ID or None if not found
- `get_all() -> List[Todo]`: Returns all todos in the repository
- `update(id: int, title: str) -> bool`: Updates a todo's title, returns success status
- `delete(id: int) -> bool`: Removes a todo by ID, returns success status
- `complete(id: int) -> bool`: Marks a todo as complete, returns success status

### Business Rules
- Repository enforces ID uniqueness
- Repository validates that operations target existing todos
- Repository maintains data integrity during operations

## Todo Service Interface

### Operations
- `create_todo(title: str, description: str = "") -> int`: Creates a new todo with validation
- `get_todo_list() -> List[Todo]`: Retrieves all todos
- `update_todo(id: int, new_title: str) -> bool`: Updates a todo with validation
- `delete_todo(id: int) -> bool`: Deletes a todo with validation
- `complete_todo(id: int) -> bool`: Marks a todo as complete with validation
- `validate_input(title: str) -> bool`: Validates user input

### Business Rules
- Service validates all inputs before passing to repository
- Service enforces domain rules (e.g., non-empty titles)
- Service provides success/failure status for all operations
- Service handles error cases gracefully
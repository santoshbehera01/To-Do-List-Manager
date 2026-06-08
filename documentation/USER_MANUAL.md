# User Manual – To-Do List Manager

Welcome! This guide explains every feature of the **To-Do List Manager –
Personal Productivity Dashboard**.

## 1. Installation

1. Install **Python 3.8 or higher** from <https://python.org>.
2. Download or clone the `To-Do-List` folder.
3. Open a terminal in that folder and run:
   ```bash
   python main.py
   ```

No additional libraries are required — Tkinter ships with Python.

## 2. The Main Window

When the app launches you will see:

- **Sidebar (left)** — navigation between pages.
- **Header (top)** — current page title and today's date.
- **Content area** — the active page.
- **Status bar (bottom)** — current state of the app.

## 3. Pages

### 3.1 Dashboard
The home page. Displays:
- Total Tasks
- Pending Tasks
- Completed Tasks
- High Priority Tasks
- A table of the 10 most recent tasks.

### 3.2 Add Task
Create a new task.

1. Enter a **Task Title** (required).
2. Optionally add a **Description**.
3. Pick a **Priority**: High, Medium, or Low.
4. Enter a **Due Date** in `YYYY-MM-DD` format.
5. Click **Save Task**.

The app validates your input and shows a success dialog when saved.

### 3.3 All Tasks
Displays every task in a scrollable table. Action buttons:

- **Refresh** — reload the table.
- **Edit** — open the selected task in an editor.
- **Mark Complete** — change the status from Pending to Completed.
- **Delete** — remove the selected task (with confirmation).

> Tip: click any row to select it before pressing an action button.

### 3.4 Pending Tasks
Same table as *All Tasks* but filtered to only **Pending** items.

### 3.5 Completed Tasks
Same table as *All Tasks* but filtered to only **Completed** items.

### 3.6 Search Tasks
Find tasks quickly.
- Type part of a title into the search box.
- Optionally pick a priority filter.
- Click **Search** — matching tasks appear below.

### 3.7 Statistics
View overall progress:
- Total / Completed / Pending tasks
- Completion percentage with a visual progress bar
- Tasks grouped by priority

### 3.8 Export Tasks
Click **Export to CSV**, choose a location, and save. The CSV can be
opened in Excel, Numbers, Google Sheets, or any text editor.

## 4. Data Storage

All tasks are saved automatically to `data/tasks.json` whenever you
add, edit, delete, or mark a task complete. There is no manual save —
your data is always up to date.

## 5. Troubleshooting

| Problem                                | Solution                                                        |
| -------------------------------------- | --------------------------------------------------------------- |
| *"Task title cannot be empty"*         | Type something into the Title field.                            |
| *"Due date must follow YYYY-MM-DD"*    | Use the exact format, e.g. `2026-06-15`.                        |
| *"Please select a priority"*           | Pick High, Medium, or Low from the dropdown.                    |
| App does not start                     | Make sure Python 3.8+ is installed and `python main.py` is run. |
| Data file appears corrupted            | Close the app, delete `data/tasks.json`, restart the app.       |

## 6. Keyboard / Mouse Tips

- Click a sidebar item to switch pages.
- Hover over sidebar buttons to see the hover highlight.
- Single-click any row in a table to select it.
- Use the scrollbar to browse long task lists.

## 7. Support

This project was built as an internship / portfolio submission. For
questions, see `documentation/PROJECT_DOC.md` for technical details.

Enjoy your improved productivity! ✅

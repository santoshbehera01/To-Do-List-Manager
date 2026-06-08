# Project Documentation – To-Do List Manager

## 1. Overview

**To-Do List Manager – Personal Productivity Dashboard** is a desktop
application written entirely in Python 3 using the Tkinter GUI toolkit.
It provides a modern dashboard interface for capturing, organizing, and
tracking personal tasks, with persistent JSON storage and CSV export.

The project was designed as an internship-submission and
portfolio-ready application that demonstrates:

- Object-oriented application architecture
- Modular, well-commented Python code
- Modern UI design using only standard Tkinter widgets
- Proper exception handling and input validation
- File I/O with JSON and CSV
- Zero third-party dependencies

## 2. Objectives

1. Provide an intuitive interface for daily task management.
2. Demonstrate professional-quality Tkinter UI design.
3. Persist data reliably between sessions.
4. Showcase clean, PEP 8-compliant Python code.

## 3. Architecture

The application uses a single-file implementation organized around a
central `ToDoApp` class that owns:

- **Data layer** — JSON read/write helpers (`load_tasks`, `save_tasks`)
- **Layout layer** — sidebar, header, content, and status bar containers
- **Page layer** — one render method per page (`page_dashboard`, etc.)
- **Reusable UI helpers** — cards, buttons, treeviews, edit dialog

```
┌────────────────────────────────────────────────────────────┐
│  ToDoApp (Tk root)                                         │
│  ┌──────────┐  ┌─────────────────────────────────────────┐ │
│  │ Sidebar  │  │ Header                                  │ │
│  │ (nav)    │  ├─────────────────────────────────────────┤ │
│  │          │  │ Content (active page)                   │ │
│  │          │  │                                         │ │
│  └──────────┘  └─────────────────────────────────────────┘ │
│                Status bar                                  │
└────────────────────────────────────────────────────────────┘
```

## 4. Data Model

Each task is stored as a JSON object:

```json
{
    "title": "Complete Internship Project",
    "description": "Finish To-Do List application",
    "priority": "High",
    "due_date": "2026-06-15",
    "status": "Pending"
}
```

`data/tasks.json` is a JSON array of such objects and is created
automatically on first launch.

## 5. Module / Function Reference

| Function                | Responsibility                                       |
| ----------------------- | ---------------------------------------------------- |
| `_ensure_data_storage`  | Creates `data/` and `tasks.json` if missing          |
| `load_tasks`            | Reads tasks from JSON, handles read errors          |
| `save_tasks`            | Writes tasks to JSON (auto-save)                     |
| `_configure_ttk_style`  | Configures the modern Treeview / Combobox styling    |
| `_build_layout`         | Builds sidebar, header, content, status bar          |
| `_build_sidebar`        | Creates nav buttons with hover effects               |
| `show_page`             | Switches active page and highlights nav button       |
| `page_dashboard`        | Renders KPI cards + recent tasks                     |
| `page_add_task`         | Renders the add-task form with validation            |
| `page_all_tasks`        | Renders the full task table                          |
| `page_pending`          | Filtered table — Pending only                        |
| `page_completed`        | Filtered table — Completed only                      |
| `page_search`           | Search by title + filter by priority                 |
| `page_statistics`       | KPI cards, completion % bar, priority breakdown      |
| `page_export`           | Exports tasks to CSV via native file dialog          |
| `_open_edit_dialog`     | Modal dialog for editing a task                      |

## 6. Validation Rules

- Title cannot be empty.
- Due date must follow `YYYY-MM-DD` (validated with `datetime.strptime`).
- Priority must be one of: `High`, `Medium`, `Low`.
- Status must be one of: `Pending`, `Completed`.
- All errors are presented via friendly `messagebox` dialogs.

## 7. Error Handling

- File I/O is wrapped in `try / except OSError` and
  `json.JSONDecodeError`.
- Missing data file triggers automatic creation rather than a crash.
- User-facing errors use `messagebox.showerror` or `showwarning`.

## 8. UI / UX Design

| Element              | Color (Hex) | Purpose                     |
| -------------------- | ----------- | --------------------------- |
| Sidebar              | `#1e293b`   | Persistent navigation       |
| Sidebar active item  | `#2563eb`   | Current-page indicator      |
| Header               | `#2563eb`   | Brand identity              |
| Background           | `#f1f5f9`   | Page surface                |
| Card                 | `#ffffff`   | Content container           |
| Success              | `#10b981`   | Completion / save actions   |
| Warning              | `#f59e0b`   | Pending tasks               |
| Danger               | `#ef4444`   | High priority / delete      |
| Status bar           | `#0f172a`   | Footer information          |

Typography: **Segoe UI** across all widgets.

## 9. Future Enhancements

- Task categories / tags
- Drag-and-drop reordering
- Reminders & notifications
- Cloud sync (Google Drive / Dropbox)
- Light / Dark theme switching
- Multi-user profiles

## 10. License

MIT License — free for personal, educational, and portfolio use.

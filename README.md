# To-Do List Manager – Personal Productivity Dashboard

A modern, dashboard-style desktop application for managing daily tasks,
built with **Python 3** and **Tkinter** using only the standard library.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production-success)

---

## ✨ Features

- 🏠 **Dashboard** with statistics cards and a recent-tasks table
- ➕ **Add Task** with title, description, priority, and due date
- 📋 **All Tasks** view with a professional `Treeview` table and scrollbar
- ⏳ **Pending Tasks** view
- ✅ **Completed Tasks** view
- ✏️ **Edit** and 🗑 **Delete** any task
- ✔️ **Mark Complete** to change task status
- 🔍 **Search** by title and filter by priority
- 📊 **Statistics** with completion percentage and priority breakdown
- 💾 **Export to CSV** with a native file dialog
- 💽 **Auto-save** to `data/tasks.json` after every change

## 🎨 Design Highlights

- Dark sidebar navigation with hover effects and active-state highlighting
- Colored header section with the current date
- Modern dashboard cards with accent strips
- Clean typography using **Segoe UI**
- Status bar at the bottom of the window
- Consistent, professional color theme

## 🖥️ Tech Stack

| Component         | Technology              |
| ----------------- | ----------------------- |
| Language          | Python 3.8+             |
| GUI Framework     | Tkinter (stdlib)        |
| Data Storage      | JSON (`data/tasks.json`)|
| Export Format     | CSV                     |
| Dependencies      | None (stdlib only)      |

## 📁 Project Structure

```
To-Do-List/
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   └── tasks.json
│
├── assets/
│   └── icons/
│
├── documentation/
│   ├── PROJECT_DOC.md
│   └── USER_MANUAL.md
│
└── screenshots/
```

## 🚀 Getting Started

### Prerequisites
- Python **3.8 or higher** (Tkinter ships with the standard installer)

### Run the application
```bash
cd To-Do-List
python main.py
```

The application opens on the **Dashboard** page. The `data/tasks.json`
file is created automatically on first launch.

## 📖 Documentation

- [PROJECT_DOC.md](documentation/PROJECT_DOC.md) — architecture & technical doc
- [USER_MANUAL.md](documentation/USER_MANUAL.md) — end-user guide

## 📝 License

Released under the MIT License — free for personal and educational use.

---

*Built as a professional internship-ready portfolio project.*

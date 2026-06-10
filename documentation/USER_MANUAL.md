# User Manual – To-Do List Manager

## Project Information

**Project Name:** To-Do List Manager

**Intern Name:** Santosh Kumar Behera

**Intern ID:** CITS2854

**Domain:** Python Programming

---

## 1. Starting the Application

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

3. The application will open on the **Dashboard** page.

---

## 2. Application Layout

The main window consists of:

- **Sidebar** – Navigation menu
- **Header** – Current page title and date
- **Content Area** – Active page content
- **Status Bar** – Application status information

---

## 3. Features and Usage

### Dashboard

The Dashboard provides an overview of:

- Total Tasks
- Pending Tasks
- Completed Tasks
- High Priority Tasks
- Recent Tasks List

---

### Add Task

1. Select **Add Task** from the sidebar.
2. Enter:
   - Task Title
   - Description
   - Priority
   - Due Date (`YYYY-MM-DD`)
3. Click **Save Task**.

---

### All Tasks

This page displays all saved tasks.

Available actions:

- Refresh Tasks
- Edit Task
- Mark Complete
- Delete Task

---

### Pending Tasks

Displays only tasks with **Pending** status.

---

### Completed Tasks

Displays only tasks with **Completed** status.

---

### Search Tasks

1. Enter a keyword.
2. Select a priority filter (optional).
3. Click **Search**.

Matching tasks will be displayed instantly.

---

### Statistics

Provides:

- Total Task Count
- Pending Task Count
- Completed Task Count
- Completion Percentage
- Priority-wise Breakdown

---

### Export Tasks

1. Open **Export Tasks**.
2. Click **Export to CSV**.
3. Select a location and save the file.

---

## 4. Data Storage

All task records are stored in:

```text
data/tasks.json
```

The file is created automatically when the application runs for the first time.

All changes are saved automatically.

---

## 5. Troubleshooting

| Problem | Solution |
|----------|----------|
| Application does not start | Verify Python 3.8 or higher is installed. |
| Task title is empty | Enter a valid task title before saving. |
| Invalid due date | Use the format `YYYY-MM-DD`. |
| Priority not selected | Choose High, Medium, or Low priority. |
| Missing data file | Restart the application. A new JSON file will be created automatically. |

---

## 6. Conclusion

The To-Do List Manager helps users organize daily activities, track task progress, and improve productivity through a simple and professional desktop interface.

This project was developed as part of the Python Programming Internship at CODTECH IT Solutions Pvt. Ltd.
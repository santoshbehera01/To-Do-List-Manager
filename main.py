"""
To-Do List Manager - Personal Productivity Dashboard
====================================================
A modern dashboard-style desktop application for managing daily tasks.

Author: Internship Project
Tech:   Python 3 + Tkinter (Standard Library only)
File:   main.py
"""

import json
import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# ---------------------------------------------------------------------------
# Theme & Constants
# ---------------------------------------------------------------------------
APP_TITLE = "To-Do-List Manager"
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")

# Modern dashboard theme
COLOR_BG = "#f8fafc"
COLOR_PRIMARY = "#6D28D9"
COLOR_SECONDARY = "#4F46E5"
COLOR_SUCCESS = "#16a34a"
COLOR_WARNING = "#f59e0b"
COLOR_DANGER = "#ef4444"
COLOR_CARD = "#ffffff"
COLOR_BORDER = "#e5e7eb"
COLOR_TEXT = "#0f172a"
COLOR_MUTED = "#475569"
COLOR_NAV_TEXT = "#475569"
COLOR_NAV_ACTIVE = "#4F46E5"
COLOR_NAV_BG = COLOR_BG
COLOR_FOOTER = "#eef2ff"

FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 22, "bold")
FONT_HEADER = (FONT_FAMILY, 18, "bold")
FONT_BODY = (FONT_FAMILY, 11)
FONT_BODY_BOLD = (FONT_FAMILY, 11, "bold")
FONT_CARD_VALUE = (FONT_FAMILY, 26, "bold")
FONT_CARD_LABEL = (FONT_FAMILY, 10)


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------
class ToDoApp:
    """Main application class for the To-Do List Manager."""

    # ----- Initialization -------------------------------------------------
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1200x720")
        self.root.minsize(1000, 620)
        self.root.configure(bg=COLOR_BG)

        self.tasks = []
        self.nav_buttons = {}
        self.current_page = None

        self._ensure_data_storage()
        self.load_tasks()
        self._configure_ttk_style()
        self._build_layout()

        # Start on Dashboard
        self.show_page("Dashboard")

    # ----- Data Storage ---------------------------------------------------
    def _ensure_data_storage(self):
        """Create data folder and tasks.json if missing."""
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
            if not os.path.exists(DATA_FILE):
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)
        except OSError as e:
            messagebox.showerror("Storage Error",
                                 f"Could not initialize data folder:\n{e}")

    def load_tasks(self):
        """Load tasks from JSON file."""
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except (OSError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        """Persist tasks to JSON file (auto-save)."""
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=4)
        except OSError as e:
            messagebox.showerror("Save Error", f"Could not save tasks:\n{e}")

    # ----- Style ---------------------------------------------------------
    def _configure_ttk_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Modern.Treeview",
            background=COLOR_CARD,
            foreground=COLOR_TEXT,
            rowheight=32,
            fieldbackground=COLOR_CARD,
            font=FONT_BODY,
            borderwidth=0,
        )
        style.configure(
            "Modern.Treeview.Heading",
            background=COLOR_BG,
            foreground=COLOR_TEXT,
            font=FONT_BODY_BOLD,
            relief="flat",
            borderwidth=0,
            padding=10,
        )
        style.map("Modern.Treeview",
                  background=[("selected", COLOR_PRIMARY)],
                  foreground=[("selected", "#ffffff")])
        style.map("Modern.Treeview.Heading",
                  background=[("active", "#e0dcff")])

        style.configure("TCombobox",
                        padding=6,
                        relief="flat",
                        selectbackground=COLOR_CARD,
                        fieldbackground=COLOR_CARD,
                        background=COLOR_CARD,
                        foreground=COLOR_TEXT,
                        font=FONT_BODY)

    # ----- Layout --------------------------------------------------------
    def _build_layout(self):
        self.navbar = tk.Frame(self.root, bg=COLOR_BG, height=72)
        self.navbar.pack(side="top", fill="x")
        self.navbar.pack_propagate(False)

        brand = tk.Frame(self.navbar, bg=COLOR_BG)
        brand.pack(side="left", padx=24, pady=12)
        tk.Label(brand, text="TaskFlow", bg=COLOR_BG,
                 fg=COLOR_TEXT, font=(FONT_FAMILY, 22, "bold")).pack(
                     anchor="w")
        tk.Label(brand, text="Modern Task Management", bg=COLOR_BG,
                 fg=COLOR_MUTED, font=FONT_BODY).pack(anchor="w")

        nav_frame = tk.Frame(self.navbar, bg=COLOR_BG)
        nav_frame.pack(side="left", padx=40)
        nav_items = [
            ("Dashboard", "🏠"),
            ("Tasks", "🗂️"),
            ("Completed", "✅"),
            ("Statistics", "📊"),
            ("Search", "🔍"),
            ("Export", "💾"),
        ]
        for name, icon in nav_items:
            self._make_nav_button(nav_frame, name, icon)

        self.header = tk.Frame(self.root, bg=COLOR_BG, height=120)
        self.header.pack(side="top", fill="x")
        self.header.pack_propagate(False)

        left_header = tk.Frame(self.header, bg=COLOR_BG)
        left_header.pack(side="left", padx=24, pady=16, fill="both", expand=True)
        self.header_title = tk.Label(left_header, text="Dashboard",
                                     bg=COLOR_BG, fg=COLOR_TEXT,
                                     font=FONT_TITLE)
        self.header_title.pack(anchor="w")
        self.header_sub = tk.Label(left_header,
                                   text=datetime.now().strftime("%A, %d %B %Y"),
                                   bg=COLOR_BG, fg=COLOR_MUTED,
                                   font=FONT_BODY)
        self.header_sub.pack(anchor="w", pady=(8, 0))

        right_header = tk.Frame(self.header, bg=COLOR_BG)
        right_header.pack(side="right", padx=24, pady=16)
        self.summary_label = tk.Label(right_header,
                                      text="0 tasks • 0 pending • 0 completed",
                                      bg=COLOR_BG, fg=COLOR_TEXT,
                                      font=FONT_BODY_BOLD)
        self.summary_label.pack(anchor="e")

        divider = tk.Frame(self.root, bg=COLOR_BORDER, height=1)
        divider.pack(fill="x")

        self.content = tk.Frame(self.root, bg=COLOR_BG)
        self.content.pack(fill="both", expand=True, padx=24, pady=(18, 0))

        footer = tk.Frame(self.root, bg=COLOR_FOOTER, height=32)
        footer.pack(side="bottom", fill="x")
        footer.pack_propagate(False)
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(footer, textvariable=self.status_var, bg=COLOR_FOOTER,
                 fg=COLOR_TEXT, font=FONT_BODY).pack(side="left", padx=20)
        self.task_count_var = tk.StringVar(value=f"{len(self.tasks)} tasks loaded")
        tk.Label(footer, textvariable=self.task_count_var, bg=COLOR_FOOTER,
                 fg=COLOR_MUTED, font=FONT_BODY).pack(side="right", padx=20)

    def _build_sidebar(self):
        pass

    def _make_nav_button(self, parent, name, icon):
        btn = tk.Label(parent, text=f"{icon}  {name}", bg=COLOR_NAV_BG,
                       fg=COLOR_NAV_TEXT, font=FONT_BODY_BOLD,
                       padx=16, pady=14, cursor="hand2")
        btn.pack(side="left", padx=8)

        def on_enter(_e, b=btn):
            if self.current_page != name:
                b.configure(bg="#f3f4ff")

        def on_leave(_e, b=btn):
            if self.current_page != name:
                b.configure(bg=COLOR_NAV_BG)

        def on_click(_e, n=name):
            self.show_page(n)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<Button-1>", on_click)
        self.nav_buttons[name] = btn

    # ----- Navigation ----------------------------------------------------
    def show_page(self, name):
        self.current_page = name
        for n, b in self.nav_buttons.items():
            if n == name:
                b.configure(bg=COLOR_NAV_ACTIVE, fg="#ffffff")
            else:
                b.configure(bg=COLOR_NAV_BG, fg=COLOR_NAV_TEXT)

        self.header_title.configure(text=name)
        self.header_sub.configure(text=datetime.now().strftime("%A, %d %B %Y"))
        self._refresh_header_summary()
        for w in self.content.winfo_children():
            w.destroy()

        pages = {
            "Dashboard": self.page_dashboard,
            "Tasks": self.page_tasks,
            "Completed": self.page_completed,
            "Statistics": self.page_statistics,
            "Search": self.page_search,
            "Export": self.page_export,
            "Add Task": self.page_add_task,
        }
        pages.get(name, self.page_dashboard)()
        self.set_status(f"Viewing {name}")

    def _refresh_header_summary(self):
        total = len(self.tasks)
        pending = sum(1 for t in self.tasks if t["status"] == "Pending")
        completed = sum(1 for t in self.tasks if t["status"] == "Completed")
        self.summary_label.configure(
            text=f"{total} tasks • {pending} pending • {completed} done")
        self.task_count_var.set(f"{total} tasks loaded")

    def set_status(self, msg):
        self.status_var.set(msg)

    # ----- Reusable UI ---------------------------------------------------
    def _section_title(self, parent, text):
        tk.Label(parent, text=text, bg=COLOR_BG, fg=COLOR_TEXT,
                 font=FONT_HEADER).pack(anchor="w", padx=24, pady=(20, 10))

    def _make_card(self, parent, label, value, accent):
        card = tk.Frame(parent, bg=COLOR_CARD, highlightbackground=COLOR_BORDER,
                        highlightthickness=1)
        # Accent strip
        tk.Frame(card, bg=accent, height=4).pack(fill="x")
        inner = tk.Frame(card, bg=COLOR_CARD)
        inner.pack(fill="both", expand=True, padx=20, pady=16)
        tk.Label(inner, text=label, bg=COLOR_CARD, fg=COLOR_MUTED,
                 font=FONT_CARD_LABEL).pack(anchor="w")
        tk.Label(inner, text=str(value), bg=COLOR_CARD, fg=accent,
                 font=FONT_CARD_VALUE).pack(anchor="w", pady=(6, 0))
        return card

    def _primary_button(self, parent, text, command, bg=COLOR_PRIMARY):
        b = tk.Button(parent, text=text, command=command,
                      bg=bg, fg="#ffffff", activebackground=COLOR_SECONDARY,
                      activeforeground="#ffffff", relief="flat",
                      font=FONT_BODY_BOLD, padx=18, pady=8,
                      cursor="hand2", borderwidth=0)
        return b

    def _secondary_button(self, parent, text, command, bg="#eef2ff", fg=COLOR_TEXT):
        b = tk.Button(parent, text=text, command=command,
                      bg=bg, fg=fg, activebackground="#dbeafe",
                      activeforeground=COLOR_TEXT, relief="flat",
                      font=FONT_BODY_BOLD, padx=16, pady=8,
                      cursor="hand2", borderwidth=0)
        return b

    def _make_badge(self, parent, text, bg, fg="#ffffff"):
        badge = tk.Frame(parent, bg=bg, padx=10, pady=4)
        tk.Label(badge, text=text, bg=bg, fg=fg,
                 font=(FONT_FAMILY, 9, "bold")).pack()
        return badge

    def _make_treeview(self, parent, columns, widths=None):
        wrapper = tk.Frame(parent, bg=COLOR_BG)
        widths = widths or [120] * len(columns)
        tree = ttk.Treeview(wrapper, columns=columns, show="headings",
                            style="Modern.Treeview")
        for col, w in zip(columns, widths):
            tree.heading(col, text=col)
            tree.column(col, width=w, anchor="w")
        vsb = ttk.Scrollbar(wrapper, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        return wrapper, tree

    def _priority_color(self, priority):
        return {
            "High": COLOR_DANGER,
            "Medium": COLOR_WARNING,
            "Low": COLOR_SUCCESS,
        }.get(priority, COLOR_MUTED)

    def _task_card(self, parent, task):
        card = tk.Frame(parent, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER,
                        highlightthickness=1)
        card.pack(fill="x", pady=10)

        header = tk.Frame(card, bg=COLOR_CARD)
        header.pack(fill="x", padx=20, pady=(16, 8))
        tk.Label(header, text=task["title"], bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_BODY_BOLD).pack(side="left")

        badge_frame = tk.Frame(header, bg=COLOR_CARD)
        badge_frame.pack(side="right")
        self._make_badge(badge_frame, task["priority"], self._priority_color(task["priority"]) ).pack(side="right")
        self._make_badge(badge_frame, task["status"], COLOR_SUCCESS if task["status"] == "Completed" else COLOR_WARNING).pack(side="right", padx=(0, 8))

        meta = tk.Frame(card, bg=COLOR_CARD)
        meta.pack(fill="x", padx=20)
        tk.Label(meta, text=f"Due {task['due_date']}", bg=COLOR_CARD,
                 fg=COLOR_MUTED, font=FONT_BODY).pack(side="left")

        if task.get("description"):
            description = task["description"].strip().replace("\n", " ")
            if len(description) > 120:
                description = description[:120].rstrip() + "..."
            tk.Label(card, text=description, bg=COLOR_CARD, fg=COLOR_MUTED,
                     font=FONT_BODY, wraplength=920, justify="left").pack(
                         fill="x", padx=20, pady=(10, 0))

        actions = tk.Frame(card, bg=COLOR_CARD)
        actions.pack(fill="x", padx=20, pady=16)

        def delete_task():
            if messagebox.askyesno("Delete", "Delete this task?"):
                index = self.tasks.index(task)
                del self.tasks[index]
                self.save_tasks()
                self.show_page(self.current_page)

        def edit_task():
            index = self.tasks.index(task)
            self._open_edit_dialog(index)

        def complete_task():
            index = self.tasks.index(task)
            self.tasks[index]["status"] = "Completed"
            self.save_tasks()
            self.show_page(self.current_page)

        self._secondary_button(actions, "✏️ Edit", edit_task).pack(side="left")
        if task["status"] != "Completed":
            self._primary_button(actions, "✅ Complete", complete_task, bg=COLOR_SUCCESS).pack(side="left", padx=8)
        self._secondary_button(actions, "🗑 Delete", delete_task, bg="#fde8e8", fg=COLOR_DANGER).pack(side="left", padx=8)

    # ----- Pages ---------------------------------------------------------
    def page_dashboard(self):
        total = len(self.tasks)
        pending = sum(1 for t in self.tasks if t["status"] == "Pending")
        completed = sum(1 for t in self.tasks if t["status"] == "Completed")
        high = sum(1 for t in self.tasks if t["priority"] == "High")
        overdue = sum(1 for t in self.tasks if t["status"] == "Pending" and t["due_date"] < datetime.now().strftime("%Y-%m-%d"))

        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True)

        cards = tk.Frame(wrap, bg=COLOR_BG)
        cards.pack(fill="x", pady=(0, 20))
        stats = [
            ("Total Tasks", total, COLOR_PRIMARY, "🗂️"),
            ("Pending", pending, COLOR_WARNING, "⏳"),
            ("Completed", completed, COLOR_SUCCESS, "✅"),
            ("High Priority", high, COLOR_DANGER, "⚡"),
        ]
        for i, (label, value, color, icon) in enumerate(stats):
            card = tk.Frame(cards, bg=COLOR_CARD,
                            highlightbackground=COLOR_BORDER,
                            highlightthickness=1)
            card.grid(row=0, column=i, padx=8, sticky="nsew")
            tk.Frame(card, bg=color, height=4).pack(fill="x")
            inner = tk.Frame(card, bg=COLOR_CARD)
            inner.pack(fill="both", expand=True, padx=20, pady=22)
            tk.Label(inner, text=icon, bg=COLOR_CARD, fg=color,
                     font=(FONT_FAMILY, 18)).pack(anchor="w")
            tk.Label(inner, text=label, bg=COLOR_CARD, fg=COLOR_MUTED,
                     font=FONT_BODY_BOLD).pack(anchor="w", pady=(14, 6))
            tk.Label(inner, text=value, bg=COLOR_CARD, fg=COLOR_TEXT,
                     font=FONT_CARD_VALUE).pack(anchor="w")
            cards.grid_columnconfigure(i, weight=1)

        split = tk.Frame(wrap, bg=COLOR_BG)
        split.pack(fill="both", expand=True)

        left = tk.Frame(split, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER,
                        highlightthickness=1)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))
        right = tk.Frame(split, bg=COLOR_CARD,
                         highlightbackground=COLOR_BORDER,
                         highlightthickness=1)
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))

        tk.Label(left, text="Completion Pulse", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_HEADER).pack(anchor="w", padx=24,
                                                       pady=(24, 0))
        pulse = tk.Canvas(left, width=220, height=220, bg=COLOR_CARD,
                          highlightthickness=0)
        pulse.pack(padx=24, pady=24)
        pulse.create_oval(14, 14, 206, 206, outline="#e5e7eb", width=18)
        if total:
            pulse.create_arc(14, 14, 206, 206, start=90,
                             extent=-((completed / total) * 360),
                             style="arc", outline=COLOR_PRIMARY, width=18)
        pulse.create_text(110, 96, text=f"{(completed / total * 100) if total else 0:.0f}%",
                          fill=COLOR_TEXT, font=(FONT_FAMILY, 24, "bold"))
        pulse.create_text(110, 136, text=f"{completed}/{total} completed",
                          fill=COLOR_MUTED, font=FONT_BODY)

        summary = tk.Frame(left, bg=COLOR_CARD)
        summary.pack(fill="x", padx=24, pady=(0, 24))
        for label, value in [
            ("Overdue", overdue),
            ("Due Soon", pending),
        ]:
            row = tk.Frame(summary, bg=COLOR_CARD)
            row.pack(fill="x", pady=10)
            tk.Label(row, text=label, bg=COLOR_CARD, fg=COLOR_MUTED,
                     font=FONT_BODY).pack(side="left")
            tk.Label(row, text=value, bg=COLOR_CARD, fg=COLOR_TEXT,
                     font=FONT_BODY_BOLD).pack(side="right")

        tk.Label(right, text="Recent Tasks", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_HEADER).pack(anchor="w", padx=24,
                                                       pady=(24, 0))
        recent_wrap = tk.Frame(right, bg=COLOR_CARD)
        recent_wrap.pack(fill="both", expand=True, padx=24, pady=24)
        recent = self.tasks[-6:][::-1]
        if not recent:
            tk.Label(recent_wrap, text="No recent tasks yet.", bg=COLOR_CARD,
                     fg=COLOR_MUTED, font=FONT_BODY).pack(pady=40)
        for task in recent:
            mini = tk.Frame(recent_wrap, bg=COLOR_BG,
                            highlightbackground=COLOR_BORDER,
                            highlightthickness=1)
            mini.pack(fill="x", pady=10)
            tk.Label(mini, text=task["title"], bg=COLOR_BG,
                     fg=COLOR_TEXT, font=FONT_BODY_BOLD).pack(
                         anchor="w", padx=16, pady=(12, 4))
            info = tk.Frame(mini, bg=COLOR_BG)
            info.pack(fill="x", padx=16, pady=(0, 12))
            tk.Label(info, text=f"Due {task['due_date']}", bg=COLOR_BG,
                     fg=COLOR_MUTED, font=FONT_BODY).pack(side="left")
            tk.Label(info, text=task["priority"], bg=COLOR_BG,
                     fg=COLOR_TEXT, font=FONT_BODY_BOLD).pack(side="right")

    def page_tasks(self):
        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True)

        header = tk.Frame(wrap, bg=COLOR_BG)
        header.pack(fill="x", pady=(0, 20))
        tk.Label(header, text="Tasks", bg=COLOR_BG, fg=COLOR_TEXT,
                 font=FONT_HEADER).pack(side="left")
        self._primary_button(header, "+ Add Task", lambda: self.show_page("Add Task"), bg=COLOR_PRIMARY).pack(side="right")

        task_area = tk.Frame(wrap, bg=COLOR_BG)
        task_area.pack(fill="both", expand=True)
        if not self.tasks:
            tk.Label(task_area, text="Your task list is empty. Add a task to get started.",
                     bg=COLOR_BG, fg=COLOR_MUTED, font=FONT_BODY).pack(pady=48)
            return
        for task in self.tasks:
            self._task_card(task_area, task)

    def page_add_task(self):
        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        card = tk.Frame(wrap, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER, highlightthickness=1)
        card.pack(fill="x")

        tk.Label(card, text="Create New Task", bg=COLOR_CARD, fg=COLOR_TEXT,
                 font=FONT_HEADER).grid(row=0, column=0, columnspan=2,
                                        sticky="w", padx=20, pady=(20, 10))

        def field_label(text, r):
            tk.Label(card, text=text, bg=COLOR_CARD, fg=COLOR_TEXT,
                     font=FONT_BODY_BOLD).grid(row=r, column=0, sticky="w",
                                               padx=20, pady=(10, 4))

        field_label("Task Title", 1)
        e_title = tk.Entry(card, font=FONT_BODY, relief="solid", bd=1)
        e_title.grid(row=2, column=0, columnspan=2, sticky="ew",
                     padx=20, ipady=6)

        field_label("Description", 3)
        e_desc = tk.Text(card, font=FONT_BODY, height=4, relief="solid", bd=1)
        e_desc.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20)

        field_label("Priority", 5)
        priority_var = tk.StringVar()
        cb_priority = ttk.Combobox(card, textvariable=priority_var,
                                   values=["High", "Medium", "Low"],
                                   state="readonly", font=FONT_BODY)
        cb_priority.grid(row=6, column=0, sticky="ew", padx=(20, 10), ipady=4)

        field_label("Due Date (YYYY-MM-DD)", 5)  # second column header
        # Move due date label to column 1
        card.grid_slaves(row=5, column=0)[0].grid_forget()
        tk.Label(card, text="Priority", bg=COLOR_CARD, fg=COLOR_TEXT,
                 font=FONT_BODY_BOLD).grid(row=5, column=0, sticky="w",
                                           padx=20, pady=(10, 4))
        tk.Label(card, text="Due Date (YYYY-MM-DD)", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_BODY_BOLD).grid(
            row=5, column=1, sticky="w", padx=10, pady=(10, 4))
        e_due = tk.Entry(card, font=FONT_BODY, relief="solid", bd=1)
        e_due.grid(row=6, column=1, sticky="ew", padx=(10, 20), ipady=6)
        e_due.insert(0, datetime.now().strftime("%Y-%m-%d"))

        card.grid_columnconfigure(0, weight=1)
        card.grid_columnconfigure(1, weight=1)

        # Buttons
        btn_row = tk.Frame(card, bg=COLOR_CARD)
        btn_row.grid(row=7, column=0, columnspan=2, sticky="e",
                     padx=20, pady=20)

        def save():
            title = e_title.get().strip()
            desc = e_desc.get("1.0", "end").strip()
            priority = priority_var.get()
            due = e_due.get().strip()

            if not title:
                messagebox.showerror("Validation", "Task title cannot be empty.")
                return
            if priority not in ("High", "Medium", "Low"):
                messagebox.showerror("Validation", "Please select a priority.")
                return
            try:
                datetime.strptime(due, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation",
                                     "Due date must follow YYYY-MM-DD format.")
                return

            self.tasks.append({
                "title": title,
                "description": desc,
                "priority": priority,
                "due_date": due,
                "status": "Pending",
            })
            self.save_tasks()
            messagebox.showinfo("Success", "Task added successfully!")
            self.show_page("Tasks")

        def clear():
            e_title.delete(0, "end")
            e_desc.delete("1.0", "end")
            priority_var.set("")
            e_due.delete(0, "end")
            e_due.insert(0, datetime.now().strftime("%Y-%m-%d"))

        tk.Button(btn_row, text="Clear", command=clear,
                  bg="#e2e8f0", fg=COLOR_TEXT, relief="flat",
                  font=FONT_BODY_BOLD, padx=18, pady=8,
                  cursor="hand2").pack(side="right", padx=(8, 0))
        self._primary_button(btn_row, "💾  Save Task", save,
                             bg=COLOR_SUCCESS).pack(side="right")

    def _render_task_table(self, parent, tasks, with_actions=True):
        cols = ("#", "Title", "Priority", "Due Date", "Status")
        wrapper, tree = self._make_treeview(parent, cols,
                                            [50, 320, 100, 140, 120])
        wrapper.pack(fill="both", expand=True, padx=24, pady=(0, 12))

        for idx, t in enumerate(tasks, 1):
            real_idx = self.tasks.index(t)
            tree.insert("", "end", iid=str(real_idx),
                        values=(idx, t["title"], t["priority"],
                                t["due_date"], t["status"]))

        if not with_actions:
            return tree

        # Action bar
        bar = tk.Frame(parent, bg=COLOR_BG)
        bar.pack(fill="x", padx=24, pady=(0, 16))

        def get_sel():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Selection", "Please select a task.")
                return None
            return int(sel[0])

        def refresh():
            self.show_page(self.current_page)

        def delete():
            i = get_sel()
            if i is None:
                return
            if messagebox.askyesno("Delete", "Delete the selected task?"):
                del self.tasks[i]
                self.save_tasks()
                messagebox.showinfo("Deleted", "Task deleted.")
                refresh()

        def mark_complete():
            i = get_sel()
            if i is None:
                return
            self.tasks[i]["status"] = "Completed"
            self.save_tasks()
            messagebox.showinfo("Updated", "Task marked as completed!")
            refresh()

        def edit():
            i = get_sel()
            if i is None:
                return
            self._open_edit_dialog(i)

        self._primary_button(bar, "🔄  Refresh", refresh).pack(side="left",
                                                              padx=(0, 8))
        self._primary_button(bar, "✏️  Edit", edit,
                             bg="#8b5cf6").pack(side="left", padx=4)
        self._primary_button(bar, "✅  Mark Complete", mark_complete,
                             bg=COLOR_SUCCESS).pack(side="left", padx=4)
        self._primary_button(bar, "🗑  Delete", delete,
                             bg=COLOR_DANGER).pack(side="left", padx=4)
        return tree

    def _open_edit_dialog(self, idx):
        t = self.tasks[idx]
        win = tk.Toplevel(self.root)
        win.title("Edit Task")
        win.geometry("460x460")
        win.configure(bg=COLOR_CARD)
        win.transient(self.root)
        win.grab_set()

        def lbl(text, r):
            tk.Label(win, text=text, bg=COLOR_CARD, fg=COLOR_TEXT,
                     font=FONT_BODY_BOLD).grid(row=r, column=0, sticky="w",
                                               padx=20, pady=(12, 4))

        lbl("Task Title", 0)
        e_title = tk.Entry(win, font=FONT_BODY, relief="solid", bd=1)
        e_title.grid(row=1, column=0, sticky="ew", padx=20, ipady=5)
        e_title.insert(0, t["title"])

        lbl("Description", 2)
        e_desc = tk.Text(win, font=FONT_BODY, height=5, relief="solid", bd=1)
        e_desc.grid(row=3, column=0, sticky="ew", padx=20)
        e_desc.insert("1.0", t.get("description", ""))

        lbl("Priority", 4)
        p_var = tk.StringVar(value=t["priority"])
        ttk.Combobox(win, textvariable=p_var,
                     values=["High", "Medium", "Low"], state="readonly",
                     font=FONT_BODY).grid(row=5, column=0, sticky="ew",
                                          padx=20, ipady=3)

        lbl("Due Date (YYYY-MM-DD)", 6)
        e_due = tk.Entry(win, font=FONT_BODY, relief="solid", bd=1)
        e_due.grid(row=7, column=0, sticky="ew", padx=20, ipady=5)
        e_due.insert(0, t["due_date"])

        lbl("Status", 8)
        s_var = tk.StringVar(value=t["status"])
        ttk.Combobox(win, textvariable=s_var,
                     values=["Pending", "Completed"], state="readonly",
                     font=FONT_BODY).grid(row=9, column=0, sticky="ew",
                                          padx=20, ipady=3)

        win.grid_columnconfigure(0, weight=1)

        def save():
            title = e_title.get().strip()
            due = e_due.get().strip()
            if not title:
                messagebox.showerror("Validation", "Title cannot be empty.",
                                     parent=win)
                return
            try:
                datetime.strptime(due, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation", "Invalid date format.",
                                     parent=win)
                return
            self.tasks[idx] = {
                "title": title,
                "description": e_desc.get("1.0", "end").strip(),
                "priority": p_var.get(),
                "due_date": due,
                "status": s_var.get(),
            }
            self.save_tasks()
            messagebox.showinfo("Updated", "Task updated successfully!",
                                parent=win)
            win.destroy()
            self.show_page(self.current_page)

        bar = tk.Frame(win, bg=COLOR_CARD)
        bar.grid(row=10, column=0, sticky="e", padx=20, pady=20)
        tk.Button(bar, text="Cancel", command=win.destroy,
                  bg="#e2e8f0", fg=COLOR_TEXT, relief="flat",
                  font=FONT_BODY_BOLD, padx=14, pady=6,
                  cursor="hand2").pack(side="right", padx=(8, 0))
        self._primary_button(bar, "Save Changes", save,
                             bg=COLOR_SUCCESS).pack(side="right")

    def page_all_tasks(self):
        self._section_title(self.content, f"All Tasks ({len(self.tasks)})")
        self._render_task_table(self.content, list(self.tasks))

    def page_pending(self):
        pending = [t for t in self.tasks if t["status"] == "Pending"]
        self._section_title(self.content, f"Pending Tasks ({len(pending)})")
        self._render_task_table(self.content, pending)

    def page_completed(self):
        completed_tasks = [t for t in self.tasks if t["status"] == "Completed"]
        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True)

        tk.Label(wrap, text=f"Completed Tasks ({len(completed_tasks)})", bg=COLOR_BG,
                 fg=COLOR_TEXT, font=FONT_HEADER).pack(anchor="w", pady=(0, 20))
        if not completed_tasks:
            tk.Label(wrap, text="No completed tasks yet.", bg=COLOR_BG,
                     fg=COLOR_MUTED, font=FONT_BODY).pack(pady=40)
            return
        for task in completed_tasks:
            self._task_card(wrap, task)

    def page_search(self):
        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        card = tk.Frame(wrap, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER, highlightthickness=1)
        card.pack(fill="x", pady=(0, 16))

        tk.Label(card, text="Search Tasks", bg=COLOR_CARD, fg=COLOR_TEXT,
                 font=FONT_HEADER).grid(row=0, column=0, columnspan=3,
                                        sticky="w", padx=20, pady=(16, 8))

        tk.Label(card, text="Search by Title", bg=COLOR_CARD, fg=COLOR_TEXT,
                 font=FONT_BODY_BOLD).grid(row=1, column=0, sticky="w",
                                           padx=20)
        tk.Label(card, text="Filter by Priority", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_BODY_BOLD).grid(
            row=1, column=1, sticky="w", padx=10)

        e_title = tk.Entry(card, font=FONT_BODY, relief="solid", bd=1)
        e_title.grid(row=2, column=0, sticky="ew", padx=20, ipady=5)
        p_var = tk.StringVar(value="All")
        ttk.Combobox(card, textvariable=p_var,
                     values=["All", "High", "Medium", "Low"],
                     state="readonly", font=FONT_BODY).grid(
            row=2, column=1, sticky="ew", padx=10, ipady=3)

        results_frame = tk.Frame(wrap, bg=COLOR_BG)
        results_frame.pack(fill="both", expand=True)

        def do_search():
            q = e_title.get().strip().lower()
            p = p_var.get()
            results = []
            for t in self.tasks:
                if q and q not in t["title"].lower():
                    continue
                if p != "All" and t["priority"] != p:
                    continue
                results.append(t)
            for w in results_frame.winfo_children():
                w.destroy()
            tk.Label(results_frame, text=f"Results ({len(results)})",
                     bg=COLOR_BG, fg=COLOR_TEXT, font=FONT_HEADER).pack(
                anchor="w", pady=(8, 8))
            cols = ("Title", "Priority", "Due Date", "Status")
            wrapper, tree = self._make_treeview(results_frame, cols,
                                                [340, 120, 140, 120])
            wrapper.pack(fill="both", expand=True)
            for t in results:
                tree.insert("", "end", values=(t["title"], t["priority"],
                                               t["due_date"], t["status"]))

        self._primary_button(card, "🔍  Search", do_search).grid(
            row=2, column=2, padx=(10, 20))
        card.grid_columnconfigure(0, weight=2)
        card.grid_columnconfigure(1, weight=1)

        do_search()

    def page_statistics(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["status"] == "Completed")
        pending = total - completed
        pct = (completed / total * 100) if total else 0

        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        cards = tk.Frame(wrap, bg=COLOR_BG)
        cards.pack(fill="x")
        items = [
            ("Total Tasks", total, COLOR_PRIMARY),
            ("Completed", completed, COLOR_SUCCESS),
            ("Pending", pending, COLOR_WARNING),
            ("Completion %", f"{pct:.1f}%", "#8b5cf6"),
        ]
        for i, (l, v, c) in enumerate(items):
            self._make_card(cards, l, v, c).grid(
                row=0, column=i, padx=8, sticky="nsew")
            cards.grid_columnconfigure(i, weight=1)

        # Progress bar
        prog = tk.Frame(wrap, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER, highlightthickness=1)
        prog.pack(fill="x", pady=24)
        tk.Label(prog, text="Overall Completion", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_BODY_BOLD).pack(anchor="w",
                                                          padx=20, pady=(16, 6))
        bar_bg = tk.Frame(prog, bg="#e2e8f0", height=22)
        bar_bg.pack(fill="x", padx=20, pady=(0, 8))
        bar_bg.pack_propagate(False)
        fill = tk.Frame(bar_bg, bg=COLOR_SUCCESS)
        fill.place(relwidth=pct / 100, relheight=1)
        tk.Label(prog, text=f"{pct:.1f}% complete  ({completed}/{total})",
                 bg=COLOR_CARD, fg=COLOR_MUTED,
                 font=FONT_BODY).pack(anchor="w", padx=20, pady=(0, 16))

        # Priority breakdown
        high = sum(1 for t in self.tasks if t["priority"] == "High")
        med = sum(1 for t in self.tasks if t["priority"] == "Medium")
        low = sum(1 for t in self.tasks if t["priority"] == "Low")
        pr_card = tk.Frame(wrap, bg=COLOR_CARD,
                           highlightbackground=COLOR_BORDER,
                           highlightthickness=1)
        pr_card.pack(fill="x")
        tk.Label(pr_card, text="Tasks by Priority", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_BODY_BOLD).pack(
            anchor="w", padx=20, pady=(16, 8))
        row = tk.Frame(pr_card, bg=COLOR_CARD)
        row.pack(fill="x", padx=20, pady=(0, 16))
        for label, val, color in [("High", high, COLOR_DANGER),
                                  ("Medium", med, COLOR_WARNING),
                                  ("Low", low, COLOR_SUCCESS)]:
            chip = tk.Frame(row, bg=color)
            chip.pack(side="left", padx=(0, 12))
            tk.Label(chip, text=f"  {label}: {val}  ", bg=color, fg="#ffffff",
                     font=FONT_BODY_BOLD, padx=6, pady=6).pack()

    def page_export(self):
        wrap = tk.Frame(self.content, bg=COLOR_BG)
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        card = tk.Frame(wrap, bg=COLOR_CARD,
                        highlightbackground=COLOR_BORDER, highlightthickness=1)
        card.pack(fill="x")
        tk.Label(card, text="Export Tasks to CSV", bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_HEADER).pack(anchor="w",
                                                       padx=20, pady=(20, 8))
        tk.Label(card,
                 text=("Export all tasks to a CSV file for use in "
                       "Excel, Google Sheets, or other tools."),
                 bg=COLOR_CARD, fg=COLOR_MUTED, font=FONT_BODY,
                 wraplength=600, justify="left").pack(anchor="w",
                                                     padx=20, pady=(0, 16))

        def export():
            if not self.tasks:
                messagebox.showwarning("Empty", "No tasks to export.")
                return
            path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
                initialfile="tasks.csv",
                title="Export Tasks",
            )
            if not path:
                return
            try:
                with open(path, "w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    w.writerow(["Title", "Description", "Priority",
                                "Due Date", "Status"])
                    for t in self.tasks:
                        w.writerow([t["title"], t.get("description", ""),
                                    t["priority"], t["due_date"],
                                    t["status"]])
                messagebox.showinfo("Exported",
                                    f"Tasks exported successfully to:\n{path}")
            except OSError as e:
                messagebox.showerror("Export Error", str(e))

        self._primary_button(card, "💾  Export to CSV", export,
                             bg=COLOR_SUCCESS).pack(anchor="w",
                                                    padx=20, pady=(0, 20))


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
def main():
    root = tk.Tk()
    ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

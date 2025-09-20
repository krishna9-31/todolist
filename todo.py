import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BubbleTasksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BubbleTasks: Your Colorful To-Do App")
        self.root.geometry("800x600")
        self.root.configure(bg="#d0e0d8")

        self.username = "SparkleUser"
        self.tasks = []

        self.build_ui()

    def build_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#aed9a0")
        header_frame.pack(fill="x")

        tk.Label(
            header_frame,
            text=f"👤 Username: {self.username}",
            bg="#aed9a0",
            font=("Arial", 10, "bold")
        ).pack(side="left", padx=10, pady=5)

        self.total_label = tk.Label(
            header_frame,
            text="📋 Total Tasks: 0",
            bg="#aed9a0",
            font=("Arial", 10, "bold")
        )
        self.total_label.pack(side="right", padx=10)

        # Title
        tk.Label(
            self.root,
            text="✨ BubbleTasks ✨",
            font=("Arial", 20, "bold"),
            fg="blue",
            bg="#d0e0d8"
        ).pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#d0e0d8")
        input_frame.pack()

        self.task_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
        self.task_entry.pack(side="left", padx=10)

        add_btn = tk.Button(
            input_frame,
            text="➕ Add New Task",
            font=("Arial", 10),
            bg="#a3d2fc",
            command=self.add_task
        )
        add_btn.pack()

        # Task Display Frame
        self.task_frame = tk.Frame(self.root, bg="#d0e0d8")
        self.task_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Empty Task", "Please enter a task name.")
            return

        task_data = {
            "title": task_text,
            "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "progress": 0
        }

        self.tasks.append(task_data)
        self.task_entry.delete(0, tk.END)
        self.update_tasks()

    def update_tasks(self):
        # Clear previous
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        self.total_label.config(text=f"📋 Total Tasks: {len(self.tasks)}")

        for index, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame, bd=2, relief="solid", bg="white")
            frame.pack(fill="x", pady=5)

            # Task Title
            tk.Label(
                frame,
                text=task["title"],
                font=("Arial", 12, "bold"),
                anchor="w",
                bg="white"
            ).pack(anchor="w", padx=10, pady=2)

            # Date Added
            tk.Label(
                frame,
                text=f"🗓️ Added on: {task['date']}",
                font=("Arial", 9),
                fg="purple",
                bg="white"
            ).pack(anchor="w", padx=10)

            # Progress
            tk.Label(
                frame,
                text=f"🟠 Progress: {task['progress']}%",
                font=("Arial", 9, "bold"),
                fg="orange",
                bg="white"
            ).pack(anchor="w", padx=10, pady=2)

            # Buttons
            btn_frame = tk.Frame(frame, bg="white")
            btn_frame.pack(anchor="e", padx=10, pady=5)

            progress_btn = tk.Button(
                btn_frame,
                text="✔ Progress +",
                bg="lightgreen",
                command=lambda i=index: self.increase_progress(i)
            )
            progress_btn.pack(side="left", padx=5)

            delete_btn = tk.Button(
                btn_frame,
                text="❌ Delete",
                bg="tomato",
                command=lambda i=index: self.delete_task(i)
            )
            delete_btn.pack(side="left", padx=5)

    def increase_progress(self, index):
        if self.tasks[index]["progress"] < 100:
            self.tasks[index]["progress"] += 10
            if self.tasks[index]["progress"] > 100:
                self.tasks[index]["progress"] = 100
            self.update_tasks()
        else:
            messagebox.showinfo("Task Complete", f"'{self.tasks[index]['title']}' is already 100% complete!")

    def delete_task(self, index):
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
        if confirm:
            del self.tasks[index]
            self.update_tasks()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BubbleTasksApp(root)
    root.mainloop()

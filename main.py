import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QListWidgetItem


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.layout.addWidget(self.task_input)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.central_widget.setLayout(self.layout)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
            QPushButton {
                background-color: #3498db;
                color: #fff;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QListWidget {
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 5px;
            }
        """)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            item = QListWidgetItem(task_text)
            self.task_list.addItem(item)
            self.task_input.clear()

    def remove_task(self):
        selected_tasks = self.task_list.selectedItems()
        for task in selected_tasks:
            row = self.task_list.row(task)
            self.task_list.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())

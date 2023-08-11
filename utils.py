def add_task_to_list(task_list_widget, task_text):
    if task_text:
        task_list_widget.addItem(task_text)


def remove_task_from_list(task_list_widget):
    selected_tasks = task_list_widget.selectedItems()
    for task in selected_tasks:
        row = task_list_widget.row(task)
        task_list_widget.takeItem(row)

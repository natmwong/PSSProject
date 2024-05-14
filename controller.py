from task import Task
from recurringTask import RecurringTask
from transientTask import TransientTask
from antiTask import AntiTask

class Controller:
    def __init__(self, model):
        self.model = model

    # Add a task to the model
    def add_task(self, start_date, end_date, task_description, task_type, recurrence_pattern):
        if task_type == "Transient Task":
            task = TransientTask(start_date, end_date, task_description)
        elif task_type == "Recurring Task":
            task = RecurringTask(start_date, end_date, task_description, recurrence_pattern)
        else:
            task = AntiTask(start_date, end_date, task_description)
        self.model.add_task(task)

        
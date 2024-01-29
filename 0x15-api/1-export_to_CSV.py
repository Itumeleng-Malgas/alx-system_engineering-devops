#!/usr/bin/python3
"""Script that uses the requests module"""

import requests
import sys
import csv


def fetch_employee_data(employee_id):
    """
    Fetches employee data from the JSONPlaceholder API.

    Parameters:
        employee_id (int): The ID of the employee.

    Returns:
        dict: Employee data.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    return employee_data


def fetch_todo_list(employee_id):
    """
    Fetches the list of todos for a specific employee from the
    JSONPlaceholder API.

    Parameters:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of todos.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todo_list = response.json()
    return todo_list


def display_todo_progress(employee_id):
    """
    Displays the progress of todos for a specific employee.

    Parameters:
        employee_id (int): The ID of the employee.
    """
    employee_data = fetch_employee_data(employee_id)
    todo_list = fetch_todo_list(employee_id)

    employee_name = employee_data.get('name')
    completed_tasks = [task for task in todo_list if task['completed']]

    total_tasks = len(todo_list)
    completed_task_count = len(completed_tasks)

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_task_count, total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")

    export_to_csv(employee_id, employee_name, todo_list)


def export_to_csv(employee_id, employee_name, todo_list):
    """
    Exports the employee's todo list to a CSV file.
    """
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = (
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_list:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
            })


if __name__ == "__main__":
    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)

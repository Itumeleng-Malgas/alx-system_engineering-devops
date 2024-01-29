#!/usr/bin/python3
"""Script that uses the requests module"""
import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data from the JSONPlaceholder API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    return employee_data


def fetch_todo_list(employee_id):
    """
    Fetches the list of todos for a specific employee from the
    JSONPlaceholder API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todo_list = response.json()
    return todo_list


def display_todo_progress(employee_id):
    """
    Displays the progress of todos for a specific employee.
    """
    employee_data = fetch_employee_data(employee_id)
    todo_list = fetch_todo_list(employee_id)

    employee_username = employee_data.get('username')

    export_to_csv(employee_id, employee_username, todo_list)


def export_to_csv(employee_id, employee_username, todo_list):
    """
    Exports the employee's todo list to a CSV file.
    """
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
                csv_file, fieldnames=fields, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_username,
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

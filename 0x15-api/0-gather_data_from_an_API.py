#!/usr/bin/python3
""" Script that uses requests module """

import requests
import json
import sys

def fetch_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    return employee_data

def fetch_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todo_list = response.json()
    return todo_list

def display_todo_progress(employee_id):
    employee_data = fetch_employee_data(employee_id)
    todo_list = fetch_todo_list(employee_id)

    employee_name = employee_data.get('name')
    completed_tasks = [task for task in todo_list if task['completed']]
    
    total_tasks = len(todo_list)
    completed_task_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({completed_task_count}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)

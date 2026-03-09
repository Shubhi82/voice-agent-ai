import json
from datetime import datetime, timedelta

DATA_PATH = "../data/customers.json"

def load_customers():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def check_due_emis():
    customers = load_customers()
    today = datetime.today()

    due_list = []

    for c in customers:
        due_date = datetime.strptime(c["emi_due_date"], "%Y-%m-%d")

        if 0 <= (due_date - today).days <= 3:
            due_list.append(c)

    return due_list

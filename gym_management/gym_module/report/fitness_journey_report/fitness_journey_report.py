

import frappe

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Weight (kg)", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Calories Intake", "fieldname": "calories_intake", "fieldtype": "Float", "width": 120},
        {"label": "BMI", "fieldname": "bmi", "fieldtype": "Float", "width": 120}
    ]

    data = frappe.get_all("Gym Progress Tracker",
        filters={"member": filters.get("member")},
        fields=["date", "weight", "calories_intake", "bmi"],
        order_by="date asc"
    )

    chart = {
        "data": {
            "labels": [d["date"] for d in data],
            "datasets": [
                {"name": "Weight (kg)", "values": [d["weight"] for d in data]},
                {"name": "Calories", "values": [d["calories_intake"] for d in data]},
                {"name": "BMI", "values": [d["bmi"] for d in data]}
            ]
        },
        "type": "line",
        "height": 300
    }

    return columns, data, None, chart

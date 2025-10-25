import frappe
import math

def execute(filters=None):
    filters = filters or {}

    # building an  filters
    conditions = ""
    if filters.get("trainer"):
        conditions += f" AND trainer = '{filters.get('trainer')}'"
    if filters.get("from_date") and filters.get("to_date"):
        conditions += f" AND class_date BETWEEN '{filters.get('from_date')}' AND '{filters.get('to_date')}'"

    # use COALESCE for safe averages
    query = f"""
        SELECT
            class_type,
            COUNT(*) AS total_bookings,
            COALESCE(ROUND(AVG(rating), 2), 0) AS avg_rating,
            SUM(CASE WHEN attendance_status='Attended' THEN 1 ELSE 0 END) AS attended,
            SUM(CASE WHEN attendance_status='Missed' THEN 1 ELSE 0 END) AS missed
        FROM `tabGym Class Booking`
        WHERE class_type IS NOT NULL {conditions}
        GROUP BY class_type
        ORDER BY total_bookings DESC
    """

    data = frappe.db.sql(query, as_dict=True)

    # clean & normalize all numeric values
    cleaned_data = []
    for d in data:
        avg_rating = d.get("avg_rating")
        try:
            #  convert decimal / none / empty to clean float
            avg_rating = float(avg_rating or 0)
            if math.isnan(avg_rating):
                avg_rating = 0.0
        except Exception:
            avg_rating = 0.0

        total_bookings = int(d.get("total_bookings") or 0)
        attended = int(d.get("attended") or 0)
        missed = int(d.get("missed") or 0)
        attendance_percent = round((attended / total_bookings) * 100, 2) if total_bookings > 0 else 0.0

        cleaned_data.append({
            "class_type": d.get("class_type") or "Unknown",
            "total_bookings": total_bookings,
            "attended": attended,
            "missed": missed,
            "avg_rating": avg_rating,
            "attendance_percent": attendance_percent
        })

    # define columns
    columns = [
        {"label": "Class Type", "fieldname": "class_type", "fieldtype": "Data", "width": 180},
        {"label": "Total Bookings", "fieldname": "total_bookings", "fieldtype": "Int", "width": 120},
        {"label": "Attended", "fieldname": "attended", "fieldtype": "Int", "width": 100},
        {"label": "Missed", "fieldname": "missed", "fieldtype": "Int", "width": 100},
        #{"label": "Average Rating", "fieldname": "avg_rating", "fieldtype": "Float", "width": 120},
        {"label": "Attendance %", "fieldname": "attendance_percent", "fieldtype": "Float", "width": 120}
    ]

    # chart
    chart = {
        "data": {
            "labels": [d["class_type"] for d in cleaned_data],
            "datasets": [
                {"name": "Total Bookings", "values": [d["total_bookings"] for d in cleaned_data]},
                {"name": "Average Rating", "values": [d["avg_rating"] for d in cleaned_data]},
                {"name": "Attendance %", "values": [d["attendance_percent"] for d in cleaned_data]},
            ]
        },
        "type": "bar",
        "colors": ["#22c55e", "#3b82f6", "#f97316"],
        "height": 320
    }

    # summary
    if cleaned_data:
        total_bookings = sum(d["total_bookings"] for d in cleaned_data)
        total_attended = sum(d["attended"] for d in cleaned_data)
        total_missed = sum(d["missed"] for d in cleaned_data)
        avg_rating = round(sum(d["avg_rating"] for d in cleaned_data) / len(cleaned_data), 2)
    else:
        total_bookings = total_attended = total_missed = avg_rating = 0

    summary = [
        {"label": "Total Bookings", "value": total_bookings, "indicator": "green"},
        {"label": "Total Attended", "value": total_attended, "indicator": "blue"},
        {"label": "Total Missed", "value": total_missed, "indicator": "orange"},
        {"label": "Average Rating", "value": avg_rating, "indicator": "purple"}
    ]

    return columns, cleaned_data, None, chart, summary

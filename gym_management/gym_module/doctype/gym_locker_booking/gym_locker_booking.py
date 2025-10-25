import frappe
from frappe.model.document import Document


class GymLockerBooking(Document):
	def validate(self):
            # Checking  if locker already booked and still active
            is_exists = frappe.db.exists("Gym Locker Booking",
            {
                "locker_no": self.locker_no,
                "status": "Booked",
                "name": ["!=", self.name]
            }
            )

            if is_exists:
                  frappe.throw(f"Locker is already booked.")

            
            # check member has active membership
            status = frappe.db.get_value("Gym Member", self.member, "status")
            if status != "Active":
                  frappe.throw("this membership is not active please renew first")
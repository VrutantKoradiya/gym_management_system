# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate, add_days, getdate

class GymClassBooking(Document):
	def validate(self):
		# check member is active
		member_status = frappe.db.get_value("Gym Member", self.member, "status")
		if member_status != "Active":
			frappe.throw("Only members with an active membership can book a class.")
			
		# check weekly booking limit from Gym Settings
		limit = frappe.db.get_single_value("Gym Settings", "max_class_bookings") or 5
		
		week_start = add_days(nowdate(), -7)
		
		bookings = frappe.db.count("Gym Class Booking", {
		   "member": self.member,
               "class_date": [">=", week_start],
               
		})
		
		if bookings >= limit:
			frappe.throw(f"You have reached your weekly booking limit of {limit} classes.")
			
		# prevent double booking same time slot and date
		duplicate = frappe.db.exists("Gym Class Booking", {
            "member": self.member,
            "class_date": self.class_date,
            "time_slot": self.time_slot,
            "name": ["!=", self.name]
		})

		if duplicate:
			frappe.throw(f"You already booked a class for {self.class_date} ({self.time_slot}).")

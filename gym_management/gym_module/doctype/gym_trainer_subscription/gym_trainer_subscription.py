# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymTrainerSubscription(Document):

	def validate(self):
		# set trainer field of member doctype when subdcription is created.. (assign trainer to member)
		if self.member and self.trainer:
			frappe.db.set_value("Gym Member", self.member, "trainer", self.trainer)
			frappe.db.set_value("Gym Trainer Subscription", self.name, "status", "Active")
			frappe.msgprint(f"trainer  assigned to member {self.member}")

	def validate(self):
		# checking member has active membership 
		status = frappe.db.get_value("Gym Member", self.member, "status")
		if status != "Active":
			frappe.throw("This member's membership is not active. Please activate first.")
			
		# checking member has already trainer subscription
		is_exists = frappe.db.exists("Gym Trainer Subscription",
            {
                "member": self.member,
                "status": "Active",
                "name": ["!=", self.name]
            }
		)
		if is_exists:
			frappe.throw(f"Member {self.member} already has an active trainer subscription.")


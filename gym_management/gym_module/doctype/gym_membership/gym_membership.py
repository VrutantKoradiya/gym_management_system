# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

from ntpath import exists
import frappe
from frappe.model.document import Document


class GymMembership(Document):
	def on_submit(self):
		#setting memebrship , activeplan , status field in Mmber Doctype
		frappe.db.set_value("Gym Member", self.member, "gym_membership", self.name)
		frappe.db.set_value("Gym Member", self.member, "active_plan", self.name)
		frappe.db.set_value("Gym Member", self.member, "status", "Active")

	def validate(self):
		#check member ship is already exists -> if yes then throw error.
		is_exists = frappe.db.exists("Gym Membership",{
			"member": self.member,
			"status": "Active",
			"name": ["!=", self.name]
			}
			)

		if is_exists:
			frappe.throw(f"member have already has an active membership ...")



# get member details if memebership is already exists
@frappe.whitelist
def get_active_member_details(member):
	plan = frappe.db.get_value(
		"Gym Membership",
		{"member": member, "status": "Active"},
		["name", "end_date"],
		as_dict=True
		)
		
	if plan:
		return {
			"plan_name": plan.name,
			"end_date": plan.end_date
			}
	return None
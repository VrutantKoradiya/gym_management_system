# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMember(Document):
	def validate(self):
		#duplicate email ? 
		if self.email and frappe.db.exists("Gym Member",{"email": self.email, "name": ["!=", self.name]}):
			frappe.throw("Email is already exists")

		#duplicate mobile number ?
		if self.mobile_no and frappe.db.exists("Gym Member",{"mobile_no": self.mobile_no, "name": ["!=", self.name]}):
			frappe.throw("Mobile number is already exists")

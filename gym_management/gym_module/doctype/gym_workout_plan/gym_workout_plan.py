# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymWorkoutPlan(Document):
	def validate(self):
		# Ensure trainer + level combination is unique
		if frappe.db.exists("Gym Workout Plan",{ "trainer": self.trainer,"level": self.level,"name": ["!=", self.name] }): 
			# here name filter means - dont count the current record from the query.
			frappe.throw(f"You already have a workout plan for the '{self.level}' level.")
		    
		# if published but no exercises, throw error
		if self.published and not self.exercises:
			frappe.throw("Cannot publish a workout plan without exercises.")

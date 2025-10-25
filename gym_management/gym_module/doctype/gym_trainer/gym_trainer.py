# Copyright (c) 2025, Vrutant and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymTrainer(Document):
	pass
	# def validate(self):
	# 	# auto-update trainer's average rating from all subscriptions
	# 	avg_rating = frappe.db.sql(""" SELECT AVG(rating) as avg_rating FROM `tabGym Trainer Subscription`
      #       WHERE trainer = %s AND rating IS NOT NULL""", (self.name,), as_dict=True)
		
	# 	if avg_rating and avg_rating[0].avg_rating:
	# 		self.rating = round(avg_rating[0].avg_rating, 2)
	# 	else:
	# 		self.rating = 0


	


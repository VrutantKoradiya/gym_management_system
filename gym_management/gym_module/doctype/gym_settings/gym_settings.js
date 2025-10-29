// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Settings", {
      validate(frm) {
            // validate positive numbers
            if (frm.doc.max_lockers < 1) {
                frappe.throw("max Lockers must be atleast 1.");
            }
    
            if (frm.doc.max_class_bookings_per_week < 1) {
                frappe.throw("max Class Bookings must be at least 1.");
            }
           
        }
    });


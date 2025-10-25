// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer", {
      //rating should from 0 - 5
	rating: function(frm) {
            if (frm.doc.rating < 0 || frm.doc.rating > 5) {
                frappe.msgprint("Rating must be between 0 and 5.");
                frm.set_value('rating', '');
            }
        },

    refresh: function(frm){
        frappe.call({
            method: "gym_management.api.trainer_rating",
            args: { trainer: frm.doc.name },
            callback: function(r) {
                if (r.message) {
                   let rating = r.message
                   frm.set_value('rating',rating );
                   
                }
            }
        });
    } 
});

// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Progress Tracker", {

      //calculate BMI based on weight enterd or height which one is fetch from Gym Member Dcotype
	weight: function(frm) {
            if (frm.doc.weight && frm.doc.member) {
                // fetch height from Gym Member
                frappe.call({
                    method: "gym_management.api.get_member_height",
                    args: { member: frm.doc.member },
                    callback: function(r) {
                        if (r.message) {
                            let height_cm = r.message;
                            if (height_cm > 0) {
                                // Convert cm → m
                                let height_m = height_cm / 100;
                                let bmi = frm.doc.weight / (height_m * height_m);
                                frm.set_value('bmi', bmi.toFixed(2));
                            } else {
                                frappe.msgprint("⚠️ Height not found for this member.");
                            }
                        }
                    }
                });
            }
        },

        //add today date
        refresh(frm) {
            // Auto-fill today's date
            if (!frm.doc.date) {
                frm.set_value("date", frappe.datetime.nowdate());
            }
        },
});

// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer Subscription", {

      // set end date
      start_date: function(frm) {
            frm.trigger('calculate_enddate');
        },
      subscription_type: function(frm) {
            frm.trigger('calculate_enddate');
        },
      calculate_enddate: function(frm) {
            if (frm.doc.start_date && frm.doc.subscription_type) {
                let days = 0;
    
                if (frm.doc.subscription_type === "Weekly") days = 7;
                else if (frm.doc.subscription_type === "Monthly") days = 30;
                else if (frm.doc.subscription_type === "Quarterly") days = 90;
    
                let end_date = frappe.datetime.add_days(frm.doc.start_date, days);
                frm.set_value('end_date', end_date);
            }
        }
});

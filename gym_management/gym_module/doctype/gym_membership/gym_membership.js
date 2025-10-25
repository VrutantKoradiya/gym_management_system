// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
      plan_type: function(frm) {
            // auto set price based on plan type
            if (frm.doc.plan_type === "Monthly") {
                frm.set_value('price', 1000);
                frm.set_value('duration', 30);
            } 
            else if (frm.doc.plan_type === "Quarterly") {
                frm.set_value('price', 2700);
                frm.set_value('duration', 90);
            } 
            else if (frm.doc.plan_type === "Yearly") {
                frm.set_value('price', 10000);
                frm.set_value('duration', 365);
            }
        },


        //calculate end date
        start_date: function(frm) {
            frm.trigger('calculate_Enddate');
        },
        duration: function(frm) {
            frm.trigger('calculate_Enddate');
        },
        calculate_Enddate: function(frm) {
            if (frm.doc.start_date && frm.doc.duration) {
                let end = frappe.datetime.add_days(frm.doc.start_date, frm.doc.duration);
                frm.set_value('end_date', end);
            }
        },



        //get member details if memebership is already exists
        member: function(frm) {
            if (frm.doc.member) {
                frappe.call({
                    method: "gym_management.gym_module.doctype.gym_membership.gym_membership.get_active_member_details",
                    args: {
                        member: frm.doc.member
                    },
                    callback: function(r) {
                        if (r.message) {
                            let p = r.message;
                            frappe.msgprint(
                                `Member ${frm.doc.member} currently has an active plan:<br>
                                ${p.membership_name} (ends on ${frappe.format(p.end_date, {fieldtype: "Date"})})`
                            );
                        }
                    }
                });
            }
        }
});

// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Workout Plan", {
      before_save(frm) {
            // check at least one exercise is added
            if (!frm.doc.exercises || frm.doc.exercises.length === 0) {
                frappe.throw("please add atleast one exercise.");
            }
        }
});



//child table functionality
frappe.ui.form.on('Gym Workout Plan Exercise', {
    // cehck sets & reps has atleast 1 if not the set 1
    sets: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.sets < 1) {
            frappe.msgprint("Sets must be at least 1.");
            row.sets = 1;
            frm.refresh_field("exercises");
        }
    },

    reps: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.reps < 1) {
            frappe.msgprint("reps must be at least 1.");
            row.reps = 1;
            frm.refresh_field("exercises");
        }
    },

    // check duration should not negative
    duration: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.duration < 0) {
            frappe.msgprint("duration cannot be negative.");
            row.duration = 0;
            frm.refresh_field("exercises");
        }
    },

    // trigger message a new row is added
    exercises_add: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.msgprint("new exercise row added. please fill all details!");
    }
});


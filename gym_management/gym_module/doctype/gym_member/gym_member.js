// Copyright (c) 2025, Vrutant and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Member", {
	
      //calculate BMI
    weight(frm) {
            frm.trigger('calculateBMI');
        },
    height: function(frm) {
            frm.trigger('calculateBMI');
        },
    calculateBMI: function(frm) {
            if (frm.doc.weight && frm.doc.height) {
                let bmi = frm.doc.weight / ((frm.doc.height / 100) ** 2);
                frm.set_value('bmi', bmi.toFixed(2)); // toFixed is used to round the number to 2 decimal places.
            }
        }
});

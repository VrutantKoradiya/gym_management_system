


frappe.ui.form.on("Gym Locker Booking", {

      //calculate expiry date
      booking_date: function(frm) {
            frm.trigger('calculate_expiryDate');
        },
      duration: function(frm) {
            frm.trigger('calculate_expiryDate');
        },
      calculate_expiryDate: function(frm) {
            if (frm.doc.booking_date && frm.doc.duration) {
                let expiry_date = frappe.datetime.add_days(frm.doc.booking_date, frm.doc.duration);
                frm.set_value('expiry_date', expiry_date);
            }
        }
});
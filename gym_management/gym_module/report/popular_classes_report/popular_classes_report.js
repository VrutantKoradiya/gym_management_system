frappe.query_reports["Popular Classes Report"] = {
	"filters": [
	    {
		  fieldname: "trainer",
		  label: __("Trainer"),
		  fieldtype: "Link",
		  options: "Gym Trainer",
		  reqd: 0
	    },
	    {
		  fieldname: "from_date",
		  label: __("From Date"),
		  fieldtype: "Date",
		  reqd: 0,
		  default: frappe.datetime.month_start()
	    },
	    {
		  fieldname: "to_date",
		  label: __("To Date"),
		  fieldtype: "Date",
		  reqd: 0,
		  default: frappe.datetime.month_end()
	    }
	],
  
	onload: function(report) {
	    frappe.msgprint({
		  message: __("📊 Analyze which classes are most popular based on bookings and ratings."),
		  title: __("Popular Classes Report"),
		  indicator: "green"
	    });
	},
  
	formatter: function(value, row, column, data, default_formatter) {
	    value = default_formatter(value, row, column, data);
  
	    // color ratings visually
	    if (column.fieldname === "avg_rating" && value) {
		  const rating = parseFloat(value);
		  let color = "green";
		  if (rating < 3) color = "red";
		  else if (rating < 4) color = "orange";
		  value = `<b style='color:${color}'>${rating}</b>`;
	    }
  
	    // highlight missed classes in orange
	    if (column.fieldname === "missed" && data.missed > 0) {
		  value = `<span style='color:orange;'>${value}</span>`;
	    }
  
	    return value;
	}
  };
  
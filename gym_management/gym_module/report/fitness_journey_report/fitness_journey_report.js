frappe.query_reports["Fitness Journey Report"] = {
	"filters": [
	    {
		  fieldname: "member",
		  label: __("Member"),
		  fieldtype: "Link",
		  options: "Gym Member",
		  reqd: 1,
		  default: "",
		  get_query: function() {
			return {
			    filters: {
				  "status": "Active"
			    }
			};
		  }
	    }
	],
  
	// Optional: Customize chart colors and behavior after loading
	onload: function(report) {
	    frappe.msgprint({
		  message: __("📊 Select a Member to view their Fitness Journey."),
		  title: __("Welcome!"),
		  indicator: "blue"
	    });
	},
  
	formatter: function(value, row, column, data, default_formatter) {
	    // Highlight BMI values
	    if (column.fieldname === "bmi" && value) {
		  let bmi = parseFloat(value);
		  let color = "green";
		  if (bmi < 18.5) color = "orange"; // underweight
		  else if (bmi > 25) color = "red"; // overweight
		  value = `<span style="color:${color}; font-weight:bold;">${value}</span>`;
	    }
	    return default_formatter(value, row, column, data);
	}
  };
  
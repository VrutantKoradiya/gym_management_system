frappe.pages['gym-profile'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Member Profile',
		single_column: true
	});


	 // Load HTML into the page
	 $(frappe.render_template("gym_profile", {})).appendTo(page.body);

	 // Fetch current logged-in member info
	 frappe.call({
	     method: "gym_management.api.get_member_profile_data",
	     callback: function(r) {
		   if (r.message) {
			 let data = r.message;
			 $("#member-name").text(data.member_name || "N/A");
			 $("#member-email").text(data.email || "N/A");
			 $("#active-plan").text(data.active_plan || "No Active Plan");
			 $("#end-date").text(data.end_date || "—");
			 $("#remaining-days").text(data.remaining_days || "—");
			 $("#trainer-name").text(data.trainer_name || "—");
			 $("#trainer-contact").text(data.trainer_contact || "—");
   
			 // Past Plans
			 if (data.past_plans && data.past_plans.length > 0) {
			     let list = "";
			     data.past_plans.forEach(p => {
				   list += `<li>${p.name} (Ended on ${p.end_date})</li>`;
			     });
			     $("#past-plans").html(list);
			 } else {
			     $("#past-plans").html("<li>No past plans found.</li>");
			 }
		   }
	     }
	 });
};


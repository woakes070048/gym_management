// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Diet Plan', {
	refresh(frm) {
		frm.add_custom_button(__("Assign Diet Schedule"), function() {
				frappe.route_options = {
					"diet_plan": frm.doc.name,
					"total_days_of_diet": frm.doc.total_days_of_diet
				};
				frappe.set_route("assign-diet-schedule", "new-assign-diet-schedule");
			}, __("Create"));
	}
});
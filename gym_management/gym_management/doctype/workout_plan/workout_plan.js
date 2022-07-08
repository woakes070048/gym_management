// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Workout Plan', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Workout Plan', {
	refresh(frm) {
		frm.add_custom_button(__("Assign Workout Schedule"), function() {
				frappe.route_options = {
					"workout_plan": frm.doc.name,
					"no_of_days": frm.doc.no_of_days
				};
				frappe.set_route("assign-workout-schedule", "new-assign-workout-schedule");
			}, __("Create"));
	}
});
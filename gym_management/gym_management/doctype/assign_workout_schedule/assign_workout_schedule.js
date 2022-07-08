// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assign Workout Schedule', {
	before_save(frm) {
	    frm.set_value("end_date", frappe.datetime.add_days(frm.doc.start_date, frm.doc.no_of_days));
	    frm.set_value("title", frm.doc.customer+"'s Workout Plan For "+frm.doc.workout_plan);
	}
});
// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt


frappe.ui.form.on('Assign Diet Schedule', {
	before_save(frm) {
	    frm.set_value("end_date", frappe.datetime.add_days(frm.doc.start_date, frm.doc.total_days_of_diet));
	    frm.set_value("title", frm.doc.customer+"'s Diet Plan For "+frm.doc.diet_plan);
	}
});
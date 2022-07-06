// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee', {
	before_save(frm) {
		frm.set_value('age', moment().diff(frm.doc.date_of_birth, 'years'));
        frm.refresh_field('age');
	}
});
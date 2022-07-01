// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Measurement History', {
	before_save(frm) {
		frm.doc.bmi = frm.doc.weight / ( ((frm.doc.height * frm.doc.height) / 100) / 100)
		frm.doc.bmr = 66.5 + ( 13.75 * frm.doc.weight) + ( 5.003 * frm.doc.height )
	}
});
// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt


frappe.ui.form.on('Customer', {
	before_save(frm) {
		frm.set_value('age', moment().diff(frm.doc.date_of_birth, 'years'));
        frm.refresh_field('age');
	}
});

frappe.ui.form.on('Customer', {
	refresh(frm) {
		frm.add_custom_button(__("Measurement History"), function() {
				frappe.route_options = {
					"customer": frm.doc.name
				};
				frappe.set_route("measurement-history", "new-measurement-history");
			}, __("Create"));
	}
});

frappe.ui.form.on('Customer', {
	refresh(frm) {
		frm.add_custom_button(__("Member"), function() {
				frappe.route_options = {
					"customer": frm.doc.name
				};
				frappe.set_route("member", "new-member");
			}, __("Create"));
	}
});

frappe.ui.form.on('Customer', {
	refresh(frm) {
		frm.add_custom_button(__("Measurement Analysis"), function() {
				frappe.route_options = {
					"customer": frm.doc.name
				};
				frappe.set_route("query-report", "Measurement Analysis");
			}, __("View"));
	}

});
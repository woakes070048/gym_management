// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Measurement Analysis"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Measurement ID"),
			"fieldtype": "Link",
			"options": "Measurement History"
		},
		{
			"fieldname": "customer",
			"label": __("Registered Member"),
			"fieldtype": "MultiSelectList",
			"options": "Customer",
			get_data: function(txt) {
				return frappe.db.get_link_options('Customer', txt);
			}
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		}
	],
	onload: function(report) {
		const views_menu = report.page.add_custom_button_group(__('Analysis Report'));
		report.page.add_custom_menu_item(views_menu, __("Diet Schedule Analysis"), function() {
			frappe.set_route('query-report', 'Diet Schedule Analysis');
		});

		report.page.add_custom_menu_item(views_menu, __("Workout Schedule Analysis"), function() {
			frappe.set_route('query-report', 'Workout Schedule Analysis');
		});
	}
};
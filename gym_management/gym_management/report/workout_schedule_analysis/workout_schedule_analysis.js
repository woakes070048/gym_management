// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Workout Schedule Analysis"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Workout Schedule ID"),
			"fieldtype": "Link",
			"options": "Assign Workout Schedule"
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
			"fieldname": "workout_plan",
			"label": __("Workout Plan"),
			"fieldtype": "MultiSelectList",
			"options": "Workout Plan",
			get_data: function(txt) {
				return frappe.db.get_link_options('Workout Plan', txt);
			}
		},
		{
			"fieldname": "trainer",
			"label": __("Trainer"),
			"fieldtype": "MultiSelectList",
			"options": "Employee",
			get_data: function(txt) {
				return frappe.db.get_link_options('Employee', txt);
			}
		}
	],
	onload: function(report) {
		const views_menu = report.page.add_custom_button_group(__('Analysis Report'));
		report.page.add_custom_menu_item(views_menu, __("Diet Schedule Analysis"), function() {
			frappe.set_route('query-report', 'Diet Schedule Analysis');
		});

		report.page.add_custom_menu_item(views_menu, __("Measurement Analysis"), function() {
			frappe.set_route('query-report', 'Measurement Analysis');
		});
	}
};
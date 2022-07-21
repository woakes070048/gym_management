// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Gym Schedule"] = {
	"filters": [
		{
				"fieldname": "name",
				"label": __("Event ID"),
				"fieldtype": "Link",
				"options": "Event"
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Datetime",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Datetime",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "event_category",
			"label": __("Event Category"),
			"fieldtype": "Select",
			"options": ["", "Event", "Meeting", "Call", "Sent/Received Email", "Other"]
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ["", "Open", "Closed"],
			"default": "Open"
		},
		{
			"fieldname": "appointment_id",
			"label": __("Appointment ID"),
			"fieldtype": "Link",
			"options": "Appointment"
		}

	]
};

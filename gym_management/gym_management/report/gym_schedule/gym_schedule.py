# Copyright (c) 2022, Nihantra C. Patel and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_columns():
	columns = [
		{
			"label": _("Event ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Event",
			"width": 80
		},
		{
			"label": _("Subject"),
			"fieldname": "subject",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Event Category"),
			"fieldname": "event_category",
			"fieldtype": "Data",
			"width": 125
		},
		{
			"label": _("Starts On"),
			"fieldname": "starts_on",
			"fieldtype": "Datetime",
			"width": 155
		},
		{
			"label": _("Ends On"),
			"fieldname": "ends_on",
			"fieldtype": "Datetime",
			"width": 155
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 70
		},
		{
			"label": _("Event Participants"),
			"fieldname": "reference_docname",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Appointment ID"),
			"fieldname": "appointment_id",
			"fieldtype": "Data",
			"options": "Appointment",
			"width": 225
		},
		
	]
	return columns


def get_data(filters):
	return frappe.db.sql(
		"""
		SELECT
			`tabEvent`.name,
			`tabEvent`.subject,
			`tabEvent`.event_category,
			`tabEvent`.starts_on,
			`tabEvent`.ends_on,
			CASE WHEN `tabEvent`.status = "Open" THEN '<c style="color:red;">' "Open" '</c>'
				ELSE '<c style="color:green;">' "Closed" '</c>'
				END as status,
			GROUP_CONCAT(DISTINCT `tabEvent Participants`.reference_docname ORDER BY `tabEvent Participants`.reference_docname ASC SEPARATOR ', ') as reference_docname,
			GROUP_CONCAT(DISTINCT `tabAppointment`.name ORDER BY `tabAppointment`.name ASC SEPARATOR ', ') as appointment_id
			
		FROM
			`tabEvent`
			LEFT JOIN `tabAppointment`
			ON `tabEvent`.name = `tabAppointment`.calendar_event

			LEFT JOIN `tabEvent Participants`
			ON `tabEvent`.`name` = `tabEvent Participants`.`parent`

		WHERE
			`tabEvent`.starts_on BETWEEN %(from_date)s AND %(to_date)s
			{conditions}

		GROUP BY
			`tabEvent`.`name`

		ORDER BY
			`tabEvent`.starts_on desc """.format(
			conditions=get_conditions(filters)
		),
		filters,
		as_dict=1,
	)


def get_conditions(filters):
	conditions = []

	if filters.get("name"):
		conditions.append(" and `tabEvent`.name = %(name)s")

	if filters.get("event_category"):
		conditions.append(" and `tabEvent`.event_category = %(event_category)s")

	if filters.get("status"):
		conditions.append(" and `tabEvent`.status = %(status)s")

	if filters.get("appointment_id"):
		conditions.append(" and `tabAppointment`.name = %(appointment_id)s")

	return " ".join(conditions) if conditions else ""
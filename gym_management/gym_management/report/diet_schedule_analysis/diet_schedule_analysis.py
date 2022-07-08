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
			"label": _("ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Assign Diet Schedule",
			"width": 100
		},
		{
			"label": _("Title"),
			"fieldname": "title",
			"fieldtype": "Data",
			"width": 320
		},
		{
			"label": _("Registered Member"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 150
		},
		{
			"label": _("Diet Plan"),
			"fieldname": "diet_plan",
			"fieldtype": "Link",
			"options": "Diet Plan",
			"width": 220
		},
		{
			"label": _("No of Days"),
			"fieldname": "total_days_of_diet",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
			"width": 95
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
			"width": 95
		},
		{
			"label": _("Trainer"),
			"fieldname": "trainer",
			"fieldtype": "Link",
			"options": "Employee",
			"width": 130
		}
	]
	return columns


def get_data(filters):
	return frappe.db.sql(
		"""
		SELECT
			`tabAssign Diet Schedule`.name,
			`tabAssign Diet Schedule`.title,
			`tabAssign Diet Schedule`.customer,
			`tabAssign Diet Schedule`.diet_plan,
			`tabAssign Diet Schedule`.total_days_of_diet,
			`tabAssign Diet Schedule`.start_date,
			`tabAssign Diet Schedule`.end_date,
			`tabAssign Diet Schedule`.trainer
			
		FROM
			`tabAssign Diet Schedule`
		WHERE
			`tabAssign Diet Schedule`.start_date BETWEEN %(from_date)s AND %(to_date)s
			{conditions}
		ORDER BY
			`tabAssign Diet Schedule`.start_date desc """.format(
			conditions=get_conditions(filters)
		),
		filters,
		as_dict=1,
	)


def get_conditions(filters):
	conditions = []

	if filters.get("customer"):
		conditions.append(" and `tabAssign Diet Schedule`.customer in %(customer)s")

	if filters.get("Diet_plan"):
		conditions.append(" and `tabAssign Diet Schedule`.diet_plan in %(Diet_plan)s")

	if filters.get("trainer"):
		conditions.append(" and `tabAssign Diet Schedule`.trainer in %(trainer)s")

	if filters.get("name"):
		conditions.append(" and `tabAssign Diet Schedule`.name = %(name)s")


	return " ".join(conditions) if conditions else ""
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
			"options": "Measurement History",
			"width": 100,
		},
		{
			"label": _("Date"),
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 95,
		},
		{
			"label": _("Registered Member"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 150,
		},
		{
			"label": _("Weight"),
			"fieldname": "weight",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("Height"),
			"fieldname": "height",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("BMI"),
			"fieldname": "bmi",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("BMR"),
			"fieldname": "bmr",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("Neck"),
			"fieldname": "neck",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("Biceps"),
			"fieldname": "biceps",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("Hips"),
			"fieldname": "hips",
			"fieldtype": "Float",
			"width": 80,
		},
		{
			"label": _("Calf"),
			"fieldname": "calf",
			"fieldtype": "Float",
			"width": 75,
		},
		{
			"label": _("Chest"),
			"fieldname": "chest",
			"fieldtype": "Float",
			"width": 75,
		},
		{
			"label": _("Waist"),
			"fieldname": "waist",
			"fieldtype": "Float",
			"width": 75,
		},
		{
			"label": _("Thighs"),
			"fieldname": "thighs",
			"fieldtype": "Float",
			"width": 75,
		},
	]
	return columns


def get_data(filters):
	return frappe.db.sql(
		"""
		SELECT
			`tabMeasurement History`.name,
			`tabMeasurement History`.date,
			`tabMeasurement History`.customer,
			`tabMeasurement History`.weight,
			`tabMeasurement History`.height,
			`tabMeasurement History`.bmi,
			`tabMeasurement History`.bmr,
			`tabMeasurement History`.neck,
			`tabMeasurement History`.biceps,
			`tabMeasurement History`.hips,
			`tabMeasurement History`.calf,
			`tabMeasurement History`.chest,
			`tabMeasurement History`.waist,
			`tabMeasurement History`.thighs
		FROM
			`tabMeasurement History`
		WHERE
			`tabMeasurement History`.date BETWEEN %(from_date)s AND %(to_date)s
			{conditions}
		ORDER BY
			`tabMeasurement History`.date desc """.format(
			conditions=get_conditions(filters)
		),
		filters,
		as_dict=1,
	)


def get_conditions(filters):
	conditions = []

	if filters.get("customer"):
		conditions.append(" and `tabMeasurement History`.customer in %(customer)s")

	if filters.get("name"):
		conditions.append(" and `tabMeasurement History`.name = %(name)s")


	return " ".join(conditions) if conditions else ""
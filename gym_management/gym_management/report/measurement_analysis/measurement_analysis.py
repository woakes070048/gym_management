# Copyright (c) 2022, Nihantra C. Patel and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data


def get_columns(filters):
	if filters.get("group_by") != 1:
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
	elif filters.get("group_by") == 1:
		columns = [
			{
				"label": _("Registered Member"),
				"fieldname": "customer",
				"fieldtype": "Link",
				"options": "Customer",
				"width": 210,
			},
			{
				"label": _("Weight"),
				"fieldname": "weight",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Height"),
				"fieldname": "height",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("BMI"),
				"fieldname": "bmi",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("BMR"),
				"fieldname": "bmr",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Neck"),
				"fieldname": "neck",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Biceps"),
				"fieldname": "biceps",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Hips"),
				"fieldname": "hips",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Calf"),
				"fieldname": "calf",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Chest"),
				"fieldname": "chest",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Waist"),
				"fieldname": "waist",
				"fieldtype": "Float",
				"width": 90,
			},
			{
				"label": _("Thighs"),
				"fieldname": "thighs",
				"fieldtype": "Float",
				"width": 90,
			},
		]		

		return columns


def get_data(filters):

	if filters.get("group_by") == 1:
		return frappe.db.sql(
			"""
			SELECT
				customer as customer,
				AVG(weight) as weight,
				AVG(height) as height,
				AVG(bmi) as bmi,
				AVG(bmr) as bmr,
				AVG(neck) as neck,
				AVG(biceps) as biceps,
				AVG(hips) as hips,
				AVG(calf) as calf,
				AVG(chest) as chest,
				AVG(waist) as waist,
				AVG(thighs) as thighs
			FROM
				`tabMeasurement History`
			WHERE
				date BETWEEN %(from_date)s AND %(to_date)s
				{conditions}
			GROUP BY
				customer asc """.format(
				conditions=get_conditions(filters)
			),
			filters,
			as_dict=1,
		)

	else:
		return frappe.db.sql(
			"""
			SELECT
				name, date, customer, weight, height, bmi, bmr, neck, biceps, hips, calf, chest, waist, thighs
			FROM
				`tabMeasurement History`
			WHERE
				date BETWEEN %(from_date)s AND %(to_date)s
				{conditions}
			ORDER BY
				date desc """.format(
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
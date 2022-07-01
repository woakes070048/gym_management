# Copyright (c) 2022, Nihantra C. Patel and contributors
# For license information, please see license.txt

import frappe
import erpnext
import gym_management
from frappe.model.document import Document

class MeasurementHistory(Document):
	pass

def measurement_history(doc, event):
	
	member_name = frappe.db.get_value("Customer",{'name':doc.customer},'name')
	if member_name:
	    member_doc = frappe.get_doc("Customer",member_name)

	    # for remove duplicate row
	    [member_doc.measurement_history_table.remove(d) for d in member_doc.get('measurement_history_table') if d.measurement_history == doc.name]

	    row = member_doc.append('measurement_history_table', {})
	    row.measurement_history = doc.name
	    row.date = doc.date
	    row.customer = doc.customer
	    row.weight = doc.weight
	    row.height = doc.height
	    row.bmi = doc.bmi
	    row.bmr = doc.bmr
	    row.neck = doc.neck
	    row.biceps = doc.biceps
	    row.hips = doc.hips
	    row.calf = doc.calf
	    row.chest = doc.chest
	    row.waist = doc.waist
	    row.thighs = doc.thighs
	    member_doc.save()
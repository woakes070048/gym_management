# Copyright (c) 2022, Nihantra C. Patel and contributors
# For license information, please see license.txt


import frappe
import erpnext
import gym_management

def measurement_history(doc, event):
	
	test_d = frappe.db.get_value("Customer",{'name':doc.customer},'name')
	if test_d:
	    test_doc = frappe.get_doc("Customer",test_d)

	    # for remove duplicate row
	    [test_doc.measurement_history_table.remove(d) for d in test_doc.get('measurement_history_table') if d.measurement_history == doc.name]

	    row = test_doc.append('measurement_history_table', {})
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
	    test_doc.save()
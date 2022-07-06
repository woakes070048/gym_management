import frappe

def create_user_permission(doc, event):
	if doc.user:
		user_name = frappe.db.get_value("User Permission",{'user':doc.user, 'allow': "Customer",'for_value':doc.name},'name')
		if not user_name:
			user_per = frappe.get_doc(dict(
				doctype = 'User Permission',
				user = doc.user,
				allow = "Customer",
				for_value = doc.name
			))
			user_per.save()
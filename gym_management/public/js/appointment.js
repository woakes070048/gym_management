frappe.ui.form.on('Appointment', {
	onload: function(frm){
		frm.set_query("appointment_with", function(){
			return {
				filters : {
					"name": ["in", ["Customer", "Lead", "Employee", "Supplier"]]
				}
			};
		});
	}
});
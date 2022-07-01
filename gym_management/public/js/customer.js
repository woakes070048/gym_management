// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt


frappe.ui.form.on('Customer', {
	before_save(frm) {
		frm.set_value('age', moment().diff(frm.doc.date_of_birth, 'years'));
        frm.refresh_field('age');
	},
	refresh:function(frm, cdt, cdn){
	    frm.fields_dict['measurement_history_table'].grid.wrapper.find('.grid-remove-rows').hide();
	}
});

frappe.ui.form.on('Measurement History Table', {
    form_render(frm, cdt, cdn){
        frm.fields_dict.measurement_history_table.grid.wrapper.find('.grid-delete-row').hide();
    }
})
// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt


frappe.ui.form.on('Assign Diet Schedule', {
	before_save(frm) {
	    frm.set_value("end_date", frappe.datetime.add_days(frm.doc.start_date, frm.doc.total_days_of_diet));
	    frm.set_value("title", frm.doc.customer+"'s Diet Plan For "+frm.doc.diet_plan);
	}
});

frappe.ui.form.on('Assign Diet Schedule', {
    refresh(frm) {
        frm.add_custom_button(__("Get Diet Plan"), function() {
            new frappe.ui.form.MultiSelectDialog({
                doctype: "Diet Plan",
                target: cur_frm,
                setters: {
                    total_days_of_diet: null,
                },
                get_query() {
                    return {
                        filters: { docstatus: ['!=', 2] }
                    };
                },
                primary_action_label: 'Get Diet Plan',
                action(selections) {
                    let leng = selections.length;
                    for (let i = 0; i < leng; i++) {
                        let plan_name = selections[i];
                        frm.set_value('diet_plan',plan_name);
                    }
                    $(".modal").modal("hide");
                }
            });
        });
    }
});
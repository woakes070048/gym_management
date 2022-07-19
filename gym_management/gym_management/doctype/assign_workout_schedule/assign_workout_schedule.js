// Copyright (c) 2022, Nihantra C. Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assign Workout Schedule', {
	before_save(frm) {
	    frm.set_value("end_date", frappe.datetime.add_days(frm.doc.start_date, frm.doc.no_of_days));
	    frm.set_value("title", frm.doc.customer+"'s Workout Plan For "+frm.doc.workout_plan);
	}
});

frappe.ui.form.on('Assign Workout Schedule', {
    refresh(frm) {
        frm.add_custom_button(__("Get Workout Plan"), function() {
            new frappe.ui.form.MultiSelectDialog({
                doctype: "Workout Plan",
                target: cur_frm,
                setters: {
                    no_of_days: null,
                },
                get_query() {
                    return {
                        filters: { docstatus: ['!=', 2] }
                    };
                },
                primary_action_label: 'Get Workout Plan',
                action(selections) {
                    let leng = selections.length;
                    for (let i = 0; i < leng; i++) {
                        let plan_name = selections[i];
                        frm.set_value('workout_plan',plan_name);
                    }
                    $(".modal").modal("hide");
                }
            });
        });
    }
});
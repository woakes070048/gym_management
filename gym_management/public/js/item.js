frappe.ui.form.on("Item", "refresh", function(frm) {
    frm.add_custom_button(__("Active"), function() {
        frm.set_value('status',"Active");
        frm.set_value('disabled',0);
        frm.save();
        }, __("Status"));
    
    frm.add_custom_button(__("Maintenance"), function() {
        frm.set_value('status',"Maintenance");
        frm.set_value('disabled',0);
        frm.save();
        }, __("Status"));
    
    frm.add_custom_button(__("Repair"), function() {
        frm.set_value('status',"Repair");
        frm.set_value('disabled',0);
        frm.save();
        }, __("Status"));
    
    frm.add_custom_button(__("Out of Service"), function() {
        frm.set_value('status',"Out of Service");
        frm.set_value('disabled',1);
        frm.save();
        }, __("Status"));

    if(frm.doc.disabled == 1){
        frm.set_value('status',"Out of Service");
        frm.save();
    }
    else{
        frm.set_value('status',"Active");
        frm.save();
    }
});
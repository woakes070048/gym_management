frappe.listview_settings['Item'] = {
    add_fields: ["status"],
    get_indicator: function(doc) {
            var indicator = [__(doc.status), frappe.utils.guess_colour(doc.status), "status,=," + doc.status];
            if(doc.status=="Repair") {
                    indicator[1] = "orange";
            }
            else if(doc.status=="Maintenance") {
                    indicator[1] = "yellow";
            }
            else if(doc.status=="Out of Service") {
                    indicator[1] = "red";
            }
            else{
                indicator[1] = "green";
            }
            return indicator;
    },
};
// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Server Side Scripting", {
// 	enable: function(frm) {
//         frm.call({
//             doc: frm.doc,
//             method: 'frm_call',
//             // erpnext.programming.doctype.client_side_script.client_side_script.frappe_call
//             args: {
//                 msg: "Hello",
//             },
//             freeze: true,
//             freeze_message: __('Calling frm_call method'),
//             callback: function(r){
//                 frappe.msgprint(r.message)
//                 // frappe.msgprint("server side calling completed")
//                 // frm.refresh_field('medication_orders')
//             }
//         });
// 	},
// });


frappe.ui.form.on("Server Side Scripting", {
	enable: function(frm) {
        frappe.call({
            // doc: frm.doc,
            method: 'erpnext.programming.doctype.client_side_script.client_side_script.frappe_call',
            // erpnext.programming.doctype.client_side_script.client_side_script.frappe_call
            args: {
                msg: "Hello",
            },
            freeze: true,
            freeze_message: __('Calling frappe_call method'),
            callback: function(r){
                frappe.msgprint(r.message)
                // frappe.msgprint("server side calling completed")
                // frm.refresh_field('medication_orders')
            }
        });
	},
});
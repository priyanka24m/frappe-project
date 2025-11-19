// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Script", {
        // refresh(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello error PMC");
        // },
        // onload(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.msgprint("hello onload PMC");
        // },
        // before_save(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello before_save PMC");
        // },
        // after_save(frm) { 
        // // frappe.msgprint("hello PMC");
        // frappe.msgprint("hello after_save PMC");
        // },
        // enable(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello enable PMC");
        // },
        // age(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello age PMC");
        // },
        // family_member_on_form_rendered(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.msgprint("hello family_members_on_form_rendered PMC");
        // },
        // before_submit(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello before_submit PMC");
        // },
        // on_submit(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello on_submit PMC");
        // },
        // before_cancel(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello before_cancel PMC");
        // },
        // after_cancel(frm) {
        // // frappe.msgprint("hello PMC");
        // frappe.throw("hello after_cancel PMC");
        // },

        // after_save: function (frm) {
        //         frappe.msgprint(__("the full name is '{0}' ", [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]))

        //         for (let row of frm.doc.family_member){
        //                 frappe.msgprint(__("{0}. The family member name is {1} and relation is {2}", [row.idx, row.name1, row.relation]))
        //         }
        // }


//         refresh:function(frm){
//                 // frm.set_intro("test set intro");
//            if (frm.is_new()){
//                 frm.set_intro("test set intro");
//         }
// }

        
//         validate:function(frm){
//         frm.set_value("full_name",frm.doc.first_name+ " " + frm.doc.middle_name+ " " +frm.doc.last_name);

//         let row = frm.add_child("family_member",{
//                 name1: "test1",
//                 relation: "relation1",
//                 age:20,
//         })
          
// }

        // enable:function(frm){
        //         frm.set_df_property('first_name','reqd',1)
        //         // frm.refresh_field('first_name')
        //         // frm.set_df_property('middle_name','read_only',1)
        //         // frm.refresh_field('middle_name')
        //         frm.toggle_reqd('age',true)
        // }


refresh:function(frm){
        frm.add_custom_button('click me', () =>{
                frappe.msgprint(__("you clicked me"));
        })

          frm.add_custom_button('click me1', () =>{
                frappe.msgprint(__("you clicked 1"));
        },'click me again')

          frm.add_custom_button('click me2', () =>{
                frappe.msgprint(__("you clicked 2"));
        },'click me again')
}


});


// frappe.ui.form.on("Family members", {
//         // name1:function(frm) {
//         // frappe.msgprint("Child table msg");
//         // },

//         age(frm,cdt,cdn) {
//         frappe.msgprint("Child table age        msg");
//         }
// });
frappe.ui.form.on('Purchase Order Item', {
    rate(frm) {
        frappe.call({
            method: "validate_rate_with_range",
            doc: frm.doc,
            args:{
                'items':frm.doc.items
            },
            callback: (r) => {
                if (r._server_messages){
                    frm.fields_dict.items.grid.toggle_enable('rate', 1); 
                }
                else{
                    frm.fields_dict.items.grid.toggle_enable('rate', 0);
                }
            },
        });
    }
})
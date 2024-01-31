frappe.ui.form.on('Purchase Order Item', {
    rate(frm) {
        frappe.call({
            method: "validate_rate_with_range",
            doc: frm.doc,
            args:{
                'items':frm.doc.items
            },
            callback: (r) => {
                if (!r.exc) frm.refresh_fields();
            },
        });
    }
})
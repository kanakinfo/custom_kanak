frappe.ui.form.on('Purchase Order Item', {
    rate(frm) {
        $(frm.wrapper).on("grid-row-render", function(e, grid_row) {
            if(grid_row.grid.df.fieldname=="items"){
                frappe.call({
                    method: "validate_rate_with_range",
                    doc: frm.doc,
                    args:{
                        'line':grid_row.doc
                    },
                    callback: (r) => {
                        if (r._server_messages){
                            grid_row.toggle_editable("rate", true);
                            grid_row.toggle_enable("rate", true);
                        }
                        else{
                            grid_row.toggle_editable("rate", false);
                            grid_row.toggle_enable("rate", false);
                        }
                    },
                });
            }
        });
    }
})
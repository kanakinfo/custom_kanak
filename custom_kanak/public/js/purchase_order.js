var super_setup_queries = erpnext.buying.BuyingController.prototype.setup_queries;

// Override the setup_queries method
erpnext.buying.BuyingController.prototype.setup_queries = function() {
    // Call the original method with the same arguments as passed to this method
    super_setup_queries.apply(this, arguments);

    this.frm.set_query("item_code", "items", function() {
            if (me.frm.doc.is_subcontracted) {
                var filters = {'supplier': me.frm.doc.supplier};
                if (me.frm.doc.is_old_subcontracting_flow) {
                    filters["is_sub_contracted_item"] = 1;
                }
                else {
                    filters["is_stock_item"] = 0;
                }

                return{
                    query: "erpnext.controllers.queries.item_query",
                    filters: filters
                }
            }
            else {
                return{
                    query: "erpnext.controllers.queries.item_query",
                    filters: { 'supplier': me.frm.doc.supplier, 'is_purchase_item': 1, 'has_variants': 0, 'item_name': ['not like', '%-ROUT']}
                }
            }
    });
};
frappe.ui.form.on('Purchase Order Item', {
    rate(frm) {
        $(frm.wrapper).on("grid-row-render", function(e, grid_row) {
            if (grid_row.grid.df.fieldname == "items") {
                frappe.call({
                    method: "validate_rate_with_range",
                    doc: frm.doc,
                    args: {
                        'line': grid_row.doc
                    },
                    callback: (r) => {
                       
                        if(r._server_messages){
                            $(".rederrorcustomcl").remove();
                            $(".orangeerrorcustom_cl").remove();
                            
                            grid_row.toggle_editable("rate", true);
                            grid_row.toggle_enable("rate", true);
                        }else {
                             $(".rederrorcustomcl").remove();
                             $(".orangeerrorcustom_cl").remove();
                            grid_row.toggle_editable("rate", false);
                            grid_row.toggle_enable("rate", false);
                        }
                    },
                });
            }
        });
    }
});

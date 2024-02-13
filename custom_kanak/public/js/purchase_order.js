frappe.provide("frappe.messages");
frappe.provide("erpnext.buying");
frappe.show_alert = frappe.toast = function (message, seconds = 7, actions = {}) {
    let indicator_icon_map = {
        orange: "solid-warning",
        yellow: "solid-warning",
        blue: "solid-info",
        green: "solid-success",
        red: "solid-error",
        rederrorcustomcl: "solid-error",
        orangeerrorcustom_cl: "solid-warning",
    };

    if (typeof message === "string") {
        message = {
            message: message,
        };
    }

    if (!$("#dialog-container").length) {
        $('<div id="dialog-container"><div id="alert-container"></div></div>').appendTo("body");
    }

    let icon;
    if (message.indicator) {
        icon = indicator_icon_map[message.indicator.toLowerCase()] || "solid-" + message.indicator;
    } else {
        icon = "solid-info";
    }

    const indicator = message.indicator || "blue";

    const div = $(`
        <div class="alert desk-alert ${indicator}" role="alert">
            <div class="alert-message-container">
                <div class="alert-title-container">
                    <div>${frappe.utils.icon(icon, "lg")}</div>
                    <div class="alert-message">${message.message}</div>
                </div>
                <div class="alert-subtitle">${message.subtitle || ""}</div>
            </div>
            <div class="alert-body" style="display: none"></div>
            <a class="close">${frappe.utils.icon("close-alt")}</a>
        </div>
    `);

    div.hide().appendTo("#alert-container").show();

    if (message.body) {
        div.find(".alert-body").show().html(message.body);
    }

    div.find(".close, button").click(function () {
        div.addClass("out");
        setTimeout(() => div.remove(), 800);
        return false;
    });

    Object.keys(actions).map((key) => {
        div.find(`[data-action=${key}]`).on("click", actions[key]);
    });

    if (seconds > 2) {
        // Delay for animation
        seconds = seconds - 0.8;
    }

    setTimeout(() => {
        div.addClass("out");
        setTimeout(() => div.remove(), 800);
        return false;
    }, seconds * 1000);

    return div;
};
// var super_setup_queries = erpnext.buying.BuyingController.prototype.setup_queries;

// // Override the setup_queries method
// erpnext.buying.BuyingController.prototype.setup_queries = function() {
//     // Call the original method with the same arguments as passed to this method
//     super_setup_queries.apply(this, arguments);

//     this.frm.set_query("item_code", "items", function() {
//             if (me.frm.doc.is_subcontracted) {
//                 var filters = {'supplier': me.frm.doc.supplier};
//                 if (me.frm.doc.is_old_subcontracting_flow) {
//                     filters["is_sub_contracted_item"] = 1;
//                 }
//                 else {
//                     filters["is_stock_item"] = 0;
//                 }

//                 return{
//                     query: "erpnext.controllers.queries.item_query",
//                     filters: filters
//                 }
//             }
//             else {
//                 return{
//                     query: "erpnext.controllers.queries.item_query",
//                     filters: { 'supplier': me.frm.doc.supplier, 'is_purchase_item': 1, 'has_variants': 0, 'item_name': ['not like', '%-ROUT']}
//                 }
//             }
//     });
// };
// frappe.ui.form.on('Purchase Order Item', {
//     rate(frm) {
//         $(frm.wrapper).on("grid-row-render", function(e, grid_row) {
//             if (grid_row.grid.df.fieldname == "items") {
//                 frappe.call({
//                     method: "validate_rate_with_range",
//                     doc: frm.doc,
//                     args: {
//                         'line': grid_row.doc
//                     },
//                     callback: (r) => {
                       
//                         if(r._server_messages){
//                             $(".rederrorcustomcl").remove();
//                             $(".orangeerrorcustom_cl").remove();
                            
//                             grid_row.toggle_editable("rate", true);
//                             grid_row.toggle_enable("rate", true);
//                         }else {
//                              $(".rederrorcustomcl").remove();
//                              $(".orangeerrorcustom_cl").remove();
//                             grid_row.toggle_editable("rate", false);
//                             grid_row.toggle_enable("rate", false);
//                         }
//                     },
//                 });
//             }
//         });
//     }
// });

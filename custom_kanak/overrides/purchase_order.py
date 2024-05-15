import frappe
from frappe import _

from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder

class CustomPurchaseOrder(PurchaseOrder):

    @frappe.whitelist()
    def validate_rate_with_range(self, line):
        prices = frappe.get_all(
            "Item Price",
            filters={
                "price_list": self.buying_price_list,
                "item_code": line.get("item_code")
            }
        )
        if prices:
            item_price = frappe.get_doc("Item Price", prices[0].get("name"))
            if item_price.min_rate > 0 and item_price.max_rate > 0:
                if line.get("rate") < item_price.min_rate or line.get("rate") > item_price.max_rate:
                    msg = _("For {0} price range should be in between {1} To {2}").format(line.get("item_code"),item_price.min_rate,item_price.max_rate)
                    if "Purchase Manager" not in frappe.get_roles(frappe.session.user):
                        frappe.msgprint(msg, alert=True, indicator="rederrorcustomcl", title=_("Warning!"))
                    else:
                        frappe.msgprint(msg, alert=True, indicator="orangeerrorcustom_cl", title=_("Warning!"))

    def validate(self):
        super(CustomPurchaseOrder, self).on_submit()
        for line in self.items:
            prices = frappe.get_all(
                "Item Price",
                filters={
                    "price_list": self.buying_price_list,
                    "item_code": line.item_code
                }
            )
            if prices:
                item_price = frappe.get_doc("Item Price", prices[0].get("name"))
                if item_price.min_rate > 0 and item_price.max_rate > 0:
                    if line.rate < item_price.min_rate or line.rate > item_price.max_rate:
                        msg = _("For {0} price range should be in between {1} To {2}").format(line.get("item_code"),item_price.min_rate,item_price.max_rate)
                        if "Purchase Manager" not in frappe.get_roles(frappe.session.user):
                            frappe.throw(msg)
                        else:
                            frappe.msgprint(msg, alert=True, indicator="orangeerrorcustom_cl", title=_("Warning!"))


from . import __version__ as app_version

app_name = "custom_kanak"
app_title = "Custom Kanak"
app_publisher = "Kanak Infosystems LLP"
app_description = "Some Extar Customisation"
app_email = "sales@kanakinfosystems.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_kanak/css/custom_kanak.css"
# app_include_js = "/assets/custom_kanak/js/custom_kanak.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_kanak/css/custom_kanak.css"
# web_include_js = "/assets/custom_kanak/js/custom_kanak.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "custom_kanak/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Order" : "public/js/purchase_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "custom_kanak.utils.jinja_methods",
#	"filters": "custom_kanak.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "custom_kanak.install.before_install"
# after_install = "custom_kanak.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "custom_kanak.uninstall.before_uninstall"
# after_uninstall = "custom_kanak.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "custom_kanak.utils.before_app_install"
# after_app_install = "custom_kanak.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "custom_kanak.utils.before_app_uninstall"
# after_app_uninstall = "custom_kanak.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_kanak.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Purchase Order": "custom_kanak.overrides.purchase_order.CustomPurchaseOrder",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"custom_kanak.tasks.all"
#	],
#	"daily": [
#		"custom_kanak.tasks.daily"
#	],
#	"hourly": [
#		"custom_kanak.tasks.hourly"
#	],
#	"weekly": [
#		"custom_kanak.tasks.weekly"
#	],
#	"monthly": [
#		"custom_kanak.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "custom_kanak.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "custom_kanak.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "custom_kanak.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["custom_kanak.utils.before_request"]
# after_request = ["custom_kanak.utils.after_request"]

# Job Events
# ----------
# before_job = ["custom_kanak.utils.before_job"]
# after_job = ["custom_kanak.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"custom_kanak.auth.validate"
# ]

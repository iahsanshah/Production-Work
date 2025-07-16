app_name = "manufacturing_mas"
app_title = "update Job Cards"
app_publisher = "Ahsan Shah"
app_description = "Job card"
app_email = "iahsanshah11@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "manufacturing_mas",
# 		"logo": "/assets/manufacturing_mas/logo.png",
# 		"title": "update Job Cards",
# 		"route": "/manufacturing_mas",
# 		"has_permission": "manufacturing_mas.api.permission.has_app_permission"
# 	}
# ]
override_whitelisted_methods = {
    "erpnext.manufacturing.doctype.work_order.work_order.create_job_cards": "manufacturing_mas.override.work_order.create_job_cards"
}

doc_events = {
    "Job Card": {
        "before_submit": "manufacturing_mas.events.job_card.create_job_card_array_second_to_last"
    }
}


# manufacturing_mas/hooks.py
override_whitelisted_methods = {}

doc_events = {
    "Work Order": {
        "on_submit": "manufacturing_mas.overrides.work_order_override.create_job_card_only_first"
    }
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manufacturing_mas/css/manufacturing_mas.css"
# app_include_js = "/assets/manufacturing_mas/js/manufacturing_mas.js"

# include js, css files in header of web template
# web_include_css = "/assets/manufacturing_mas/css/manufacturing_mas.css"
# web_include_js = "/assets/manufacturing_mas/js/manufacturing_mas.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "manufacturing_mas/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "manufacturing_mas/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "manufacturing_mas.utils.jinja_methods",
# 	"filters": "manufacturing_mas.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "manufacturing_mas.install.before_install"
# after_install = "manufacturing_mas.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "manufacturing_mas.uninstall.before_uninstall"
# after_uninstall = "manufacturing_mas.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "manufacturing_mas.utils.before_app_install"
# after_app_install = "manufacturing_mas.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "manufacturing_mas.utils.before_app_uninstall"
# after_app_uninstall = "manufacturing_mas.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manufacturing_mas.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"manufacturing_mas.tasks.all"
# 	],
# 	"daily": [
# 		"manufacturing_mas.tasks.daily"
# 	],
# 	"hourly": [
# 		"manufacturing_mas.tasks.hourly"
# 	],
# 	"weekly": [
# 		"manufacturing_mas.tasks.weekly"
# 	],
# 	"monthly": [
# 		"manufacturing_mas.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "manufacturing_mas.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "manufacturing_mas.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "manufacturing_mas.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["manufacturing_mas.utils.before_request"]
# after_request = ["manufacturing_mas.utils.after_request"]

# Job Events
# ----------
# before_job = ["manufacturing_mas.utils.before_job"]
# after_job = ["manufacturing_mas.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"manufacturing_mas.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


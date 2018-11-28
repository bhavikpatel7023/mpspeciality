# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mpspeciality"
app_title = "MP Specility"
app_publisher = "Bhavik Patel"
app_description = "MP Speciality"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bhavikpatel7023@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mpspeciality/css/mpspeciality.css"
# app_include_js = "/assets/mpspeciality/js/mpspeciality.js"

# include js, css files in header of web template
# web_include_css = "/assets/mpspeciality/css/mpspeciality.css"
# web_include_js = "/assets/mpspeciality/js/mpspeciality.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "mpspeciality.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mpspeciality.install.before_install"
# after_install = "mpspeciality.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mpspeciality.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Roll Builder": {
		"on_submit": "mpspeciality.api.stock_entry"
	},
	"Roll Number": {
		"on_trash": "mpspeciality.api.delete_batch"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mpspeciality.tasks.all"
# 	],
# 	"daily": [
# 		"mpspeciality.tasks.daily"
# 	],
# 	"hourly": [
# 		"mpspeciality.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mpspeciality.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mpspeciality.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mpspeciality.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mpspeciality.event.get_events"
# }


# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bhavik Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json

class RollBuilder(Document):
	pass
	'''
	def before_save(self):
		if len(self.items):
			self.old_items = self.items
			for item in self.get("items"):
				for i in range(item.qty):
					demo_item = {}
					demo_item["qty"] = 1
					demo_item["item_code"] = self.item_code
					#demo_item["s_warehouse"] = self.source_warehouse
					demo_item["t_warehouse"] = self.target_warehouse
					demo_item["weight"] = item.weight
					demo_item["roll_no"] = item.roll_no
					self.old_items.append(demo_item)
	
@frappe.whitelist()
def stock_save(data):
	doc=frappe.get_doc({
			"naming_series":"STE-",
			"doctype":"Stock Entry",
			"purpose":"Repack"
			"items":[
			{
			"t_warehouse":"",
			"qty":300,
			"item_code":"Roll",
			"s_warehouse":"Stores - EB",
			"batch_no":""
			}
			],
			"posting_date":frappe.utils.nowdate()
		})
	doc.insert()
	'''
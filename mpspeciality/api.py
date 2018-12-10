from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import requests
import json
import logging

def stock_entry(doc,method):
	try:
		#frappe.msgprint(doc.name)
		new_items = []
		parent_item = {}
		parent_item["s_warehouse"] = doc.source_warehouse
		parent_item["item_code"] = doc.item_code
		parent_item["qty"] = doc.total_qty
		parent_item["batch_no"] = doc.input_roll_number
		new_items.append(parent_item)
		for item in doc.items:
			if int(item.is_scrap)==1 and not doc.scrap_warehouse:
				frappe.throw("please select Scrap warehouse")
				
		i = 0
		for item in doc.items:
			#frappe.msgprint(str(item.idx)+" "+str(item.weight))
			for j in range(item.qty):
				demo_item = {}
				demo_item["item_code"] = doc.item_code
				demo_item["qty"] = item.weight
				demo_item["gross_weight_"] = item.gross_weight
				demo_item["tare_weight"] = item.tare_weight
				batches = frappe.db.sql("""select name from `tabBatch`""")
				#frappe.msgprint(json.dumps(batches))
				#batch1 = str(str(item.roll_no)+str('-')+str(i))
				#frappe.msgprint(batch1)
				check_batch = str(str(doc.input_roll_number)+str('-')+str(i+1))
				
				#batch generation based on scrap or not
				
				if int(item.is_scrap)==0:
					
					if not check_batch in batches:
						#frappe.msgprint("batch not found")
						batch = frappe.get_doc({
							"docstatus":0,
							"doctype":"Batch",
							"batch_id":check_batch,
							"item": doc.item_code
							})
						batch.insert()
						#frappe.msgprint("Batch created")
						#frappe.msgprint(str(item.weight)+" "+str(batch.name))
				#roll number set based on Scrap or not
				if int(item.is_scrap)==1:
					demo_item["batch_no"] = doc.input_roll_number
				else:
					demo_item["batch_no"] = check_batch
					
				#warehouse set based on scrap
				if int(item.is_scrap)==1 and doc.scrap_warehouse:
					demo_item["t_warehouse"] = doc.scrap_warehouse

				elif doc.target_warehouse:
					demo_item["t_warehouse"] = doc.target_warehouse
				else:
					demo_item["t_warehouse"] = doc.source_warehouse
				#frappe.msgprint(json.dumps(demo_item))
				i = i + 1
				new_items.append(demo_item)
		#frappe.msgprint(json.dumps(new_items))
		doc=frappe.get_doc({
			"naming_series":"STE-",
			"doctype":"Stock Entry",
			"purpose":"Repack",
			"items": new_items ,
			"posting_date":frappe.utils.nowdate()
		})
		doc.insert()
		doc.submit()
		frappe.msgprint("Roll has been Generated")
	except Exception as e:
		frappe.throw("Something went wrong {0}".format(e))
		return e

@frappe.whitelist()
def roll_number_generator(item_code,route=None,is_mother_roll=None, parent_roll_no=None):
	#frappe.msgprint(item_code)
	batch_no = None
	roll = ''
	if int(is_mother_roll)==1:
		batch_no = str('0000000')
		names = frappe.db.sql("""select name from `tabRoll Number` ORDER BY creation DESC """,as_dict=1)
		if len(names) > 0:
			#frappe.msgprint(str(names[0].name))
			batch_no = int(names[0].name)+1
			roll = str(batch_no)
		else:
		#	frappe.msgprint(str(batch_no))
			batch_no  = int(batch_no) +  1
			roll =str(batch_no)
		roll = frappe.get_doc({
			"docstatus":0,
			"doctype":"Roll Number",
			"roll_no":str(roll)
		})
		roll.insert()
	else:
		batch_no = str(parent_roll_no)
		if not route==None:
			batch_no = str(batch_no) + "/" + route
		else:
			frappe.throw("Please select route")
			
	batch = frappe.get_doc({
			"docstatus":0,
			"doctype":"Batch",
			"name": "New Batch 1",
			"batch_id":str(batch_no),
			"item": item_code
	})
	
	batch.insert()
	return batch_no
	
def delete_batch(doc,method):
	pass
	#document = frappe.get_doc("Batch",doc.name)
	#document.delete()
	
'''
def stock_entry_manufacture(doc,method):
	try:
		if doc.purpose=="Manufacture":
			
			names = frappe.db.sql_list("""select name from `tabRoll Number` where ORDER BY roll_number desc """)
			
				
	except Exception as e:
		logging.exception("message")
		return e
'''
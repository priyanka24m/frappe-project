# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class ServerSideScripting(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Int
		amended_from: DF.Link | None
		client_side_doc: DF.Link | None
		dob: DF.Date | None
		email: DF.Data | None
		enable: DF.Check
		family_member: DF.Link | None
		first_name: DF.Data | None
		full_name: DF.ReadOnly | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		mob_no: DF.Data | None
	# end: auto-generated types

	# def validate(self):
	# 	frappe.msgprint("hello from validate server side")

	# def validate(self):
	# 	frappe.msgprint(_("hello full name is {0}").format(self.first_name+ " " + self.middle_name + " "+ self.last_name))

	# def validate(self):
	# 	for row in self.get("family_member"):
	# 		frappe.msgprint(_(
	# 			'{0}. the family member is {1} and relation is {2}'
	# 		).format(row.idx, row.name1, row.relation) )

	# def before_save(self):
	# 	frappe.msgprint("hello from before_save server side")

	# def after_save(self):
	# 	frappe.msgprint("hello from after_save server side")

	# def before_insert(self):
	# 	frappe.msgprint("hello from before_insert server side")

	# def after_insert(self):
	# 	frappe.msgprint("hello from after_insert server side")

	# def on_update(self):
	# 	frappe.msgprint("hello from on_update server side")


	# def before_submit(self):
	# 	frappe.msgprint("hello from before_submit server side")

	# def after_submit(self):
	# 	frappe.msgprint("hello from after_submit server side")

	# def on_cancel(self):
	# 	frappe.msgprint("hello from on_cancel server side")

	# def on_trash(self):
	# 	frappe.msgprint("hello from on_trash server side")

	# def after_delete(self):
	# 	frappe.msgprint("hello from after_delete server side")



	def get_document(self):
		doc = frappe.get_doc('Client Side Script',self.client_side_doc)
		frappe.msgprint(_('the first name is {0} and age is {1}').format(self.first_name, self.age))

		for row in doc.get('family_member'):
			frappe.msgprint(_('{0}. the family member is {1} and relation is {2}').format(row.idx, row.name1, row.relation))

	def new_document(self):
		doc = frappe.new_doc('Client Side Script')
		doc.first_name = 'duffer'
		doc.last_name = 'stupid'
		doc.age = 100
		doc.append('family_member',{
			"name1":"biggest duffer",
			"relation":"stranger",
			"age":500
		})

		doc.insert()


	def delete_document(self):
		# frappe.delete_doc('Client Side Script','PR-0005')
		doc = frappe.get_doc('Client Side Script', 'PR-0004')
		doc.delete()


	def save_document(self):
		doc = frappe.new_doc('Client Side Script')
		doc.first_name = 'great'
		doc.last_name = 'stupid'
		doc.age = 100
		doc.append('family_member',{
			"name1":"biggest duffer",
			"relation":"stranger",
			"age":500
		})

		doc.save()


	def db_set_document(self):
		doc = frappe.get_doc('Client Side Script', 'PR-0005')
		doc.db_set('age', 200)


	def get_list_doc(self):
		doc = frappe.db.get_list('Client Side Script',
					filters={'enable':1},
					fields=['first_name','age'])
		for d in doc:
			frappe.msgprint(_('the first name is {0} and age is {1}').format(d.first_name,d.age))	


	# def get_value_doc(self):
	# 	doc = frappe.db.get_value('Client Side Script', 'PR-0003', ['first_name','age'])
	# 	frappe.msgprint(_('the first name is {0} and age is {1}').format(doc[0],doc[1]))


	def set_value_doc(self):
		frappe.db.set_value('Client Side Script', 'PR-0003', 'first_name','tytyyt')
		doc = frappe.db.get_value('Client Side Script', 'PR-0003', ['first_name','age'])

		frappe.msgprint(_('the first name is {0} and age is {1}').format(doc[0],doc[1]))


	def check_exists(self):
		if frappe.db.exists('Client Side Script', 'PR-0004'):
			frappe.msgprint(_('document exists'))
		else:
			frappe.msgprint(_('document does not exist'))

	def doc_count(self):
		doc = frappe.db.count('Client Side Script', {'enable':1})
		frappe.msgprint(_('count {0}').format(doc))

	def sql_query(self):
		data = frappe.db.sql(""" 
			select first_name,age from `tabClient Side Script` where enable =1 
		""",as_dict=1)

		for d in data:
			frappe.msgprint(_('the first name is {0} and age is {1}').format(d.first_name,d.age))



	def validate(self):
		pass
		# self.get_document()
		# self.new_document()
		# self.delete_document()
		# self.save_document()
		# self.db_set_document()
		# self.get_list_doc()
		# self.get_value_doc()
		# self.set_value_doc()
		# self.check_exists()
		# self.doc_count()
		# self.sql_query()

	@frappe.whitelist()
	def frm_call(self,msg):
		import time
		time.sleep(3)
		frappe.msgprint(_(msg))
		self.mob_no = 22222
		return 'hi msg from frm call'
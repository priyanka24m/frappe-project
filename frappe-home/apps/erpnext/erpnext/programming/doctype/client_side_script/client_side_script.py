# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientSideScript(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.programming.doctype.family_members.family_members import Familymembers
		from frappe.types import DF

		age: DF.Int
		amended_from: DF.Link | None
		dob: DF.Date | None
		email: DF.Data | None
		enable: DF.Check
		family_member: DF.Table[Familymembers]
		first_name: DF.Data | None
		full_name: DF.ReadOnly | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		mob_no: DF.Data | None
	# end: auto-generated types

	pass



@frappe.whitelist()
def frappe_call(msg):
	# import time
	# time.sleep(3)
	# frappe.msgprint(_(msg))
	# self.mob_no = 22222
	return 'hi msg from frappe call'
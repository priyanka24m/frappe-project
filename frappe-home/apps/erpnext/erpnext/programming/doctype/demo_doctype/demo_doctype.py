# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DemoDoctype(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attach: DF.Attach | None
		attach_image: DF.AttachImage | None
		barcode: DF.Barcode | None
		check_box: DF.Check
		color: DF.Color | None
		currency: DF.Currency
		date: DF.Date | None
		datetime: DF.Datetime | None
		first_name: DF.Data | None
		float: DF.Float
		link: DF.Link | None
		select: DF.Literal["A", "B", "C"]
		text: DF.Text | None
	# end: auto-generated types

	pass

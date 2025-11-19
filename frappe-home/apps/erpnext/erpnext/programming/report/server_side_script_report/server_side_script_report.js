// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Script Report"] = {
	filters: [
		{
			"fieldname": "name",
			"label": __("server side scripting"),
			"fieldtype": "Link",
			"options": "Server Side Scripting",
			// "reqd": 1,
		},
		{
			"fieldname": "dob",
			"label": __("DOB"),
			"fieldtype": "Date",
			// "reqd": 1,
		},
		{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Data",
			// "reqd": 1,
		},
	],
};

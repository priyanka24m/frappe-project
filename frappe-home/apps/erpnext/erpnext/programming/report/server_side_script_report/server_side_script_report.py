# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	if not filters: filters = {}

	data, columns = [],[]

	columns = get_columns()
	cs_data = get_data(filters)

	if not cs_data:
		msgprint(_('No records'))
		return columns, cs_data

	for d in cs_data:
		row = frappe._dict({
			'first_name':d.first_name,
			'age':d.age,
			'dob':d.dob
		})
		data.append(row)


	chart = get_chart_data(data)
	report_summary = get_report_summary(data)
	return columns, data, None,chart, report_summary

	# return columns, data, None, chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("First Name"),
			"fieldname": "first_name",
			"fieldtype": "Data",
			"width": '120'
		},
		{
			"label": _("DOB"),
			"fieldname": "dob",
			"fieldtype": "Date",
			"width": '120'
		},
		{
			"label": _("Age"),
			"fieldname": "age",
			"fieldtype": "Data",
			"width": '120'
		},
	]

def get_data(filters):
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'Server Side Scripting',
		fields = ['first_name','dob','age'],
		filters = conditions,
		order_by = 'first_name desc'
	)

	return data


def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions


def get_chart_data(data):
	if not data:
		return None
	
	labels = ['Age <= 45', 'Age > 45' ]
	age_data = {
		'Age <= 45':0,
		'Age > 45':0	
	}

	datasets= []

	for entry in data:
		if entry.age <= 45:
			age_data['Age <= 45'] += 1
		else:
			age_data['Age > 45'] += 1


	datasets.append({
		'name':'Age Status',
		'values': [age_data.get('Age <= 45'), age_data.get('Age > 45')]
	})

	chart = {
		'data':{
			'labels':labels,
			'datasets':datasets
		},
		# 'type':'pie',
		# 'type':'line',
		'type':'bar',
		'height': 300
	}

	return chart


def get_report_summary(data):
	if not data:
		return None
	age_below_45, age_above_45 = 0,0

	for entry in data:
		if entry.age <= 45:
			age_below_45 +=1

		else:
			age_above_45 += 1

	return [
		{
			'value': age_below_45,
			'indicator': 'Green',
			'label': 'Age Below 45',
			'datatype': 'Int'
		},
		{
			'value': age_above_45,
			'indicator': 'red',
			'label': 'Age Above 45',
			'datatype': 'Int'
		}
	]

	# pass
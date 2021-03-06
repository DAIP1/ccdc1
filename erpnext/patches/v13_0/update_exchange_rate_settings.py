import frappe

from erpnext.setup.install import setup_currency_exchange


def execute():
	frappe.reload_doc("accounts", "doctype", "currency_exchange_settings")
	frappe.reload_doc("accounts", "doctype", "currency_exchange_settings_result")
	frappe.reload_doc("accounts", "doctype", "currency_exchange_settings_details")
	setup_currency_exchange()
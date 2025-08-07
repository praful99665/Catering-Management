import frappe
from frappe.utils import add_days, getdate

def create_event_todo(doc, method): 
    
    
    if doc.custom_event_date:
        reminder_date = add_days(getdate(doc.custom_event_date), -1)
    if doc.custom_lead:
        employee = frappe.get_doc("Employee", doc.custom_lead)
        if employee.user_id:

            todo = frappe.get_doc({
                'doctype': 'ToDo',
                'description': doc.custom_notes,
                'allocated_to': employee.user_id,
                'custom_event_date': doc.custom_event_date,
                'custom_reminder_date': reminder_date,
                'custom_customer': doc.customer,
                'reference_type': "Sales Invoice",
                'reference_name': doc.name,
            })

        todo.insert(ignore_permissions=True)

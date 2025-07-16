# manufacturing_mas/events/job_card.py

import frappe
from erpnext.manufacturing.doctype.job_card.job_card import get_job_card_data

def create_job_card_array_second_to_last(doc, method):
    frappe.msgprint(f"Checking next operation after: {doc.operation}")

    if doc.completed_qty < doc.for_quantity:
        frappe.msgprint("Current Job Card not fully completed.")
        return

    # Get linked Work Order and its operations
    work_order = frappe.get_doc("Work Order", doc.work_order)
    operations = work_order.operations

    # Find current operation index
    current_index = None
    for idx, op in enumerate(operations):
        if op.operation == doc.operation:
            current_index = idx
            break

    if current_index is None:
        frappe.msgprint("Current operation not found in Work Order.")
        return

    # Stop if last operation
    if current_index + 1 >= len(operations):
        frappe.msgprint("Last operation completed. No further Job Cards needed.")
        return

    # Get next operation
    next_op = operations[current_index + 1]

    # Check if next Job Card already exists
    existing = frappe.db.exists("Job Card", {
        "work_order": work_order.name,
        "operation": next_op.operation
    })
    if existing:
        frappe.msgprint(f"Job Card already exists for: {next_op.operation}")
        return

    # Create Job Card for next operation
    job_card_data = get_job_card_data(work_order.name, next_op.operation)
    job_card = frappe.new_doc("Job Card")
    job_card.update(job_card_data)
    job_card.for_quantity = work_order.qty
    job_card.save()
    frappe.msgprint(f"✅ Created Job Card for operation: {next_op.operation}")

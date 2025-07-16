import frappe
from frappe.utils import cint
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder

def create_job_card_only_first(self, *args, **kwargs):
    # Check if job cards already exist for this work order
    existing_job_cards = frappe.get_all("Job Card", 
                                      filters={"work_order": self.name},
                                      fields=["name"])
    
    if existing_job_cards:
        print(f"🔧 [DEBUG] Job cards already exist for {self.name}, skipping creation")
        return

    print("🔧 [DEBUG] Custom create_job_card_only_first called for:", self.name)

    if not self.operations:
        return

    first_row = self.operations[0]

    # Set accurate job card qty
    job_card_qty = self.qty
    first_row.job_card_qty = job_card_qty

    # Create Job Card directly
    job_card = frappe.new_doc("Job Card")
    job_card.work_order = self.name
    job_card.operation = first_row.operation
    job_card.workstation = first_row.workstation
    job_card.for_quantity = job_card_qty
    job_card.company = self.company
    job_card.posting_date = self.planned_start_date
    job_card.wip_warehouse = self.wip_warehouse
    job_card.insert()

    # Update planned end date
    if first_row.planned_end_time:
        self.db_set("planned_end_date", first_row.planned_end_time)

# Apply the override
WorkOrder.create_job_card = create_job_card_only_first
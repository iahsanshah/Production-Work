import frappe

def create_job_card(self):
    pass
#     manufacturing_settings_doc = frappe.get_doc("Manufacturing Settings")

#     enable_capacity_planning = not cint(manufacturing_settings_doc.disable_capacity_planning)
#     plan_days = cint(manufacturing_settings_doc.capacity_planning_for_days) or 30

#     if self.operations:
#         first_row = self.operations[0]
#         qty = self.qty
#         while qty > 0:
#             qty = split_qty_based_on_batch_size(self, first_row, qty)
#             if first_row.job_card_qty > 0:
#                 self.prepare_data_for_job_card(first_row, 0, plan_days, enable_capacity_planning)
#         # Set planned_end_date based on the first operation only
#         if first_row.planned_end_time:
#             self.db_set("planned_end_date", first_row.planned_end_time)

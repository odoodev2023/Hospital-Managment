from odoo import api, fields, models




class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"

    reference_record = fields.Reference([('hospital.pat','patient')], string="Record")

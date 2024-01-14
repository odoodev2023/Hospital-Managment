from odoo import api, fields, models


class Inherit(models.Model):
        _inherit = 'sale.order'

        new_field = fields.Char(string="New Field")









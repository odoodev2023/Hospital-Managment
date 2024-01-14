from datetime import date
import datetime
from odoo import api, fields, models , _
from odoo.exceptions import ValidationError


class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointment, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        return res

    name = fields.Char(string="Name")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", domain=[('state','=','draft')])
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Date Cancellation")



    def action_cancel(self):
        if self.appointment_id.booking_date == fields.date.today():
            raise ValidationError(_("TEST"))

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }



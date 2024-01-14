from odoo import api, fields, models
from datetime import date, datetime


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.pat', string="patient", ondelete='cascade', tracking=1)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], related='patient_id.gender', tracking=2)
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(string='Booking Date', tracking=10)
    ref = fields.Char(string="Reference")
    Prescription = fields.Html(string='Prescription' , tracking=15)
    note = fields.Char(string="Age Num")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], default='draft', string="Status", required=True)







    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    #def print_ruselt(self):

      #  serach_test = self.env['hospital.pat'].search([('age','>',5)])
       # count_test = serach_test.search_count([])
       # for rec in serach_test:
        #    rec.phone = 158766565653 + count_test



    @api.model
    def create(self):
        record['name'] = self.env['ir.sequence'].next_by_code('customer.sequence')
        return super(HospitalPatient , self).create(record)







    def action_test(self):
        return


    def action_cancel(self):
        action = self.ref('hospital2.action_cancel_appointment').read()[0]
        return action
















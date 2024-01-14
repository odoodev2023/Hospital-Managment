from datetime import date
from odoo import api, fields, models , _
from odoo.exceptions import ValidationError




class HospitalPatient(models.Model):
    _name = "hospital.pat"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Pat"

    name = fields.Char(string="Name", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ], string='Gender', tracking=True)
    ref = fields.Char(string="Reference")
    date_of_brith = fields.Date(string='Date of Brith')
    age = fields.Integer(string="age", compute='_compute_age', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    appointment = fields.Many2one('hospital.appointment', string="Appointment")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    website = fields.Char(string="Website")
    code = fields.Text(string="Code")
    sequence = fields.Integer(string="Sequence", default=10)



    def action_view_appointment(self):
        return

    def test_action(self):
        record = self.env['hospital.pat'].search([])
        print('>>>>>>>>>>>>>>>>>', record.mapped('age'))


    @api.returns('self', lambda x: x.id )
    def copy(self, default=None):
        if not default:
            default = {}
            default['name']= _("%s (copy)", self.name)
            return super(HospitalPatient, self).copy(default=default)





    def actionclick_test(self):
        print('clicked')
        return




    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment:
                raise ValidationError(_('cannot be deleted'))






    @api.model
    def create(self,vals):
        print("odoo mad" , vals)
        vals ['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self,vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    def _compute_age(self):

        for rec in self:
            today = date.today()
            if rec.date_of_brith:
                rec.age = today.year - rec.date_of_brith.year
            else:
                rec.age = 0



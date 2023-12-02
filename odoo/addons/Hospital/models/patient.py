from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Records'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string='Are you Child?')
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('Male','male'),('Female','female'),('Others','others')],string='Gender')

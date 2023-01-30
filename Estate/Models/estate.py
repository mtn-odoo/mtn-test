from odoo import fields, models

class estate(models.Model):
    _name = "estate"
    _description = "pour vendre ta dar"

    name = fields.Char()
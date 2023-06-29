from odoo import fields, models

class estate(models.Model):
    _name = "estate_property"
    _description = "type de bien"

    name = fields.Char(required=True, index=True)

    
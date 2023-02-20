from odoo import fields, models

class estate(models.Model):
    _name = "estate"
    _description = "pour vendre ta dar"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_avaibility = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('nord','Nord'),('sud','Sud'),('est','Est'),('ouest','Ouest')]
    )
    
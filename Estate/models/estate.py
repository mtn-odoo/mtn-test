from odoo import fields, models

class estate(models.Model):
    _name = "estate"
    _description = "pour vendre ta dar"

    name = fields.Char(required=True, index=True)
    description = fields.Text()
    postcode = fields.Char()
    date_avaibility = fields.Date(copy=False,default=lambda self:fields.Date.add(fields.Date.today(),months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    active = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('nord','Nord'),('sud','Sud'),('est','Est'),('ouest','Ouest')]
    )
    state = fields.Selection(
        string='State',
        selection=[('new','New'),('offer eeceived','Offer Received')]
    )
    
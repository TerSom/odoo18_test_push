from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property'
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, degfault=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False,default=10000)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        selection=[
        ('north', 'North'), 
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
        ],
        default="north"
    )
    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[
            ('new','New'),
            ('offer Received','Offer Received'),
            ('offer Accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')
        ],
        required=True,
        copy=False,
        default="new",
    )

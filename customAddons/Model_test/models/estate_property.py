from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property'
    
    title = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, degfault=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False,default=10000)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
        ('north', 'North'), 
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
        ],
        default="north"
    )
    active = fields.Boolean(default=True)
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
    
    property_type_id = fields.Many2one("estate.property.type", string="property type")
    property_tag_ids = fields.Many2many("estate.property.tag", string="property tag")
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.users', string='Buyer',copy=False ,index=True, )
    offer_ids = fields.One2many ("estate.property.offer", "property_id", string="Offers")
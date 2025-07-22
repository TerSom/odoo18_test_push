from odoo import models,field

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property'
    
    name = field.Char(required=True)
    description = field.Text()
    postcode = field.Char()
    date_availability = field.Date()
    expected_price = field.Float(required=True)
    selling_price = field.Float()
    bedrooms = field.Integer()
    living_area = field.Integer()
    facades = field.Interger()
    garage = field.Bolean()
    garden_area = field.Bolean()
    garden_orientation = field.Selection(
        ('north', 'North'), 
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    )
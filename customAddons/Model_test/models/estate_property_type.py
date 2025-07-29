from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"
    
    name = fields.Char(required=True)
    
    _sql_constraints = [
        ('check_nama_unique', 'UNIQUE(name)',
         'nama harus uniq.')
    ]
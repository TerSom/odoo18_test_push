from odoo import models, fields, api

class Category(models.Model):
    _name = "book.category"
    _description = "Book category table"
    
    name = fields.Char(string="Category")
    description = fields.Text(string="Description")
    color = fields.Integer(string="Color")

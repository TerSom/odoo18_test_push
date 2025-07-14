from odoo import models, fields, api

class Tag(models.Model):
    _name = "book.tag"
    _description = "Book tag table"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    color = fields.Integer(string="Color")

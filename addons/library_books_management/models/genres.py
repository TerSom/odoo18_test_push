from odoo import models, fields, api

class Genre(models.Model):
    _name = "book.genre"
    _description = "Book genre table"
    
    name = fields.Char(string="Genre")
    description = fields.Text(string="Description")
    book_id = fields.Many2many("book", string="Book")
    color = fields.Integer(string="Color")

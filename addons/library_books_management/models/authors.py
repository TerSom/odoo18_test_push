from odoo import models, fields, api

class Author(models.Model):
    _name = "book.author"
    _description = "Book author table"

    name = fields.Char(string="Name")
    birthdate = fields.Date(string="Birthdate")
    description = fields.Text(string="Description")
    book_id = fields.One2many("book","author", string="Books")
    photo = fields.Binary(string="Photo")

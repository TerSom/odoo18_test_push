from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Judul Buku', required=True)
    author = fields.Char(string='Penulis')
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date(string='Tanggal Terbit')

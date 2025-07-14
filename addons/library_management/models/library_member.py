from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string='Nama Anggota', required=True)
    nis = fields.Char(string='NIS', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Nomor Telepon')

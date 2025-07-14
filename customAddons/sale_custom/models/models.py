from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_custom_field = fields.Char(string="Pelanggan")
    x_custom_fields = fields.Many2one(comodel_name='sale.order', string="alamat")
    x_additional_note = fields.Text(string="Catatan Tambahan")

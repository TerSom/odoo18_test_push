from odoo import models, fields, api

class Editorial(models.Model):
    _name = "book.editorial"
    _description = "Book editorial table"

    partner_id = fields.Many2one("res.partner", string="Name", required=True)
    name = fields.Char(related="partner_id.name", string="Name")
    street = fields.Char(related="partner_id.street", string="Street")
    city = fields.Char(related="partner_id.city", string="City")
    state = fields.Many2one(related="partner_id.state_id", string="State")
    zip = fields.Char(related="partner_id.zip", string="ZIP")
    country = fields.Many2one(related="partner_id.country_id", string="Country")
    phone = fields.Char(related="partner_id.phone", string="Phone")
    mobile = fields.Char(related="partner_id.mobile", string="Mobile")
    book_id = fields.One2many("book","editorial", string="Book")
    description = fields.Text(string="Description")

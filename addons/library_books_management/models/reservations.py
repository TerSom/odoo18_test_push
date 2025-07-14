from odoo import fields, models, api

class Reservation(models.Model):
    _name = "book.reservation"
    _description = "Book reservation table"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "date asc"

    partner_id = fields.Many2one("res.partner", string="Contact")
    street = fields.Char(related="partner_id.street", string="Street")
    city = fields.Char(related="partner_id.city", string="City")
    state = fields.Many2one(related="partner_id.state_id", string="State")
    zip = fields.Char(related="partner_id.zip", string="ZIP")
    country = fields.Many2one(related="partner_id.country_id", string="Country")
    phone = fields.Char(related="partner_id.phone", string="Phone")
    mobile = fields.Char(related="partner_id.mobile", string="Mobile")
    book_id = fields.Many2one("book", string="Book")
    date = fields.Date(string="Date")
    done = fields.Boolean(string="Done")

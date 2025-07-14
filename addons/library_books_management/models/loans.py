from odoo import fields, models, api

class Loan(models.Model):
    _name = "book.loan"
    _description = "Book loan table"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'end_date asc'

    partner_id = fields.Many2one("res.partner", string="Contact")
    street = fields.Char(related="partner_id.street", string="Street")
    city = fields.Char(related="partner_id.city", string="City")
    state = fields.Many2one(related="partner_id.state_id", string="State")
    zip = fields.Char(related="partner_id.zip", string="ZIP")
    country = fields.Many2one(related="partner_id.country_id", string="Country")
    phone = fields.Char(related="partner_id.phone", string="Phone")
    mobile = fields.Char(related="partner_id.mobile", string="Mobile")
    book_id = fields.Many2one("book", string="Book")
    name = fields.Char(related="book_id.name", string="Book name")
    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")
    returned = fields.Boolean(string="Returned")
    not_returned = fields.Boolean(compute="_compute_decoration")

    @api.depends('returned', 'end_date')
    def _compute_decoration(self):
        for record in self:
            if record.end_date:
                record.not_returned = not record.returned and record.end_date <= fields.Date.today()
            else:
                record.not_returned = False

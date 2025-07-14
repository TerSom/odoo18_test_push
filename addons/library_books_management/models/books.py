# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'book'
    _description = 'Book table'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    author = fields.Many2one("book.author",string="Author", required=True)
    isbn = fields.Integer(string="ISBN")
    genre = fields.Many2many("book.genre",string="Genre")
    category = fields.Many2many("book.category",string="Category")
    description = fields.Text(string="Description")
    summary = fields.Text(string="Summary")
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('damaged', 'Damaged'),
        ('not available', 'Not available'),
        ('reserved', 'Reserved'),
        ('lost', 'Lost'),
        ('repairing', 'Repairing'),
        ('archived', 'Archived')
    ], string='Status', default='available', tracking=20)
    editorial = fields.Many2one("book.editorial",string="Editorial")
    published_date = fields.Date(string="Published date")
    image = fields.Binary(string="Image", store=True)
    tags = fields.Many2many("book.tag",string="Tags")
    loans = fields.One2many("book.loan",'book_id', string="Loans")
    reservations = fields.One2many("book.reservation","book_id", string="Reservations")
    active = fields.Boolean(string="Active", default=True)

    def action_available(self):
        self.state = "available"

    def action_borrowed(self):
        self.state = "borrowed"

    def action_damaged(self):
        self.state = "damaged"

    def action_not_available(self):
        self.state = "not available"

    def action_reserved(self):
        self.state = "reserved"

    def action_lost(self):
        self.state = "lost"

    def action_repairing(self):
        self.state = "repairing"

    def action_archived(self):
        self.state = "archived"

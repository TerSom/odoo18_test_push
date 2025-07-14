# -*- coding: utf-8 -*-
# from odoo import http


# class BelajarOdoo(http.Controller):
#     @http.route('/belajar_odoo/belajar_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/belajar_odoo/belajar_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('belajar_odoo.listing', {
#             'root': '/belajar_odoo/belajar_odoo',
#             'objects': http.request.env['belajar_odoo.belajar_odoo'].search([]),
#         })

#     @http.route('/belajar_odoo/belajar_odoo/objects/<model("belajar_odoo.belajar_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('belajar_odoo.object', {
#             'object': obj
#         })


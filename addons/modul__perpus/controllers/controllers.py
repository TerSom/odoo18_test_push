# -*- coding: utf-8 -*-
# from odoo import http


# class ModulPerpus(http.Controller):
#     @http.route('/modul__perpus/modul__perpus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul__perpus/modul__perpus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul__perpus.listing', {
#             'root': '/modul__perpus/modul__perpus',
#             'objects': http.request.env['modul__perpus.modul__perpus'].search([]),
#         })

#     @http.route('/modul__perpus/modul__perpus/objects/<model("modul__perpus.modul__perpus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul__perpus.object', {
#             'object': obj
#         })


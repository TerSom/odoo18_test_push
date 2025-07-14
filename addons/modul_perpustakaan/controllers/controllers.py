# -*- coding: utf-8 -*-
from odoo import http


class ModulPerpustakaan(http.Controller):
    @http.route('/modul_perpustakaan/modul_perpustakaan', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/modul_perpustakaan/modul_perpustakaan/objects', auth='public')
    def list(self, **kw):
        return http.request.render('modul_perpustakaan.listing', {
            'root': '/modul_perpustakaan/modul_perpustakaan',
            'objects': http.request.env['modul_perpustakaan.modul_perpustakaan'].search([]),
        })

    @http.route('/modul_perpustakaan/modul_perpustakaan/objects/<model("modul_perpustakaan.modul_perpustakaan"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('modul_perpustakaan.object', {
            'object': obj
        })


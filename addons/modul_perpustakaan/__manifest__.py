# -*- coding: utf-8 -*-
{
    'name': "modul_perpustakaan",

    'summary': "Modul Manajemen Perpustakaan",

    'description': """
Modul untuk mengelola data buku perpustakaan
    """,

    'author': "Terry",
    'website': "https://www.yourcompany.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/perpustakaan_menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}

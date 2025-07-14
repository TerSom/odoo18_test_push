# -*- coding: utf-8 -*-
{
    'name': "Library management",

    'summary': "Manage the entry and exit of books from a library",

    'description': """
Manage the entry and exit of books from a library
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library Management',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/books_views.xml',
        'views/reservations_views.xml',
        'views/loans_views.xml',
        'views/genres_views.xml',
        'views/categories_views.xml',
        'views/editorials_views.xml',
        'views/authors_views.xml',
        'views/tags_views.xml',
        'views/book_menus.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
    'installable': True,
    'application': True,  # Esto indica que tu módulo es una aplicación.
    'auto_install': False,
}

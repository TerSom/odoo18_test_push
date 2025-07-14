{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Modul Perpustakaan sederhana',
    'sequence': 10,
    'description': """ Manajemen Buku & Siswa """,
    'category': 'Tools',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

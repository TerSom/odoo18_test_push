{
    'name': "Test modell",
    'version': '1.0',
    'depends': [
        'base',
        
        ],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    'application': True,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}
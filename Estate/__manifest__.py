{
    'name' : 'Estate',
    'version' : '1.2',
    'summary': 'estate mtn',
    'sequence': 10,
    'description': """
test test
    """,
    'category': 'mtn test',
    'depends' : ['base_setup'],
    'data': [
        'views/estate.xml',
        'security/state.csv',
        'security/access.csv'
    ],
    'demo': [
        'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
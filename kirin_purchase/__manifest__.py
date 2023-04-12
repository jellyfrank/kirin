# -*- coding: utf-8 -*-
{
    'name': "Kirin Purchase",

    'summary': """
        Kirin Purchase
    """,

    'description': """
        Kirin Purchase
    """,

    'author': "Kevin Kong",
    'website': "https://www.odoomommy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'odoomommy.com',
    'version': '16.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase','mommy_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/kirin_wizard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

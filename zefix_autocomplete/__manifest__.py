# -*- coding: utf-8 -*-
{
    'name': "Zefix Autocomplete",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Abilium GmbH",
    'website': "https://www.abilium.io",

    'category': 'Hidden/Tools',
    'version': '0.1',
    'application': True,

    'depends': [
        'base',
        'contacts',
        'partner_autocomplete'
    ],

    'data': [
        'views/config_settings.xml',
        'static/src/base.xml'
    ]
}

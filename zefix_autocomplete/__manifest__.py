# -*- coding: utf-8 -*-
{
    'name': "Zefix Autocomplete",

    'summary': """
        Fetches company details when entering the company name from the swiss company register Zefix.ch
    """,

    'description': """
        The credentials can be specified in the configuration settings
    """,

    'author': "Abilium GmbH",
    'website': "https://www.abilium.io",

    'category': 'Hidden/Tools',
    'version': '17.0.0.0.1',
    'application': True,

    'depends': [
        'contacts',
        'partner_autocomplete'
    ],

    'data': [
        'views/config_settings.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ]
    }
}

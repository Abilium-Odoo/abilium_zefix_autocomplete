# -*- coding: utf-8 -*-

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    zefix_login = fields.Char(
        string='Zefix Login',
        config_parameter='abilium_zefix_autocomplete.zefix_login'
    )

    zefix_password = fields.Char(
        string='Zefix Password',
        config_parameter='abilium_zefix_autocomplete.zefix_password'
    )

    zefix_is_prod = fields.Boolean(
        string='Is Production',
        config_parameter='abilium_zefix_autocomplete.zefix_is_prod',
        help='Specifies if the production API should be used.'
    )

# -*- coding: utf-8 -*-

from odoo import models, fields, api
from requests import post, get, exceptions
from requests.auth import HTTPBasicAuth
import logging
_logger = logging.getLogger(__name__)

ZEFIX_API_PROD = 'https://www.zefix.admin.ch/ZefixPublicREST/api/v1/'
ZEFIX_API_TEST = 'https://www.zefixintg.admin.ch/ZefixPublicREST/api/v1/'


class ZefixAutocomplete(models.Model):
    _inherit = 'res.partner'

    @api.model
    def enrich_company(self, company_domain, partner_gid, vat, zefix_uid):
        if zefix_uid:
            return self._enrich_zefix_company(zefix_uid)
        else:
            return super(ZefixAutocomplete, self).enrich_company(company_domain, partner_gid, vat)

    @api.model
    def autocomplete(self, query):
        results = super(ZefixAutocomplete, self).autocomplete(query)

        zefix_results = self._search_zefix(query)
        zefix_results.extend(results)
        return zefix_results

    @api.model
    def _search_zefix(self, query):
        try:
            res = post(
                url=self._get_zefix_api_url() + 'company/search',
                auth=self._get_zefix_auth(),
                json={'name': query}
            )
        except exceptions.RequestException as error:
            _logger.info('Request Error: %s' % error)
        else:
            if res.status_code != 200:
                _logger.info('Error Response, Status Code: %d' % res.status_code)

            return self._format_zefix_companies_short_data(res.json())

    @api.model
    def _enrich_zefix_company(self, zefix_uid):
        try:
            res = get(
                url=self._get_zefix_api_url() + 'company/uid/' + str(zefix_uid),
                auth=self._get_zefix_auth()
            )
        except exceptions.RequestException as error:
            _logger.info('Request Error: %s' % error)
        else:
            if res.status_code != 200:
                _logger.info('Error Response, Status Code: %d' % res.status_code)

            return self._format_zefix_company_full_data(res.json())

    @api.model
    def _get_zefix_auth(self):
        login = self.env['ir.config_parameter'].sudo().get_param('zefix_autocomplete.zefix_login')
        password = self.env['ir.config_parameter'].sudo().get_param('zefix_autocomplete.zefix_password')
        return HTTPBasicAuth(login, password)

    @api.model
    def _get_zefix_api_url(self):
        prod = self.env['ir.config_parameter'].sudo().get_param('zefix_autocomplete.zefix_is_prod')
        return ZEFIX_API_PROD if prod else ZEFIX_API_TEST

    @api.model
    def _format_zefix_companies_short_data(self, companies):
        results = []

        for company in companies:
            results.append({
                'name': company.get('name'),
                'zefix_uid': company.get('uid'),
                'vat': company.get('uid')[:3] + '-' + company.get('uid')[3:6] + '.' + company.get('uid')[6:9] + '.' + company.get('uid')[9:12] + ' MWST',
                'country_id': self.env.ref('base.ch').id
            })

        return results

    @api.model
    def _format_zefix_company_full_data(self, company_list):
        assert len(company_list) == 1

        company = company_list[0]
        return {
            'name': company.get('name'),
            'country_id': self.env.ref('base.ch').id,
            'street': company.get('address').get('street') + ' ' + company.get('address').get('houseNumber'),
            'street2': company.get('address').get('addon'),
            'zip': company.get('address').get('swissZipCode'),
            'city': company.get('address').get('city')
        }

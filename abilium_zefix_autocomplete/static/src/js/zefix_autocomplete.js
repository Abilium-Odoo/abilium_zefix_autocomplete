odoo.define('abilium_zefix_autocomplete.autocomplete', function(require) {
	"use strict";

	var PartnerAutocompleteMixin = require('partner.autocomplete.Mixin');

	PartnerAutocompleteMixin._enrichCompany = function (company) {
		return this._rpc({
			model: 'res.partner',
			method: 'enrich_company',
			args: [company.website, company.partner_gid, company.vat, company.zefix_uid],
		});
	}

	return PartnerAutocompleteMixin;
});

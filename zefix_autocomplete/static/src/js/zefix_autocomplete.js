/** @odoo-module **/

import { usePartnerAutocomplete } from "@partner_autocomplete/js/partner_autocomplete_core";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";


patch(usePartnerAutocomplete.prototype, {
    const orm = useService("orm");

    enrichCompany(company) {
        return orm.call({
			model: 'res.partner',
			method: 'enrich_company',
			args: [company.website, company.partner_gid, company.vat, company.zefix_uid],
		});
    }
});

# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('sale_order_template_id')
    def _onchange_sale_order_template_id(self):
        sale_order_template = self.sale_order_template_id.with_context(lang=self.partner_id.lang)

        order_lines_data = [fields.Command.clear()]
        order_lines_data += [
            fields.Command.create(line._prepare_order_line_values())
            for line in sale_order_template.sale_order_template_line_ids
        ]

        # set first line to sequence -99, so a resequence on first page doesn't cause following page
        # lines (that all have sequence 10 by default) to get mixed in the first page
        if len(order_lines_data) >= 2:
            order_lines_data[1][2]['sequence'] = -99

        if not self.opportunity_id and self.sale_order_template_id:
            self.order_line = order_lines_data

        option_lines_data = [fields.Command.clear()]
        option_lines_data += [
            fields.Command.create(option._prepare_option_line_values())
            for option in sale_order_template.sale_order_template_option_ids
        ]
        self.sale_order_option_ids = option_lines_data

# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    order_line_ids = fields.One2many('crm.lead.products', 'lead_id', string='Orderline')
    currency_id = fields.Many2one('res.currency', string="Currency",related="company_currency" )
    total = fields.Monetary(string="Total", compute='_compute_total')

    def action_new_quotation(self):
        action = super(CrmLead, self).action_new_quotation()
        vals = [fields.Command.clear()]
        for order in self.order_line_ids:
            order.ensure_one()
            vals.append(fields.Command.create({
                'product_id': order.product_id.id,
                'name': order.name,
                'product_uom_qty': order.product_uom_qty,
                'price_unit': order.price_unit,
                'price_subtotal': order.price_subtotal,
            }))
        if action and 'context' in action:
            action['context'].update({
                'default_order_line': vals,
            })
        return action

    @api.depends('order_line_ids.product_id', 'order_line_ids.product_uom_qty')
    def _compute_total(self):
        total_count = 0
        for price in self.order_line_ids:
            total_count += price.price_subtotal
        self.total = total_count


class CrmProducts(models.Model):
    _name = 'crm.lead.products'

    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Text(string='Description')
    product_uom_qty = fields.Float(string='Quantity', default="1")
    price_unit = fields.Float(string='Unit Price')
    lead_id = fields.Many2one('crm.lead', string='Relation Field')
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal')
    company_id = fields.Many2one('res.company', string='Company', readonly=True,
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string='Currency')

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.price_unit = self.product_id.list_price
            self.name = self.product_id.name

    @api.constrains('product_id')
    def _constrains_product(self):
        if not self.product_id or len(self.product_id) == 0:
            raise ValidationError("You must add at least one product!")

    @api.depends('product_id', 'product_uom_qty', 'price_unit')
    def _compute_subtotal(self):
        for total in self:
            total.price_subtotal = total.product_uom_qty * total.price_unit

# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_categ_id = fields.Many2one('product.category', 'Product Category', related='product_id.categ_id', store=True)

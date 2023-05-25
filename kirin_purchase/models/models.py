#!/usr/bin/python3
# @Time    : 2023-04-12
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class purchase_order(models.Model):
    _inherit="purchase.order"

    @api.depends("receipt_status","order_line.product_qty","order_line.qty_received")
    def _compute_is_partial_order(self):
        """部分订单接收"""
        # 判断条件： 订单完全开票 + 订单数量不等于接收数量
        for order in self:
            order.is_partial_order = False
            if order.receipt_status == 'full' and order.order_line.filtered(lambda l:l.product_qty != l.qty_received):
                order.is_partial_order = True

    is_partial_order = fields.Boolean("Partial Ordered", compute="_compute_is_partial_order",store=True)

    def action_create_invoice(self):
        for order in self:
            super(purchase_order,order).action_create_invoice()
        return self.invoice_ids.get_view_action()
#!/usr/bin/python3
# @Time    : 2023-04-12
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class kirin_purchase_wizard(models.Model):
    _name = "purchase.confirm.wizard"

    def button_confirm(self):
        """批量确认采购订单"""
        for order in self.active_records:
            order.button_confirm()
            picking_ids = order.picking_ids.filtered(lambda p:p.state not in ['cancel','done'])
            picking_ids.set_done_quantity()
            picking_ids.action_confirm()
            picking_ids.button_validate()
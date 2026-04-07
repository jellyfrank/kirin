#!/usr/bin/python3
# @Time    : 2023-04-12
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class stock_picking(models.Model):
    _inherit="stock.picking"

    def set_done_quantity(self):
        """设置完成数量"""
        for move in self.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
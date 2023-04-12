#!/usr/bin/python3
# @Time    : 2023-04-12
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class purchase_order(models.Model):
    _inherit="purchase.order"

    
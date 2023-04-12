#!/usr/bin/python3
# @Time    : 2022-10-08
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class ir_model(models.Model):
    _inherit="ir.model"

    track = fields.Boolean('Track All', help='Track all fields changes and displaying on chatter?')



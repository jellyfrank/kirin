# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.osv import expression

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        """
        创建行时自动排序
        :param vals: 创建数据
        :return: 记录集
        """
        res = super(AccountMove, self).create(vals_list)
        for move in res:
            if move.line_ids:
                base_sequence = 1
                for line in move.line_ids:
                    line.sequence += base_sequence
                    base_sequence += 1
                move.line_ids[0]._compute_sequence()
        return res

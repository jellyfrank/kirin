# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.osv import expression


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    categ_id = fields.Many2one('product.category', 'Product Category', related='product_id.categ_id', store=True)
    barcode = fields.Char('Product Barcode', related='product_id.barcode', store=True)

    @api.depends('display_type', 'product_id', 'product_id.categ_id')
    def _compute_sequence(self):
        """
        重定义display_type=product的排序方式（相对）
        :return: 客户端动作
        """
        seq_map = {
            'tax': 10000,
            'rounding': 11000,
            'payment_term': 12000,
        }
        for line in self:
            line.sequence = seq_map.get(line.display_type, line.sequence or 100)

        def sort_key(l):
            if not l.product_id or not l.product_id.categ_id:
                return (999, '')
            categ = l.product_id.categ_id
            depth = len(categ.parent_path.split('/')) - 1 if categ.parent_path else 0
            return (depth, categ.name)

        for move in self.mapped('move_id'):
            lines = move.line_ids.sorted('sequence')

            current_group = []
            group_sequences = []

            for line in lines:
                if line.display_type == 'product':
                    current_group.append(line)
                    group_sequences.append(line.sequence)
                else:
                    if current_group:
                        sorted_products = sorted(current_group, key=sort_key)
                        group_sequences.sort()
                        for prod_line, seq in zip(sorted_products, group_sequences):
                            prod_line.sequence = seq

                        current_group = []
                        group_sequences = []

            # 处理末尾的产品组
            if current_group:
                sorted_products = sorted(current_group, key=sort_key)
                group_sequences.sort()
                for prod_line, seq in zip(sorted_products, group_sequences):
                    prod_line.sequence = seq

    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super(AccountMoveLine, self).create(vals_list)
    #     self._compute_sequence()
    #     return res

    # @api.model
    # def write(self, vals):
    #     res = super(AccountMoveLine, self).write(vals)
    #     return res
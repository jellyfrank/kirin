# -*- coding: utf-8 -*-
# from odoo import http


# class KirinPurchase(http.Controller):
#     @http.route('/kirin_purchase/kirin_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kirin_purchase/kirin_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kirin_purchase.listing', {
#             'root': '/kirin_purchase/kirin_purchase',
#             'objects': http.request.env['kirin_purchase.kirin_purchase'].search([]),
#         })

#     @http.route('/kirin_purchase/kirin_purchase/objects/<model("kirin_purchase.kirin_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kirin_purchase.object', {
#             'object': obj
#         })

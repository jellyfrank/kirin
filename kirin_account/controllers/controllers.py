# -*- coding: utf-8 -*-
# from odoo import http


# class KirinAccount.(http.Controller):
#     @http.route('/kirin_account./kirin_account.', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kirin_account./kirin_account./objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kirin_account..listing', {
#             'root': '/kirin_account./kirin_account.',
#             'objects': http.request.env['kirin_account..kirin_account.'].search([]),
#         })

#     @http.route('/kirin_account./kirin_account./objects/<model("kirin_account..kirin_account."):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kirin_account..object', {
#             'object': obj
#         })

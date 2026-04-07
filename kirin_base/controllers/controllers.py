# -*- coding: utf-8 -*-
# from odoo import http


# class KirinBase(http.Controller):
#     @http.route('/kirin_base/kirin_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kirin_base/kirin_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kirin_base.listing', {
#             'root': '/kirin_base/kirin_base',
#             'objects': http.request.env['kirin_base.kirin_base'].search([]),
#         })

#     @http.route('/kirin_base/kirin_base/objects/<model("kirin_base.kirin_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kirin_base.object', {
#             'object': obj
#         })

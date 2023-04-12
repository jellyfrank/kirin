#!/usr/bin/python3
# @Time    : 2022-04-24
# @Author  : Kevin Kong (kfx2007@163.com)

import odoo
from odoo.http import request
import json


class MommyBase(http.Controller):
    @http.route('/mommy/get_quick_edit/')
    def index(self, **kw):
        """wether use quick edit or not."""
        enable = bool(request.env['ir.config_parameter'].sudo(
        ).get_param("mommy.quick.edit", True))
        return json.dumps({"quick_edit": enable})
